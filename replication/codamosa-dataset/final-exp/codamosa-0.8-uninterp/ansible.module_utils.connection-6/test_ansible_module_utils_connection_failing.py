# Automatically generated by Pynguin.
import ansible.module_utils.connection as module_0
import socket as module_1

def test_case_0():
    try:
        int_0 = -3301
        var_0 = module_0.write_to_file_descriptor(int_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xf0\xd2\x12O\xc7t>\xb6\xe5'
        str_0 = ' MbS]hg'
        var_0 = module_0.send_data(bytes_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 1888.0467
        var_0 = module_0.recv_data(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 4018.39
        str_0 = 'Mx\rKmx }F'
        var_0 = module_0.exec_command(float_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = set()
        list_0 = [set_0, set_0, set_0]
        tuple_0 = (set_0, list_0)
        connection_0 = module_0.Connection(tuple_0)
        bytes_0 = b'*\xb6\r\xfe\xc1\x8b\xde'
        connection_1 = module_0.Connection(bytes_0)
        var_0 = connection_1.send(connection_0)
    except BaseException:
        pass

def test_case_5():
    try:
        connection_error_0 = None
        connection_0 = module_0.Connection(connection_error_0)
    except BaseException:
        pass

def test_case_6():
    try:
        connection_error_0 = None
        bytes_0 = b'M\xc9\xebPY)t\x05\x10o\x96\xeb\xde6z\x9b\x8fx'
        connection_0 = module_0.Connection(bytes_0)
        var_0 = connection_0.__getattr__(connection_error_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        connection_0 = module_0.Connection(bool_0)
        set_0 = {bool_0}
        connection_error_0 = module_0.ConnectionError(set_0)
        list_0 = [connection_0]
        list_1 = [list_0, connection_0, list_0]
        dict_0 = {}
        var_0 = connection_0.__rpc__(list_1, **dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        socket_0 = module_1.socket()
        connection_0 = module_0.Connection(socket_0)
        connection_1 = module_0.Connection(connection_0)
        var_0 = module_0.recv_data(connection_1)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\xd2\xf4<\xe3\xf1\xffLd\x08\xe87\nt'
        connection_0 = module_0.Connection(bytes_0)
        var_0 = connection_0.__rpc__(connection_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0]
        set_0 = set()
        connection_0 = module_0.Connection(set_0)
        var_0 = connection_0.send(list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '1C^k@f[sP]kK{]"F'
        float_0 = 0.5
        bool_0 = True
        connection_error_0 = module_0.ConnectionError(bool_0)
        connection_0 = module_0.Connection(float_0)
        var_0 = module_0.request_builder(str_0)
        list_0 = [str_0]
        var_1 = connection_0.__getattr__(list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'control socket path is %s'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        bool_0 = False
        connection_0 = module_0.Connection(bool_0)
        var_0 = connection_0.__rpc__(dict_0)
    except BaseException:
        pass