# Automatically generated by Pynguin.
import ansible.cli.scripts.ansible_connection_cli_stub as module_0
import ansible.playbook.play_context as module_1
import _io as module_2
import ansible.module_utils.connection as module_3

def test_case_0():
    try:
        var_0 = module_0.main()
    except BaseException:
        pass

def test_case_1():
    try:
        play_context_0 = module_1.PlayContext()
        str_0 = '/dev/nu"ll'
        connection_process_0 = module_0.ConnectionProcess(play_context_0, play_context_0, str_0, str_0)
        var_0 = connection_process_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        dict_0 = {}
        bytes_0 = b'*'
        connection_process_0 = module_0.ConnectionProcess(bool_0, dict_0, bytes_0, bytes_0, bool_0)
        list_0 = []
        var_0 = connection_process_0.start(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'X#d=C&?X'
        bytes_0 = b'\x13N\xfd'
        int_0 = -2063
        set_0 = {str_0, str_0}
        tuple_0 = ()
        str_1 = 'H0~\nLW%'
        dict_0 = {bytes_0: str_1}
        connection_process_0 = module_0.ConnectionProcess(set_0, set_0, tuple_0, str_1, dict_0)
        var_0 = connection_process_0.command_timeout(int_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '<J6b:xim'
        dict_0 = {str_0: str_0}
        bytes_0 = b'\xf6Y>8\x90'
        list_0 = [bytes_0]
        bool_0 = True
        str_1 = "m='y*!ro_"
        set_0 = set()
        dict_1 = {str_1: set_0}
        tuple_0 = (str_1, bool_0, set_0, dict_1)
        bool_1 = True
        connection_process_0 = module_0.ConnectionProcess(bytes_0, list_0, bool_0, tuple_0, bool_1)
        var_0 = connection_process_0.handler(str_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 1
        str_0 = "d.'mv]"
        list_0 = []
        set_0 = {int_0}
        float_0 = 0.0001
        bytes_0 = b'6\xa0t\xef\x908'
        set_1 = {bytes_0}
        connection_process_0 = module_0.ConnectionProcess(set_0, float_0, list_0, set_1)
        float_1 = -769.742125
        connection_process_1 = module_0.ConnectionProcess(int_0, str_0, list_0, connection_process_0, float_1)
        str_1 = '~XdG'
        bool_0 = False
        set_2 = {bool_0}
        bool_1 = False
        str_2 = 'A'
        int_1 = None
        list_1 = []
        dict_0 = {}
        connection_process_2 = module_0.ConnectionProcess(set_2, int_1, dict_0, list_1, str_2)
        float_2 = -1901.58
        connection_process_3 = module_0.ConnectionProcess(int_1, list_1, list_1, int_1, connection_process_2, float_2)
        connection_process_4 = module_0.ConnectionProcess(bool_0, bool_1, str_2, connection_process_3)
        str_3 = ',f'
        str_4 = '\n        Returns the role name (either the role: or name: field) from\n        the role definition, or (when the role definition is a simple\n        string), just that string\n        '
        float_3 = 1881.2894
        float_4 = 1563.58
        tuple_0 = (float_3, float_4, set_2)
        bool_2 = True
        bytes_1 = b'\xa3\x0b\x10\xc2\x92ei\x10'
        tuple_1 = (tuple_0, bool_2, set_2, bytes_1)
        dict_1 = {bool_0: tuple_0, str_1: str_1, float_4: str_1}
        connection_process_5 = module_0.ConnectionProcess(str_4, tuple_1, set_2, dict_1)
        var_0 = connection_process_5.connect_timeout(connection_process_4, str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        string_i_o_0 = module_2.StringIO()
        play_context_0 = module_1.PlayContext()
        str_0 = '/dev/null'
        connection_process_0 = module_0.ConnectionProcess(string_i_o_0, play_context_0, str_0, str_0)
        str_1 = 'YkIV,.RVEtyxR-'
        var_0 = connection_process_0.start(str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        string_i_o_0 = module_2.StringIO()
        play_context_0 = module_1.PlayContext()
        str_0 = '/dev/null'
        connection_process_0 = module_0.ConnectionProcess(string_i_o_0, play_context_0, str_0, str_0)
        var_0 = connection_process_0.shutdown()
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0}
        string_i_o_0 = module_2.StringIO()
        float_0 = 2612.04
        connection_0 = module_3.Connection(float_0)
        int_0 = 299
        str_0 = 'xd,Q\rw{^yBp >w~f'
        connection_process_0 = module_0.ConnectionProcess(string_i_o_0, connection_0, int_0, float_0, str_0)
        var_0 = connection_process_0.start(dict_0)
    except BaseException:
        pass