# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0
import json as module_1

def test_case_0():
    try:
        str_0 = 'XmG&$fIPs\rqC,)4cY;Z~'
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"jsonrpc": "2.0", "method": "foo", "id": 0, "params": []}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\x0c\nFU!5tfrb?yAFiG|@'
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.parse_error(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{\n"method": "add",\n"params": [1, 2],\n"id": 12345\n}'
        var_0 = json_rpc_server_0.handle_request(str_0)
        var_1 = json_rpc_server_0.response()
    except BaseException:
        pass

def test_case_4():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{\n"method": "add",\n"params": [1, 2],\n"id": 12345\n}'
        var_0 = json_rpc_server_0.handle_request(str_0)
        var_1 = json_rpc_server_0.invalid_request()
    except BaseException:
        pass

def test_case_5():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{\n"method": "add",\n"params": [1, 2],\n"id": 12345\n}'
        var_0 = json_rpc_server_0.handle_request(str_0)
        var_1 = json_rpc_server_0.invalid_params()
    except BaseException:
        pass

def test_case_6():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"jsonrpc": "2.0", "method": "rpc.run", "id": "1"}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = 'jsonrpc'
        str_1 = 'method'
        str_2 = 'params'
        str_3 = 'id'
        str_4 = '2.0'
        str_5 = '_rpc.exec'
        var_0 = []
        var_1 = {}
        var_2 = [var_0, var_1]
        int_0 = 1
        var_3 = {str_0: str_4, str_1: str_5, str_2: var_2, str_3: int_0}
        var_4 = module_1.dumps(var_3)
        var_5 = json_rpc_server_0.handle_request(var_4)
    except BaseException:
        pass