# Automatically generated by Pynguin.
import ansible.cli.scripts.ansible_connection_cli_stub as module_0
import _io as module_1
import ansible.playbook.play_context as module_2
import ansible.utils.display as module_3
import ansible.module_utils.connection as module_4

def test_case_0():
    try:
        var_0 = module_0.main()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\te;mL)'
        dict_0 = {str_0: str_0, str_0: str_0}
        connection_process_0 = module_0.ConnectionProcess(str_0, dict_0, str_0, dict_0)
        var_0 = connection_process_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'3kuJ\x8a\x8b\xb9\x86g\xca\x08~\xe9L\x94\x83\xb3\xad'
        bool_0 = False
        set_0 = {bool_0, bytes_0}
        connection_process_0 = module_0.ConnectionProcess(bytes_0, bool_0, bytes_0, set_0)
        bytes_1 = b'\x7f\xc3\x80;(\xfaW\x82\x82N\x7f\xc8k\x16D\xbd\xfe\xf4\xbe'
        var_0 = connection_process_0.start(bytes_1)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 3404.51738
        float_1 = None
        list_0 = [float_0, float_0, float_1]
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        bytes_0 = b'\x03T\xbcVD\x94\xe1\x99Q\x18'
        connection_process_0 = module_0.ConnectionProcess(bool_0, bool_0, set_0, bytes_0)
        var_0 = connection_process_0.connect_timeout(float_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        int_0 = 173
        tuple_0 = (int_0,)
        float_0 = 0.0001
        str_0 = 'hl.-GQvN.'
        bool_0 = False
        tuple_1 = (float_0, str_0, bool_0)
        float_1 = -2704.7
        bytes_0 = b'w9{1'
        connection_process_0 = module_0.ConnectionProcess(tuple_1, tuple_1, float_1, bytes_0, float_0)
        var_0 = connection_process_0.command_timeout(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        list_0 = None
        float_0 = 3194.175
        bytes_0 = b''
        str_0 = 'pcj\x0b?'
        set_0 = {str_0}
        tuple_0 = None
        str_1 = ' gets plugin sources from play for groups '
        str_2 = ')e9f0\nE'
        tuple_1 = (set_0, tuple_0, str_1, str_2)
        str_3 = '\r'
        connection_process_0 = module_0.ConnectionProcess(float_0, bytes_0, tuple_1, str_3)
        int_0 = 520
        bool_1 = True
        connection_process_1 = module_0.ConnectionProcess(connection_process_0, int_0, connection_process_0, bool_1)
        var_0 = connection_process_1.handler(bool_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        string_i_o_0 = module_1.StringIO()
        play_context_0 = module_2.PlayContext()
        str_0 = 'tests/test_files/ansible-pc_local_socket'
        str_1 = 'tests/test_files'
        var_0 = None
        connection_process_0 = module_0.ConnectionProcess(string_i_o_0, play_context_0, str_0, str_1, var_0)
        var_1 = {}
        var_2 = connection_process_0.start(var_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'3kuJ\x8a\x8b\xb9\x86g\xca\x08~\xe9L\x94E\xb3\xad\x91'
        bool_0 = False
        set_0 = {bool_0, bytes_0, bool_0}
        display_0 = module_3.Display()
        int_0 = 618
        str_0 = '>pB'
        connection_0 = module_4.Connection(str_0)
        connection_process_0 = module_0.ConnectionProcess(int_0, connection_0, set_0, connection_0)
        var_0 = connection_process_0.start(display_0)
    except BaseException:
        pass