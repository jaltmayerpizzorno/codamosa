# Automatically generated by Pynguin.
import ansible.cli.scripts.ansible_connection_cli_stub as module_0
import ansible.playbook.play_context as module_1
import _io as module_2
import ansible.utils.display as module_3
import ansible.module_utils.connection as module_4
import ansible.utils.jsonrpc as module_5

def test_case_0():
    try:
        var_0 = module_0.main()
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = None
        connection_process_0 = module_0.ConnectionProcess(var_0, var_0, var_0, var_0, var_0, var_0)
        var_1 = connection_process_0.exception
        var_2 = connection_process_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        play_context_0 = module_1.PlayContext()
        str_0 = 'moc%_an#ibSe_playbook_id'
        connection_process_0 = module_0.ConnectionProcess(str_0, play_context_0, str_0, str_0, str_0, str_0)
        var_0 = connection_process_0.start(play_context_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -155
        int_1 = 1354
        dict_0 = {int_1: int_1, int_0: int_1, int_0: int_0}
        dict_1 = {int_0: int_0, int_1: int_1, int_1: int_1, int_1: dict_0}
        list_0 = [int_0, dict_1]
        float_0 = -811.338768
        set_0 = {float_0, float_0, float_0}
        dict_2 = {}
        bool_0 = False
        list_1 = [dict_2, bool_0]
        connection_process_0 = module_0.ConnectionProcess(float_0, set_0, dict_2, list_1)
        var_0 = connection_process_0.connect_timeout(dict_1, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = None
        int_0 = 1981
        int_1 = -997
        dict_1 = {}
        list_0 = []
        float_0 = None
        bytes_0 = b'v\x8c\xaa\xb0\xf1B\xe6\x1aZ\xa0tK\xf2\xc6\xb5'
        tuple_0 = (list_0, float_0, bytes_0)
        connection_process_0 = module_0.ConnectionProcess(int_1, dict_1, int_1, tuple_0)
        var_0 = connection_process_0.command_timeout(dict_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x0e\t"q'
        str_0 = '__main__'
        str_1 = '1CPuFv[$)}4\\t>x'
        tuple_0 = (bytes_0, str_0, str_1)
        dict_0 = {}
        int_0 = -503
        str_2 = 'R=fN/'
        bytes_1 = b'"ypgZ\x125'
        connection_process_0 = module_0.ConnectionProcess(tuple_0, int_0, str_2, bytes_1)
        list_0 = [connection_process_0]
        str_3 = '93sZ7Dn!hB-82A'
        connection_process_1 = module_0.ConnectionProcess(connection_process_0, list_0, connection_process_0, str_3, list_0)
        var_0 = connection_process_1.handler(dict_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        bool_0 = True
        bytes_0 = b'\xe4\\\x95m\x07ot!\x12'
        connection_process_0 = module_0.ConnectionProcess(list_0, bool_0, bytes_0, bytes_0)
        var_0 = connection_process_0.shutdown()
    except BaseException:
        pass

def test_case_7():
    try:
        string_i_o_0 = module_2.StringIO()
        play_context_0 = module_1.PlayContext()
        str_0 = 'moc%_an#ibSe_playbook_id'
        var_0 = string_i_o_0
        connection_process_0 = module_0.ConnectionProcess(var_0, play_context_0, str_0, str_0, str_0, str_0)
        var_1 = connection_process_0.start(play_context_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        display_0 = module_3.Display(bool_0)
        int_0 = -2680
        str_0 = 'o;;.W!'
        dict_0 = {str_0: str_0, str_0: str_0}
        connection_0 = module_4.Connection(dict_0)
        connection_1 = module_4.Connection(connection_0)
        json_rpc_server_0 = module_5.JsonRpcServer()
        bool_1 = False
        tuple_0 = (json_rpc_server_0, bool_1)
        list_0 = [connection_1, str_0]
        connection_process_0 = module_0.ConnectionProcess(tuple_0, connection_0, list_0, json_rpc_server_0)
        list_1 = []
        connection_process_1 = module_0.ConnectionProcess(connection_process_0, connection_0, str_0, list_1, bool_1)
        play_context_0 = module_1.PlayContext()
        display_1 = module_3.Display(play_context_0)
        connection_process_2 = module_0.ConnectionProcess(int_0, connection_1, connection_process_1, display_1)
        var_0 = connection_process_2.start(display_0)
    except BaseException:
        pass