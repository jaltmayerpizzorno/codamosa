# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1
import ansible.module_utils.common.text.converters as module_2

def test_case_0():
    pass

def test_case_1():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    var_0 = setattr(json_rpc_server_0, str_0, str_0)
    str_1 = 'msg'
    var_1 = json_rpc_server_0.response(str_1)

def test_case_2():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '{"jsonrpc":"2.0","method":"test","params":[{"name":"foo"},{"name":"bar"}],"id":1}'
    var_0 = json_rpc_server_0.handle_request(str_0)

def test_case_3():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '\n        {\n            "jsonrpc": "2.0",\n            "method": "error",\n            "params": [\n                ["foo", "bar"],\n                {\n                    "LAZY_RESULT": true\n                }\n            ],\n            "id": "69cffa78-8cf1-4340-b2a2-7760f6e957b9"\n        }\n    '
    var_0 = json_rpc_server_0.handle_request(str_0)

def test_case_4():
    str_0 = 'This is a unit test for method response of class JsonRpcServer'
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_1 = '_identifier'
    int_0 = 1
    var_0 = setattr(json_rpc_server_0, str_1, int_0)
    str_2 = 'b'
    str_3 = 'e'
    str_4 = {str_1: str_3}
    str_5 = {str_0: str_2, str_0: str_4}
    str_6 = 'result: '
    var_1 = str_6 + str_6
    var_2 = print(var_1)
    var_3 = json_rpc_server_0.response(str_5)
    str_7 = 'actual_response: '
    var_4 = str_7 + str_2
    var_5 = print(var_4)
    str_8 = 'result_type'
    int_1 = 0
    var_6 = module_1.dumps(str_5)
    var_7 = module_2.to_text(var_6)
    str_9 = 'expect_response: '
    var_8 = str(str_8)
    var_9 = str_9 + var_8
    var_10 = print(var_9)