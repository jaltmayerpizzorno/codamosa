# Automatically generated by Pynguin.
import ansible.module_utils.connection as module_0

def test_case_0():
    try:
        str_0 = '_QHnR'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0]
        var_0 = module_0.write_to_file_descriptor(dict_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        connection_0 = module_0.Connection(bool_0)
        list_0 = [bool_0, bool_0, connection_0, bool_0]
        connection_error_0 = module_0.ConnectionError(list_0)
        dict_0 = {}
        str_0 = "Z~'YNqb<2Qfs"
        var_0 = module_0.write_to_file_descriptor(bool_0, str_0)
        var_1 = connection_0.__rpc__(connection_error_0, *list_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'X3AzA]E1 \x0bLL<0`DIr'
        float_0 = 457.0673
        connection_0 = module_0.Connection(float_0)
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: connection_0}
        var_0 = module_0.request_builder(dict_0)
        dict_1 = None
        float_1 = -3110.9
        var_1 = module_0.send_data(dict_1, float_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'k<v'
        list_0 = []
        var_0 = module_0.send_data(str_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'hT$Ki\t{I*t$'
        var_0 = module_0.recv_data(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = None
        set_0 = None
        var_0 = module_0.exec_command(list_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '5'
        connection_0 = module_0.Connection(str_0)
        var_0 = connection_0.__getattr__(connection_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = "ji'6d"
        str_1 = 'got IOError/EOFError in task loop: %s'
        str_2 = 'Eb'
        bool_0 = None
        dict_0 = {str_0: str_1, str_1: str_0, str_1: str_0, str_2: bool_0}
        connection_error_0 = module_0.ConnectionError(str_1, **dict_0)
        var_0 = module_0.recv_data(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        connection_error_0 = None
        connection_0 = module_0.Connection(connection_error_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0]
        connection_0 = module_0.Connection(bool_0)
        var_0 = connection_0.__rpc__(bool_0, *list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        connection_0 = module_0.Connection(bool_0)
        var_0 = connection_0.__rpc__(connection_0)
    except BaseException:
        pass

def test_case_11():
    try:
        list_0 = []
        tuple_0 = ()
        connection_0 = module_0.Connection(tuple_0)
        var_0 = connection_0.send(list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'\x9c\x1ebe\x9e\x03\x82rh{\xd72k='
        str_0 = '`o8miu)/\r\rzW'
        connection_0 = module_0.Connection(str_0)
        var_0 = connection_0.send(bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = False
        set_0 = set()
        connection_error_0 = module_0.ConnectionError(set_0)
        connection_0 = module_0.Connection(connection_error_0)
        connection_1 = module_0.Connection(connection_0)
        connection_2 = module_0.Connection(bool_0)
        var_0 = connection_1.__getattr__(set_0)
    except BaseException:
        pass