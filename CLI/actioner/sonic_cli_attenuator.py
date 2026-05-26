#!/usr/bin/python3

import sys
from scripts.rpipe_utils import pipestr
from scripts.render_cli import show_cli_output
import cli_client as cc

import urllib3

urllib3.disable_warnings()

def invoke(func, args):
    body = None
    aa = cc.ApiClient()
    voa_name = ""
    if func == "get_openconfig_optical_attenuator_optical_attenuator_attenuators_attenuator":
        voa_name = args[1]
        path = cc.Path("/restconf/data/openconfig-optical-attenuator:optical-attenuator/attenuators/attenuator={voa_name_key}", voa_name_key=voa_name.upper())
        return aa.get(path)
    elif func == "patch_openconfig_optical_attenuator_optical_attenuator_attenuators_attenuator_config_attenuation":
        #example args=['1.8', 'attenuator', 'voa1', 'attenuation', '1.8']
        voa_name = args[2]
        body = {
                "openconfig-optical-attenuator:attenuation": args[0]
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-attenuator:optical-attenuator/attenuators/attenuator={voa_name_key}/config/attenuation",voa_name_key=voa_name.upper())
        return aa.patch(path, body)


def run(func, args):
    # normal process
    #print("func:", func)
    #print("args:", args)
    api_response = invoke(func, args)
    #print("api_response:", api_response)
    if api_response.ok():
        if api_response.content is not None:
            response = api_response.content
            #print("response:", response)
            if "openconfig-optical-attenuator:attenuator" in list(response.keys()):
                value = response["openconfig-optical-attenuator:attenuator"]
                #print("value:", value)
                if value is None:
                    return
                show_cli_output(args[0], response)
    else:
        print((api_response.error_message()))


if __name__ == "__main__":

    pipestr().write(sys.argv)
    run(sys.argv[1], sys.argv[2:])
