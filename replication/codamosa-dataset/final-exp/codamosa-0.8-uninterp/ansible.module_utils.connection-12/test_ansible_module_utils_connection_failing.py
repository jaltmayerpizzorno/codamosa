# Automatically generated by Pynguin.
import ansible.module_utils.connection as module_0

def test_case_0():
    try:
        connection_0 = None
        list_0 = [connection_0]
        list_1 = [list_0, list_0, connection_0]
        connection_error_0 = module_0.ConnectionError(list_0, *list_1)
        set_0 = {connection_0, connection_0, connection_error_0}
        bytes_0 = None
        var_0 = module_0.write_to_file_descriptor(set_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'AB1e6[4WJ&Y4h'
        bool_0 = False
        list_0 = [str_0, bool_0]
        connection_error_0 = module_0.ConnectionError(list_0)
        var_0 = module_0.write_to_file_descriptor(bool_0, connection_error_0)
        connection_0 = module_0.Connection(str_0)
        float_0 = -1609.583542
        connection_1 = module_0.Connection(float_0)
        var_1 = module_0.recv_data(connection_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 3870.09067
        str_0 = '-C&4<o^1\r'
        var_0 = module_0.send_data(float_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = None
        var_1 = module_0.recv_data(var_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 0.0
        str_0 = '+@lOi5(F1TXt6yTYcr\\C'
        var_0 = module_0.exec_command(float_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'test/data/socket'
        connection_0 = module_0.Connection(str_0)
        var_0 = connection_0.__rpc__(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        str_0 = 'g_Q&`)ti\tXBsl'
        dict_0 = {str_0: bool_0, str_0: str_0}
        connection_error_0 = module_0.ConnectionError(bool_0, **dict_0)
        int_0 = 38
        connection_0 = module_0.Connection(int_0)
        var_0 = module_0.recv_data(connection_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = None
        connection_0 = module_0.Connection(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Test'
        connection_0 = module_0.Connection(str_0)
        var_0 = module_0.recv_data(connection_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 5
        connection_0 = module_0.Connection(int_0)
        var_0 = connection_0.__rpc__(connection_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        connection_0 = module_0.Connection(bool_0)
        var_0 = module_0.recv_data(connection_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'prLm\\U<=g*qazZS'
        connection_0 = module_0.Connection(str_0)
        connection_1 = module_0.Connection(connection_0)
        bytes_0 = b'\xd1\xf6\x8d_Ij\xa7\x11r\xae\xb2\x98u\x11\xdc'
        connection_2 = module_0.Connection(bytes_0)
        var_0 = connection_2.send(connection_1)
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = 4466.0
        list_0 = [float_0, float_0]
        list_1 = [list_0, list_0, float_0]
        bytes_0 = b'\xc1\xea'
        connection_0 = module_0.Connection(bytes_0)
        var_0 = connection_0.__getattr__(list_1)
    except BaseException:
        pass