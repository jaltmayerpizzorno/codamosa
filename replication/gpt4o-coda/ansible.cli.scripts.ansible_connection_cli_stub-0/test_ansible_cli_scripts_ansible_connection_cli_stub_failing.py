# Automatically generated by Pynguin.
import ansible.cli.scripts.ansible_connection_cli_stub as module_0
import ansible.playbook.play_context as module_1
import _io as module_2

def test_case_0():
    try:
        var_0 = module_0.main()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2826
        dict_0 = {}
        str_0 = '|SV4s_I(zou}!\tg/]4'
        connection_process_0 = module_0.ConnectionProcess(int_0, dict_0, str_0, dict_0)
        var_0 = connection_process_0.shutdown()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '!>s.+q&.'
        float_0 = 848.2
        list_0 = [float_0]
        bytes_0 = b"\xed\x9d\xf1\xce@\x90\xfaw\xd5\x8b\xd5\x87\xb8\xe9'\xa8\x04=\n"
        connection_process_0 = module_0.ConnectionProcess(float_0, float_0, float_0, list_0, bytes_0)
        var_0 = connection_process_0.start(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        bytes_0 = b'\x96\x1csH\x9d\xca<9'
        float_0 = 1245.21
        connection_process_0 = module_0.ConnectionProcess(bool_0, bool_0, bytes_0, float_0)
        var_0 = connection_process_0.run()
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xec\xc3:\xad\xaaO\xbb\x9c\xa1+'
        tuple_0 = None
        str_0 = 'only run plays and tasks whose tags do not match these values'
        bool_0 = True
        dict_0 = {}
        str_1 = '__main__'
        int_0 = 788
        list_0 = None
        str_2 = 'ansible.cli.scripts.ansible_connection_cli_stub'
        float_0 = 1238.671
        int_1 = 448
        connection_process_0 = module_0.ConnectionProcess(dict_0, int_1, dict_0, list_0, float_0)
        connection_process_1 = module_0.ConnectionProcess(list_0, str_2, float_0, connection_process_0)
        connection_process_2 = module_0.ConnectionProcess(dict_0, dict_0, str_1, int_0, connection_process_1)
        connection_process_3 = module_0.ConnectionProcess(tuple_0, str_0, bool_0, connection_process_2)
        str_3 = '#)TUNj\tQ(O '
        str_4 = '\n:stderr: %s'
        set_0 = {str_3, str_3, str_4}
        list_1 = [set_0, set_0, str_3, str_3]
        int_2 = -970
        connection_process_4 = module_0.ConnectionProcess(set_0, list_1, set_0, list_1, int_2)
        var_0 = connection_process_4.connect_timeout(bytes_0, connection_process_3)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = None
        list_0 = []
        bytes_0 = b'\xde\x11\xd0w\x17I\xa3%4\xe3\xfa'
        float_1 = 4682.0
        bytes_1 = b'H\x03\xb8\x88)\x05\xc1\xe4^\x00'
        list_1 = [bytes_0, bytes_1, bytes_1, bytes_0]
        str_0 = "N'"
        connection_process_0 = module_0.ConnectionProcess(bytes_1, list_1, list_1, float_1, str_0)
        connection_process_1 = module_0.ConnectionProcess(bytes_0, float_1, connection_process_0, float_1)
        var_0 = connection_process_1.command_timeout(float_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = ()
        complex_0 = None
        float_0 = 0.1
        int_0 = -2514
        bool_0 = True
        int_1 = 3600
        connection_process_0 = module_0.ConnectionProcess(float_0, int_0, bool_0, int_1)
        str_0 = 'w\t'
        set_0 = set()
        connection_process_1 = module_0.ConnectionProcess(tuple_0, str_0, set_0, set_0)
        var_0 = connection_process_1.handler(complex_0, connection_process_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = None
        bytes_0 = b'\xda\xd2\xcf\x14\x9b-\xcd\x91B\xa5\x81=\x11\x0e\x04?'
        play_context_0 = module_1.PlayContext()
        int_0 = 0
        list_1 = [int_0, bytes_0]
        list_2 = [bytes_0]
        dict_0 = {}
        connection_process_0 = module_0.ConnectionProcess(bytes_0, play_context_0, list_1, list_2, dict_0)
        var_0 = connection_process_0.start(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = []
        string_i_o_0 = module_2.StringIO()
        float_0 = 0.0001
        str_0 = ">h'V/ce"
        play_context_0 = module_1.PlayContext()
        bool_0 = None
        list_1 = [string_i_o_0, str_0, play_context_0, bool_0]
        connection_process_0 = module_0.ConnectionProcess(string_i_o_0, float_0, str_0, list_1)
        var_0 = connection_process_0.start(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -112
        bool_0 = True
        str_0 = '.'
        set_0 = None
        dict_0 = {bool_0: int_0, str_0: bool_0, int_0: set_0, bool_0: bool_0}
        connection_process_0 = module_0.ConnectionProcess(bool_0, str_0, str_0, dict_0)
        var_0 = connection_process_0.run()
    except BaseException:
        pass