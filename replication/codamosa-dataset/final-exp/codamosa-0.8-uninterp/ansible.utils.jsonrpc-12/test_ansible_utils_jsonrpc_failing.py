# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"jsonrpc": "2.0", "method": "response", "params": [null], "id": 1}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.register(json_rpc_server_0)
        str_0 = '{"jsonrpc": "2.0", "method": "response", "params": [null], "id": 1}'
        var_1 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.invalid_params()
    except BaseException:
        pass

def test_case_3():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.register(json_rpc_server_0)
        str_0 = '\n        {\n            "jsonrpc": "2.0",\n            "method": "error",\n            "params": [\n                ["foo", "bar"],\n                {\n                    "LAZY_RESULT": true\n                }\n            ],\n            "id": "69cffa78-8cf1-4340-b2a2-7760f6e957b9"\n        }\n    '
        var_1 = json_rpc_server_0.handle_request(str_0)
        var_2 = module_1.loads(var_1)
        float_0 = -1449.174
        dict_0 = {var_0: float_0, str_0: str_0}
        var_3 = json_rpc_server_0.parse_error(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        float_0 = 60.0
        json_rpc_server_0 = module_0.JsonRpcServer(*list_0)
        var_0 = json_rpc_server_0.invalid_request(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = 'jsonrpc'
        str_1 = 'method'
        str_2 = 'id'
        str_3 = '2.0'
        str_4 = '_rpc_method'
        int_0 = 0
        var_0 = {str_0: str_3, str_1: str_4, str_2: int_0}
        var_1 = module_1.dumps(var_0)
        var_2 = json_rpc_server_0.handle_request(var_1)
    except BaseException:
        pass

def test_case_6():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = 'method'
        str_1 = 'params'
        str_2 = 'id'
        str_3 = 'rpc.test'
        int_0 = 8
        str_4 = 'foo'
        var_0 = [int_0, str_4]
        int_1 = 1
        var_1 = {str_0: str_3, str_1: var_0, str_2: int_1}
        var_2 = module_1.dumps(var_1)
        var_3 = json_rpc_server_0.handle_request(var_2)
    except BaseException:
        pass