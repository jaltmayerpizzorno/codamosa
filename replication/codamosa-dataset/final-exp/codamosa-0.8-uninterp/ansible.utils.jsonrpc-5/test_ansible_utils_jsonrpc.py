# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0

def test_case_0():
    pass

def test_case_1():
    json_rpc_server_0 = module_0.JsonRpcServer()
    bytes_0 = b'{"jsonrpc": "2.0", "method": "response", "params": [[], {}], "id": "1"}'
    var_0 = json_rpc_server_0.handle_request(bytes_0)

def test_case_2():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '{"jsonrpc": "2.0", "method": "hello", "params": [42, 23], "id": 1}'
    var_0 = json_rpc_server_0.handle_request(str_0)

def test_case_3():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    var_0 = setattr(json_rpc_server_0, str_0, str_0)
    var_1 = json_rpc_server_0.response(str_0)
    var_2 = json_rpc_server_0.invalid_params()

def test_case_4():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    var_0 = setattr(json_rpc_server_0, str_0, str_0)
    var_1 = json_rpc_server_0.response(str_0)

def test_case_5():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    var_0 = setattr(json_rpc_server_0, str_0, str_0)
    var_1 = json_rpc_server_0.response()