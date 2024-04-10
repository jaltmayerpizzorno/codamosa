# Automatically generated by Pynguin.
import ansible.utils.jsonrpc as module_0

def test_case_0():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"jsonrpc": "2.0", "method": "echo", "id": 1}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '9IF*^X\nJ$5|-rX:&KC^Y'
        var_0 = json_rpc_server_0.register(str_0)
        str_1 = ''
        var_1 = json_rpc_server_0.register(str_1)
        list_0 = [json_rpc_server_0, json_rpc_server_0, json_rpc_server_0]
        json_rpc_server_1 = module_0.JsonRpcServer(*list_0)
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
        var_0 = json_rpc_server_0.internal_error()
    except BaseException:
        pass

def test_case_4():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"id": "None", "jsonrpc": "2.0", "params": [[1,2,3], {"quux": "quux"}], "method": "test_method"}'
        var_0 = json_rpc_server_0.handle_request(str_0)
        var_1 = json_rpc_server_0.parse_error()
    except BaseException:
        pass

def test_case_5():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"method":"_get_timestamp","params":[],"id":3}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        var_0 = json_rpc_server_0.invalid_params()
    except BaseException:
        pass

def test_case_7():
    try:
        json_rpc_server_0 = module_0.JsonRpcServer()
        str_0 = '{"jsonrpc": "2.0", "id": "123", "method": "rpc.locked_config", "params": [1, 2, 3]}'
        var_0 = json_rpc_server_0.handle_request(str_0)
    except BaseException:
        pass