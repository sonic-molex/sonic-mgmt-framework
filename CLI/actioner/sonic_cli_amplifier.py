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
    edfa_name = ""
    if func == "get_openconfig_optical_amplifier_optical_amplifier_amplifiers_amplifier":
        edfa_name = args[1]
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}", edfa_name_key=edfa_name.upper())
        return aa.get(path)
    elif func == "patch_openconfig_optical_amplifier_optical_amplifier_amplifiers_amplifier_config_target_gain":
        #example args=['<value>', 'amplifier', 'pa/ba', '<field>', '<value>']
        edfa_name = args[2]
        body = {
                "openconfig-optical-amplifier:target-gain": args[0]
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}/config/target-gain",edfa_name_key=edfa_name.upper())
        return aa.patch(path, body)
    elif func == "patch_openconfig_optical_amplifier_optical_amplifier_amplifiers_amplifier_config_target_gain_tilt":
        #example args=['<value>', 'amplifier', 'pa/ba', '<field>', '<value>']
        edfa_name = args[2]
        body = {
                "openconfig-optical-amplifier:target-gain-tilt": args[0]
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}/config/target-gain-tilt",edfa_name_key=edfa_name.upper())
        return aa.patch(path, body)
    elif func == "patch_openconfig_optical_amplifier_optical_amplifier_amplifiers_amplifier_config_gain_range":
        #example args=['<value>', 'amplifier', 'pa/ba', '<field>', '<value>']
        edfa_name = args[2]
        # get gain-range 
        body = {
                "openconfig-optical-amplifier:gain-range": args[0]
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}/config/gain-range",edfa_name_key=edfa_name.upper())
        return aa.patch(path, body)
    elif func == "patch_openconfig_optical_amplifier_optical_amplifier_amplifiers_amplifier_config_enabled":
        #example args=['<value>', 'amplifier', 'pa/ba', '<field>', '<value>']
        edfa_name = args[2]
        bEnable = enableStrToBoolDict[args[0]]
        body = {
                "openconfig-optical-amplifier:enabled": bEnable
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}/config/enabled",edfa_name_key=edfa_name.upper())
        return aa.patch(path, body)
    elif func == "patch_com_oplink_amplifier_ext_optical_amplifier_amplifiers_amplifier_config_autolos":
        #example args=['<value>', 'amplifier', 'pa/ba', '<field>', '<value>']
        edfa_name = args[2]
        bEnable = enableStrToBoolDict[args[0]]
        body = {
                "com-oplink-amplifier-ext:autolos": bEnable
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}/config/com-oplink-amplifier-ext:autolos",edfa_name_key=edfa_name.upper())
        return aa.patch(path, body)
    elif func == "patch_com_oplink_amplifier_ext_optical_amplifier_amplifiers_amplifier_config_apr_enabled":
        #example args=['<value>', 'amplifier', 'pa/ba', '<field>', '<value>']
        edfa_name = args[2]
        bEnable = enableStrToBoolDict[args[0]]
        body = {
                "com-oplink-amplifier-ext:apr-enabled": bEnable
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}/config/com-oplink-amplifier-ext:apr-enabled",edfa_name_key=edfa_name.upper())
        return aa.patch(path, body)
    elif func == "patch_openconfig_optical_amplifier_optical_amplifier_amplifiers_amplifier_config_amp_mode":
        #example args=['<value>', 'amplifier', 'pa/ba', '<field>', '<value>']
        edfa_name = args[2]
        body = {
                "openconfig-optical-amplifier:amp-mode": args[0]
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}/config/amp-mode",edfa_name_key=edfa_name.upper())
        return aa.patch(path, body)
    elif func == "patch_openconfig_optical_amplifier_optical_amplifier_amplifiers_amplifier_config_target_output_power":
        #example args=['<value>', 'amplifier', 'pa/ba', '<field>', '<value>']
        edfa_name = args[2]
        body = {
                "openconfig-optical-amplifier:target-output-power": args[0]
            } 
        # TODO  
        path = cc.Path("/restconf/data/openconfig-optical-amplifier:optical-amplifier/amplifiers/amplifier={edfa_name_key}/config/target-output-power",edfa_name_key=edfa_name.upper())
        return aa.patch(path, body)
    


def run(func, args):
    # normal process
    #print("func:", func)
    #print("args:", args)
    api_response = invoke(func, args)
    if api_response.ok():
        if api_response.content is not None:
            response = api_response.content
            if "openconfig-optical-amplifier:amplifier" in list(response.keys()):
                value = response["openconfig-optical-amplifier:amplifier"]
                if value is None:
                    return
                show_cli_output(args[0], response)
    else:
        print((api_response.error_message()))


if __name__ == "__main__":

    pipestr().write(sys.argv)
    run(sys.argv[1], sys.argv[2:])
