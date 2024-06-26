# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    try:
        str_0 = '{"jsonrpc": "2.0", "method": "run_command", "params": [["show version"]], "id": "5"}'
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '_identifier'
        str_1 = 'ip'
        float_0 = None
        var_0 = json_rpc_server_0.register(float_0)
        var_1 = setattr(json_rpc_server_0, str_0, str_1)
        str_2 = 'ucse4name'
        str_3 = 'admin'
        str_4 = {str_2: str_3, str_1: str_1}
        var_2 = json_rpc_server_0.response(str_4)
        str_5 = 'C+b@\x0bgk'
        str_6 = 'a@j,9\\xm)'
        dict_0 = {str_3: json_rpc_server_0, str_5: var_0, str_6: var_1, str_2: str_6}
        var_3 = json_rpc_server_0.register(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.response()
    except BaseException:
        pass

def test_case_3():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.internal_error()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -776
        dict_0 = {}
        json_rpc_server_0 = module_0.JsonRpcServer(**dict_0)
        var_0 = json_rpc_server_0.parse_error(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"jsonrpc": "2.0", "method": "_connection.connection_error", "params": [], "id": 1}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{\n        "jsonrpc" : "2.0",\n        "method" : "invalid method",\n        "params" : [ "foo", "bar" ],\n        "id" : 2\n    }'
        var_0 = json_rpc_server_0.handle_request(str_0)
        str_1 = ''
        str_2 = None
        set_0 = {str_0, json_rpc_server_0, str_0, str_2}
        bool_0 = True
        tuple_0 = (str_1, set_0, bool_0)
        var_1 = json_rpc_server_0.invalid_params(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = 'method'
        str_1 = 'params'
        str_2 = 'testId'
        str_3 = 'rpc.method'
        int_0 = 2
        int_1 = [int_0, int_0]
        var_0 = {str_3: str_2, str_0: str_3, str_1: int_1}
        var_1 = module_1.dumps(var_0)
        var_2 = json_rpc_server_0.handle_request(var_1)
    except BaseException:
        pass