# Automatically generated by Pynguin.
import ansible.cli.scripts.ansible_connection_cli_stub as module_0
import ansible.utils.display as module_1
import ansible.playbook.play_context as module_2
import _io as module_3
import ansible.module_utils.connection as module_4

def test_case_0():
    try:
        var_0 = module_0.main()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '/tmp/test_socket'
        connection_process_0 = module_0.ConnectionProcess(str_0, str_0, str_0, str_0)
        var_0 = connection_process_0.shutdown()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'/l\x95\xf9\x18)\xc9C0'
        bytes_1 = b'\xb0\xb0\x00\x14\xdc5\x7f;U\xce_\xd75'
        set_0 = {bytes_1}
        display_0 = module_1.Display()
        float_0 = 32.26978
        connection_process_0 = module_0.ConnectionProcess(bytes_1, set_0, bytes_1, display_0, float_0)
        var_0 = connection_process_0.start(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/tmp/test_socket_lock'
        connection_process_0 = module_0.ConnectionProcess(str_0, str_0, str_0, str_0)
        var_0 = connection_process_0.run()
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 100.0
        float_1 = 4496.0
        str_0 = 'ansible.cli.scripts.ansible_connection_cli_stub'
        str_1 = None
        dict_0 = {str_0: str_1, str_0: float_1, float_0: str_1, str_0: float_0}
        bytes_0 = b'l\x7f\xeb\xbay\xb4\xf8\x0c3\x14\xbfe\x17\x93\xf9\x8d\xeb\x04\x0b\x18'
        list_0 = [dict_0]
        bool_0 = True
        tuple_0 = (list_0, bool_0)
        tuple_1 = (tuple_0, dict_0, tuple_0)
        int_0 = -1659
        bool_1 = False
        str_2 = 't\\!AZA+{T'
        float_2 = -1648.36
        list_1 = [bytes_0, str_2, float_2]
        float_3 = -2947.15
        str_3 = '\n    This function will check if the service name supplied\n    is enabled in any of the sysv runlevels\n\n    :arg name: name of the service to test for\n    :kw runlevel: runlevel to check (default: None)\n    '
        connection_process_0 = module_0.ConnectionProcess(dict_0, list_1, float_3, str_3)
        str_4 = '__main__'
        connection_process_1 = module_0.ConnectionProcess(bool_1, str_2, connection_process_0, connection_process_0, str_4)
        var_0 = connection_process_1.connect_timeout(tuple_1, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x0fyX\x14\xe0'
        int_0 = -1014
        str_0 = 'u\x0b(ZTUb5iS%ljF>'
        bytes_1 = b'7vJ\xe1*N\xcf\xf0'
        float_0 = 2395.1
        bytes_2 = b'\xdc&!\x95V6=\xe5\xcb\x16\x15#\x83\xbe6'
        connection_process_0 = module_0.ConnectionProcess(str_0, str_0, bytes_1, float_0, bytes_2)
        var_0 = connection_process_0.handler(bytes_0, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = None
        tuple_0 = (int_0,)
        str_0 = '2dI=)wR6CDQ#2'
        int_1 = -1828
        dict_0 = {tuple_0: int_0, int_0: int_0, int_0: int_0}
        str_1 = '4@v-5\\c\\\n7$[^~'
        connection_process_0 = module_0.ConnectionProcess(int_1, dict_0, str_1, int_1)
        var_0 = connection_process_0.command_timeout(tuple_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '/tmp/test_socket_lock'
        connection_process_0 = module_0.ConnectionProcess(str_0, str_0, str_0, str_0)
        var_0 = connection_process_0.run()
    except BaseException:
        pass

def test_case_8():
    try:
        play_context_0 = module_2.PlayContext()
        str_0 = '/home/user'
        str_1 = '1234-5678'
        int_0 = 10006
        string_i_o_0 = module_3.StringIO()
        connection_process_0 = module_0.ConnectionProcess(string_i_o_0, play_context_0, str_1, str_0, str_1, int_0)
        var_0 = connection_process_0.start(str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = []
        int_0 = -590
        connection_0 = module_4.Connection(int_0)
        bytes_0 = b'+\xa8\xba~5\xb6\xba\xb7\x06\x06\xfb'
        str_0 = ''
        connection_process_0 = module_0.ConnectionProcess(int_0, connection_0, bytes_0, str_0)
        var_0 = connection_process_0.start(list_0)
    except BaseException:
        pass