# Automatically generated by Pynguin.
import ansible.cli.scripts.ansible_connection_cli_stub as module_0
import _io as module_1
import ansible.playbook.play_context as module_2

def test_case_0():
    try:
        var_0 = module_0.main()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = './test_ConnectionProcess_shutdown'
        connection_process_0 = module_0.ConnectionProcess(str_0, str_0, str_0, str_0)
        var_0 = connection_process_0.shutdown()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        str_0 = 'prefix_count'
        bytes_0 = b'3\xf9Y\xdb" 0\x92\xf3\x08\x9e'
        connection_process_0 = module_0.ConnectionProcess(str_0, bool_0, str_0, bytes_0)
        list_0 = [bytes_0]
        var_0 = connection_process_0.start(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'tBl1z&'
        connection_process_0 = module_0.ConnectionProcess(str_0, str_0, str_0, str_0)
        var_0 = connection_process_0.run()
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = None
        float_0 = -2631.686436
        str_0 = 'OZ4?Bd}5-FYP-{'
        str_1 = '5A?Co'
        set_0 = {str_1}
        dict_0 = {}
        connection_process_0 = module_0.ConnectionProcess(float_0, str_0, str_1, set_0, dict_0)
        list_1 = [connection_process_0]
        float_1 = 1.0
        tuple_0 = (float_1,)
        tuple_1 = (tuple_0,)
        int_0 = 1908
        connection_process_1 = module_0.ConnectionProcess(list_1, tuple_1, set_0, tuple_1, tuple_0, int_0)
        var_0 = connection_process_1.connect_timeout(list_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '__main__'
        bytes_0 = b'\x84\xb8\x1d-\xb6\xb3\x03X\x14\xf3'
        set_0 = set()
        str_1 = '6=eKF\trCe\rDid'
        list_0 = [str_1, str_1]
        str_2 = ';.#jGx(hGZ@\\\ndn \ns'
        bytes_1 = b'\xe6\xcb\xf6rd]\x80\xcf\xfe\xf4\xd3\x019'
        connection_process_0 = module_0.ConnectionProcess(set_0, str_1, list_0, str_2, bytes_1)
        var_0 = connection_process_0.command_timeout(str_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        complex_0 = None
        str_0 = 'ansible.cli.scripts.ansible_connection_cli_stub'
        bool_0 = True
        float_0 = 1122.0
        list_0 = [bool_0, bool_0]
        str_1 = "k'Q)"
        tuple_0 = (bool_0,)
        connection_process_0 = module_0.ConnectionProcess(list_0, str_1, tuple_0, list_0)
        bytes_0 = b'\xe3m$\xe1\x94/'
        connection_process_1 = module_0.ConnectionProcess(bool_0, float_0, connection_process_0, bytes_0)
        var_0 = connection_process_1.handler(complex_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = None
        string_i_o_0 = module_1.StringIO()
        dict_0 = {string_i_o_0: string_i_o_0}
        bytes_0 = b'G1\xa4\xb3Z\x83\xd0\xa5\xa2\x9f\xdb\xbe\xd7\x8e,'
        int_0 = -2575
        connection_process_0 = module_0.ConnectionProcess(string_i_o_0, dict_0, bytes_0, str_0, int_0)
        var_0 = connection_process_0.start(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\xe7\\\xa0\x1a\x8c\xb0\x1d\xd8\x8dA\xdf\\u/l\x03'
        list_0 = [bytes_0, bytes_0]
        float_0 = -700.8756
        play_context_0 = module_2.PlayContext()
        tuple_0 = None
        dict_0 = {tuple_0: play_context_0, float_0: bytes_0, float_0: float_0}
        connection_process_0 = module_0.ConnectionProcess(float_0, play_context_0, bytes_0, dict_0)
        var_0 = connection_process_0.start(list_0)
    except BaseException:
        pass