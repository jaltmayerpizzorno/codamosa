# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    json_rpc_server_0 = module_0.JsonRpcServer()

def test_case_1():
    json_rpc_server_0 = module_0.JsonRpcServer()
    str_0 = 'method'
    str_1 = 'params'
    str_2 = 'i.'
    var_0 = {str_1: str_0, str_0: str_1, str_1: str_2}
    var_1 = module_1.dumps(var_0)
    var_2 = json_rpc_server_0.handle_request(var_1)