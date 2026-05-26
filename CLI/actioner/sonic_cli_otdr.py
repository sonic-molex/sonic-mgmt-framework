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
    otdr_name = ""
    if func == "get_otdr_config_common":
        path = cc.Path("/restconf/data/openconfig-gnoi-otdr:optical-time-domain-reflectometer/config-common")
        return aa.get(path)
    elif func == "get_otdr_port_info":
        otdr_name = args[1]
        path = cc.Path("/restconf/data/openconfig-gnoi-otdr:optical-time-domain-reflectometer/otdrs/otdr={otdr_name_key}", otdr_name_key=otdr_name)
        return aa.get(path)
    elif func == "patch_otdr_config_common_scan_type":
        #format args=['LineIn/LineOut/OtdrOut', 'otdr', 'config-common', 'scan-type', 'LineIn/LineOut/OtdrOut', 'field', 'value']
        #Eg. ['medium', 'otdr', 'config-common', 'scan-type', 'medium', 'acquisition-time-s', '12']
        #print(f"{args}")
        scan_type = args[0]
        field_name = args[5]
        field_val = None
        #print("type(args[6])", type(args[6]))
        if (field_name == "acquisition-time-s") or (field_name == "range-m") or (field_name == "pulse-width-ns"):
            #string -> int
            field_val = int(args[6])
        elif (field_name == "wavelength-mhz"):
            #For uint64 leaf-node type, using string
            field_val = args[6]
        else:
            #string
            field_val = args[6]
        #print("type(field_val)", type(field_val))
        body = {}
        body_key = "openconfig-gnoi-otdr:" + field_name
        body[body_key] = field_val
        #print(f"{body}")
        # TODO  
        path = cc.Path("/restconf/data/openconfig-gnoi-otdr:optical-time-domain-reflectometer/config-common/scan-types={scan_type_key}/{field_name}", scan_type_key=scan_type, field_name=field_name)
        return aa.patch(path, body)
    elif func == "patch_otdr_config_common_fiber_profile":
        #format args=['otdr', 'config-common', 'fiber-profile', 'field', 'value']
        #Eg. 
        #print(f"{args}")
        field_name = args[3]
        field_val = args[4]
        # create body request
        body = {}
        body_key = "openconfig-gnoi-otdr:" + field_name
        body[body_key] = field_val
        #print(f"{body}")
        # TODO  
        path = cc.Path("/restconf/data/openconfig-gnoi-otdr:optical-time-domain-reflectometer/config-common/fiber-profile/{field_name}", field_name=field_name)
        return aa.patch(path, body)
    elif func == "patch_otdr_config_port_customized":
        #format args=['otdr', 'config', 'port', 'LineIn/LineOut/OtdrOut', 'field', 'value']
        #Eg. ['otdr', 'config', 'port', 'LineIn', 'range-m', '3']
        #print(f"{args}")
        otdr_name = args[3]
        field_name = args[4]
        field_val = args[5]

        if (field_name == "acquisition-time-s") or (field_name == "range-m") or (field_name == "pulse-width-ns"):
            #string -> int
            field_val = int(args[5])
        elif (field_name == "wavelength-mhz"):
            #For uint64 leaf-node type, using string
            field_val = args[5]
        else:
            #string
            field_val = args[5]
        # create body request
        body = {}
        body_key = "openconfig-gnoi-otdr:" + field_name
        body[body_key] = field_val
        #print(f"{body}")
        path = cc.Path("/restconf/data/openconfig-gnoi-otdr:optical-time-domain-reflectometer/otdrs/otdr={otdr_name_key}/config/{field_name}", otdr_name_key = otdr_name, field_name=field_name)
        return aa.patch(path, body)
    elif func == "post_rpc_otdr_scan":
        #format args=['otdr', 'exec', 'scan', 'start', 'port', 'LineIn/LineOut/OtdrOut', 'scan-type', 'short/medium/long/auto/customized'] 
        #        or ['otdr', 'exec', 'scan', 'stop']
        #print(f"{args}")
        rpc_operation = args[3]
        body = None
        if rpc_operation == "start":
            otdr_name = args[5]
            body = {
                    "openconfig-gnoi-otdr:input": {
                        "name":  otdr_name,
                        "operation": "start",
                        "otdr-scan-type": args[7]
                    }
                }
        else:
            body = {
                    "openconfig-gnoi-otdr:input": {
                        "operation": "stop"
                    }
                }
        #print(f"{body}")
        path = cc.Path("/restconf/operations/openconfig-gnoi-otdr:otdr-scan")
        return aa.post(path, body)


def run(func, args):
    # normal process
    #print("func:", func)
    #print("args:", args)
    api_response = invoke(func, args)
    #print("api_response:", api_response)
    if api_response.ok():
        if api_response.content is not None:
            if  func == "get_otdr_config_common" or func == "get_otdr_port_info":
                response = api_response.content
                #print("response:", response)
                show_cli_output(args[0], response)
            #elif func == "post_rpc_otdr_scan": 
                #print(api_response.content)
    else:
        print((api_response.error_message()))


if __name__ == "__main__":
    pipestr().write(sys.argv)
    run(sys.argv[1], sys.argv[2:])
