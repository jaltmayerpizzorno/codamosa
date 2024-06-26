# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'{"jsonrpc": "2.0", "method": "test_func", "params": [1, 2], "id": 1}'
    json_rpc_server_0 = module_0.JsonRpcServer()
    var_0 = json_rpc_server_0.handle_request(bytes_0)

def test_case_2():
    bytes_0 = b'{"jsonrpc": "2.0", "method": "test_func", "params": [1, 2], "id": 1}'
    json_rpc_server_0 = module_0.JsonRpcServer()
    var_0 = lambda *args, **kwargs: args
    var_1 = json_rpc_server_0.register(var_0)
    var_2 = json_rpc_server_0.handle_request(bytes_0)
    var_3 = module_1.loads(var_2)

def test_case_3():
    json_rpc_server_0 = module_0.JsonRpcServer()
    var_0 = json_rpc_server_0.register(json_rpc_server_0)
    str_0 = '_identifier'
    int_0 = 42
    var_1 = setattr(json_rpc_server_0, str_0, int_0)
    str_1 = 'hello world'
    var_2 = json_rpc_server_0.response(str_1)
    var_3 = module_1.dumps(var_2)

def test_case_4():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    str_1 = '42'
    var_0 = setattr(json_rpc_server_0, str_0, str_1)
    int_0 = 1
    var_1 = json_rpc_server_0.response()
    str_2 = 'error message'
    var_2 = json_rpc_server_0.error(int_0, str_2)

def test_case_5():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    str_1 = 'test'
    var_0 = setattr(json_rpc_server_0, str_0, str_1)
    int_0 = 1
    str_2 = 'error message'
    str_3 = 'data'
    var_1 = json_rpc_server_0.error(int_0, str_2, str_3)

def test_case_6():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    int_0 = 0
    var_0 = setattr(json_rpc_server_0, str_0, int_0)
    var_1 = json_rpc_server_0.response()
    var_2 = print(var_1)
    str_1 = 'Result'
    var_3 = json_rpc_server_0.response(str_1)
    var_4 = print(var_3)
    bytes_0 = b'Result'
    var_5 = json_rpc_server_0.response(bytes_0)
    var_6 = print(var_5)