# Automatically generated by Pynguin.
import ansible.plugins.connection.paramiko_ssh as module_0

def test_case_0():
    try:
        str_0 = '\tT@PR&A*jAez(RcsK'
        dict_0 = {}
        my_add_policy_0 = module_0.MyAddPolicy(str_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'yeV\x0b'
        int_0 = 1106
        tuple_0 = (str_0, int_0)
        str_1 = ':4?3&XLzc\t6A l '
        dict_0 = {str_1: tuple_0, str_1: str_1}
        str_2 = ')R`'
        list_0 = [int_0, tuple_0, str_1, str_2]
        connection_0 = module_0.Connection(str_0, tuple_0, dict_0, *list_0, **dict_0)
        var_0 = connection_0.close()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xc8;\xf6QK?\xc6\xb8\xef\x93\xce'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        str_0 = '\r'
        str_1 = None
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
        float_0 = 1651.5
        list_0 = [dict_0, float_0]
        bytes_1 = b'\xc5\x00\xa6o\xf2\xd7\xd2T\xb9'
        connection_0 = module_0.Connection(list_0, bytes_1, *list_0)
        var_0 = connection_0.exec_command(bytes_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        str_0 = 'Za3+=UP.e8 v;#xMG[?'
        dict_0 = {str_0: list_0}
        bytes_0 = b'\x98\xd1'
        str_1 = ''
        int_0 = -657
        list_1 = [list_0]
        connection_0 = module_0.Connection(list_0, dict_0, int_0, *list_1, **dict_0)
        var_0 = connection_0.put_file(bytes_0, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        bytes_0 = b'\xbc+\xda'
        str_0 = '|r\\'
        str_1 = '5|N(e(jV'
        str_2 = '.?n>8-s>wQI2M]Frs3l5'
        str_3 = '@N4\tq%b}(AkY|'
        dict_0 = {str_1: tuple_0, str_2: str_2, str_3: str_2}
        set_0 = {str_3, str_3}
        list_0 = [str_1, set_0]
        connection_0 = module_0.Connection(tuple_0, dict_0, list_0)
        var_0 = connection_0.fetch_file(bytes_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x16\x9b\n\xffj\x01\xb1'
        str_0 = '01tJ"vQ,qI@v8\''
        str_1 = 'm(s6h|sTfL{'
        dict_0 = {str_0: bytes_0, str_0: bytes_0, str_1: bytes_0, str_1: bytes_0}
        int_0 = 816
        int_1 = 4532
        list_0 = []
        dict_1 = {bytes_0: list_0}
        list_1 = [list_0, dict_1, dict_1, dict_1]
        connection_0 = module_0.Connection(list_0, dict_1, list_1)
        my_add_policy_0 = module_0.MyAddPolicy(int_1, connection_0)
        var_0 = my_add_policy_0.missing_host_key(str_0, dict_0, int_0)
    except BaseException:
        pass