# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    pass

def test_case_1():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = 'method'
    str_1 = 'params'
    str_2 = 'id'
    str_3 = 'response_method'
    var_0 = []
    var_1 = {}
    var_2 = [var_0, var_1]
    int_0 = 1
    var_3 = {str_0: str_3, str_1: var_2, str_2: int_0}
    list_0 = None
    var_4 = json_rpc_server_0.register(list_0)
    var_5 = module_1.dumps(var_3)
    var_6 = json_rpc_server_0.handle_request(var_5)
    var_7 = module_1.dumps(var_6)

def test_case_2():
    str_0 = '{"jsQnrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}'
    json_rpc_server_0 = module_0.JsonRpcServer()
    var_0 = json_rpc_server_0.handle_request(str_0)

def test_case_3():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    int_0 = 1
    var_0 = setattr(json_rpc_server_0, str_0, int_0)
    var_1 = json_rpc_server_0.response()

def test_case_4():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    str_1 = '1'
    var_0 = setattr(json_rpc_server_0, str_0, str_1)
    int_0 = 2
    str_2 = 'test'
    var_1 = json_rpc_server_0.error(int_0, str_2)
    str_3 = 'test2'
    var_2 = json_rpc_server_0.error(int_0, str_2, str_3)
    var_3 = delattr(json_rpc_server_0, str_0)

def test_case_5():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    str_1 = '12345'
    var_0 = setattr(json_rpc_server_0, str_0, str_1)
    str_2 = 'Hello, World!'
    var_1 = json_rpc_server_0.response(str_2)

def test_case_6():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    str_1 = '12'
    var_0 = setattr(json_rpc_server_0, str_0, str_1)
    var_1 = json_rpc_server_0.response()
    str_2 = 'some result'
    var_2 = json_rpc_server_0.response(str_2)
    bytes_0 = b'some result'
    var_3 = json_rpc_server_0.response(bytes_0)