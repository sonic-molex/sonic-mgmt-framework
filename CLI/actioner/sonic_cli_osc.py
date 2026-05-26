#!/usr/bin/python3

import sys
from scripts.rpipe_utils import pipestr
from scripts.render_cli import show_cli_output
import cli_client as cc

import urllib3

urllib3.disable_warnings()

enableStrToBoolDict = {"enable": True, "disable": False}

def invoke(func, args):
    body = None
    aa = cc.ApiClient()
    osc_name = ""
    if func == "get_supervisory_channel_osc":
        osc_name = args[1]
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/supervisory-channels/supervisory-channel={osc_name_key}", osc_name_key=osc_name.upper())
        return aa.get(path)
    elif func == "patch_supervisory_channel_osc_enabled":
        #example args=['enable/disable', 'ocs', 'ocs0-0', 'enabled', 'enable/disable']
        osc_name = args[2]
        bEnable = enableStrToBoolDict[args[0]]
        body = {
                "com-oplink-amplifier-ext:enabled": bEnable
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/supervisory-channels/supervisory-channel={osc_name_key}/config/com-oplink-amplifier-ext:enabled", osc_name_key=osc_name.upper())
        return aa.patch(path, body)


def run(func, args):
    # normal process
    api_response = invoke(func, args)
    if api_response.ok():
        if api_response.content is not None:
            response = api_response.content
            if "openconfig-optical-amplifier:supervisory-channel" in list(response.keys()):
                value = response["openconfig-optical-amplifier:supervisory-channel"]
                if value is None:
                    return
                show_cli_output(args[0], response)
    else:
        print((api_response.error_message()))


if __name__ == "__main__":

    pipestr().write(sys.argv)
    run(sys.argv[1], sys.argv[2:])
