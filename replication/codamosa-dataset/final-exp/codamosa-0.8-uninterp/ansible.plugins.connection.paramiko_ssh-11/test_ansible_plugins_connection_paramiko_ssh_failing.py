# Automatically generated by Pynguin.
import ansible.plugins.connection.paramiko_ssh as module_0

def test_case_0():
    try:
        bytes_0 = b']\xf0\xde\xaeX\x146\xb6\x1c\x8d\x01Y\xf0\xee~\xed\x9c\x01p'
        str_0 = ' J7Gsqh "w5D'
        dict_0 = {str_0: bytes_0}
        list_0 = []
        connection_0 = module_0.Connection(bytes_0, str_0, dict_0, *list_0)
        my_add_policy_0 = module_0.MyAddPolicy(connection_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'C|t6>.[qAj1ar^\nM\nt{l'
        str_1 = '- changing dependent role %s from %s to %s'
        set_0 = set()
        list_0 = [set_0]
        bytes_0 = b'\xe4%\x14\xc6%pG(\x16Y'
        connection_0 = module_0.Connection(set_0, list_0, bytes_0)
        var_0 = connection_0.exec_command(str_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '#'
        list_0 = [str_0, str_0, str_0, str_0]
        list_1 = [str_0, str_0]
        tuple_0 = (list_0, list_1)
        str_1 = '! 7`2)i2+NmocRlDi3F2'
        dict_0 = {str_1: tuple_0, str_1: list_0}
        dict_1 = {}
        bytes_0 = b'Fl\x9b\xe1\xf3\x82\xe6\x9b\xef\x88V\xe8\x92'
        list_2 = [bytes_0, dict_1, dict_1]
        int_0 = -19
        connection_0 = module_0.Connection(dict_1, list_2, int_0)
        var_0 = connection_0.fetch_file(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n#c:4\x0c2j'
        bool_0 = True
        bytes_0 = b'o\xe8'
        list_0 = [str_0, str_0]
        list_1 = [str_0, list_0, str_0, str_0]
        connection_0 = module_0.Connection(str_0, bool_0, bytes_0, *list_1)
        var_0 = connection_0.close()
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -2196.5638
        bool_0 = True
        str_0 = '\x0cm~\\)T?%pV$2%md\x0b'
        list_0 = [str_0, str_0, float_0]
        connection_0 = module_0.Connection(bool_0, str_0, *list_0)
        var_0 = connection_0.reset()
        bytes_0 = None
        bytes_1 = b'==s[\x8a\x91\x82G\x10N\xcf'
        my_add_policy_0 = module_0.MyAddPolicy(bytes_1, connection_0)
        var_1 = my_add_policy_0.missing_host_key(bytes_0, list_0, my_add_policy_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -2196.5638
        bool_0 = True
        str_0 = '\x0cm~\\)T?%pV$2%md\x0b'
        list_0 = [str_0, str_0, float_0]
        connection_0 = module_0.Connection(bool_0, str_0, *list_0)
        var_0 = connection_0.reset()
        bytes_0 = b'==s[\x8a\x91\x82G\x10N\xcf'
        my_add_policy_0 = module_0.MyAddPolicy(bytes_0, connection_0)
        list_1 = [float_0]
        var_1 = connection_0.put_file(list_1, list_0)
    except BaseException:
        pass