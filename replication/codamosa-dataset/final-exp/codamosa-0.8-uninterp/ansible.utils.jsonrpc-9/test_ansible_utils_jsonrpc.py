# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    pass

def test_case_1():
    json_rpc_server_0 = module_0.JsonRpcServer()
    bytes_0 = b'{ "jsonrpc": "2.0", "method": "echo", "params": [1,"2"], "id": "1"}'
    var_0 = json_rpc_server_0.handle_request(bytes_0)

def test_case_2():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    var_0 = setattr(json_rpc_server_0, str_0, str_0)
    var_1 = json_rpc_server_0.response()

def test_case_3():
    str_0 = 'error'
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_1 = 'method'
    str_2 = 'params'
    var_0 = [str_1, str_1]
    var_1 = {str_1: str_0, str_2: var_0}
    var_2 = module_1.dumps(var_1)
    var_3 = json_rpc_server_0.handle_request(var_2)

def test_case_4():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = '_identifier'
    var_0 = setattr(json_rpc_server_0, str_0, str_0)
    str_1 = 'Hello world'
    var_1 = json_rpc_server_0.response(str_1)