#!/usr/bin/python3

import sys
from scripts.rpipe_utils import pipestr
from scripts.render_cli import show_cli_output
import cli_client as cc

import urllib3

urllib3.disable_warnings()


def channel_sort(response):
    if "openconfig-channel-monitor:channels" in response and "channel" in response["openconfig-channel-monitor:channels"]:
        #print(response["openconfig-channel-monitor:channels"]["channel"])
        channel_array = response["openconfig-channel-monitor:channels"]["channel"]
        # Sort by lower-frequency, from largest to smallest
        sorted_channel_array = sorted(channel_array, key = lambda x:x["lower-frequency"], reverse=True)

        response["openconfig-channel-monitor:channels"]["channel"] = sorted_channel_array
    return response

def invoke(func, args):
    body = None
    aa = cc.ApiClient()
    ocm_name = ""
    if func == "get_ocm_port_channels":
        ocm_name = args[1]
        path = cc.Path("/restconf/data/openconfig-channel-monitor:channel-monitors/channel-monitor={ocm_name_key}/channels", ocm_name_key=ocm_name)
        return aa.get(path)
    elif func == "get_ocm_port_config":
        ocm_name = args[1]
        path = cc.Path("/restconf/data/openconfig-channel-monitor:channel-monitors/channel-monitor={ocm_name_key}/config", ocm_name_key=ocm_name)
        return aa.get(path)
    elif func == "patch_ocm_monitor_port":
        #example args=['LineIn/LineOut/ClientIn/ClientOut/OcmIn', 'ocm', 'channel-monitor', 'LineIn/LineOut/ClientIn/ClientOut/OcmIn', 'monitor-port', 'value']
        ocm_name = args[0]
        #print(f"{args}")
        body = {
                "openconfig-channel-monitor:monitor-port": args[5]
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-channel-monitor:channel-monitors/channel-monitor={ocm_name_key}/config/monitor-port", ocm_name_key=ocm_name)
        return aa.patch(path, body)


def run(func, args):
    # normal process
    #print("func:", func)
    #print("args:", args)
    api_response = invoke(func, args)
    #print("api_response:", api_response)
    if api_response.ok():
        if api_response.content is not None:
            if  func == "get_ocm_port_channels" or func == "get_ocm_port_config":
                response = api_response.content
                #print("response:", response)
                #if func == "get_ocm_port_channels":
                #    response = channel_sort(response)
                show_cli_output(args[0], response)
    else:
        print((api_response.error_message()))


if __name__ == "__main__":
    pipestr().write(sys.argv)
    run(sys.argv[1], sys.argv[2:])
