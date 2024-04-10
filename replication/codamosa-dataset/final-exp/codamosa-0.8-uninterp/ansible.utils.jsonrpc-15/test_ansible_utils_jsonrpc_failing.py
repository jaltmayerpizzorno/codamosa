# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    try:
        list_0 = None
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.handle_request(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"jsonrpc": "2.0", "id": 1, "method": "status", "params": []}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.header()
    except BaseException:
        pass

def test_case_3():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{\n    "jsonrpc": "2.0",\n    "method": "rpc.run_command",\n    "params": [\n        "show version"\n    ],\n    "id": 12\n    }'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "jCw<IRWryS'HNrn"
        dict_0 = {str_0: str_0, str_0: str_0}
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.parse_error(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'S|zwP&-D:6[7Jw&'
        json_rpc_server_0 = module_0.JsonRpcServer()
        dict_0 = {str_0: json_rpc_server_0}
        var_0 = json_rpc_server_0.invalid_params(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = 'method'
        str_1 = 'params'
        var_0 = []
        var_1 = [var_0, str_1]
        var_2 = {str_0: str_0, str_1: var_1, str_0: str_1}
        var_3 = module_1.dumps(var_2)
        var_4 = json_rpc_server_0.handle_request(var_3)
        var_5 = json_rpc_server_0.internal_error(str_0)
    except BaseException:
        pass