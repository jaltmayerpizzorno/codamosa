# Automatically generated by Pynguin.
import ansible.plugins.connection.paramiko_ssh as module_0

def test_case_0():
    try:
        float_0 = 100.0
        bytes_0 = b'N\x8a\x88\xed\xbf4w\x8cx\xd1\x06\x04\x1a\xd3'
        str_0 = '0[XJgp'
        tuple_0 = (bytes_0,)
        connection_0 = module_0.Connection(tuple_0, str_0, str_0)
        var_0 = connection_0.reset()
        list_0 = []
        set_0 = {float_0, tuple_0, tuple_0}
        my_add_policy_0 = module_0.MyAddPolicy(set_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 6
        str_0 = 'ZR0>C5S"-5H;irw*$'
        list_0 = [str_0]
        connection_0 = module_0.Connection(int_0, str_0, *list_0)
        var_0 = connection_0.close()
    except BaseException:
        pass

def test_case_2():
    try:
        my_add_policy_0 = None
        bytes_0 = b'\xeeB\x0e\\\x15\xe8'
        bool_0 = True
        bytes_1 = b'\xe7;|\xac\xa6\x9c\xd2\xf0b\t\xdd\x80\x8b\x80\x14\xa5\x02w\xe8\xce'
        bytes_2 = b'n \x96{\x9a\x1fVH'
        list_0 = [bool_0, bool_0, bool_0, bytes_2]
        str_0 = '8Yp'
        str_1 = 'zCU'
        dict_0 = {str_0: bytes_1, str_0: bytes_2, str_1: bool_0}
        connection_0 = module_0.Connection(bool_0, bytes_1, list_0, **dict_0)
        var_0 = connection_0.exec_command(my_add_policy_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 100.0
        bytes_0 = b'N\x8a\x88\xed\xbf4w\x8cx\xd1\x06\x04\x1a\xd3'
        str_0 = '0[XJgp'
        tuple_0 = (bytes_0,)
        str_1 = "Zr\x0bGs+yfA9'v\n+Nqu"
        connection_0 = module_0.Connection(tuple_0, str_1, str_0)
        var_0 = connection_0.reset()
        list_0 = [var_0]
        var_1 = connection_0.fetch_file(list_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'N\x8a\x88\xed\xbf4w\x8cx\xd1\x06\x04\x1a\xd3'
        str_0 = '0[XJgp'
        tuple_0 = (bytes_0,)
        str_1 = "Zr\x0bGs+yfA9'v\n+Nqu"
        connection_0 = module_0.Connection(tuple_0, str_1, str_0)
        bool_0 = False
        bytes_1 = b'\x8b^YQ\xf4J\xcc\x9e\x88Z\xce\xf6m(\xdd0\x19'
        set_0 = {bytes_1, str_1}
        my_add_policy_0 = module_0.MyAddPolicy(set_0, connection_0)
        var_0 = connection_0.put_file(bool_0, my_add_policy_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'N\x8a\x88\xed\xbf4w\x8cx\xd1\x06\x04\x1a\xd3'
        str_0 = '0[XJgp'
        tuple_0 = (bytes_0,)
        str_1 = "Zr\x0bGs+yfA9'v\n+Nqu"
        connection_0 = module_0.Connection(tuple_0, str_1, str_0)
        float_0 = 1.5
        int_0 = -216
        display_0 = None
        bool_0 = False
        my_add_policy_0 = module_0.MyAddPolicy(bool_0, connection_0)
        var_0 = my_add_policy_0.missing_host_key(float_0, int_0, display_0)
    except BaseException:
        pass