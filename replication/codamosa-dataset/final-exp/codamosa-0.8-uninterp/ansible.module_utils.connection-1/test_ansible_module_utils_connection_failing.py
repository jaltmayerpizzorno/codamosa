# Automatically generated by Pynguin.
import ansible.module_utils.connection as module_0

def test_case_0():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        var_0 = module_0.write_to_file_descriptor(dict_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        bool_0 = True
        var_0 = module_0.write_to_file_descriptor(bool_0, dict_0)
        bool_1 = True
        connection_0 = module_0.Connection(bool_1)
        var_1 = module_0.recv_data(connection_0)
    except BaseException:
        pass

def test_case_2():
    try:
        connection_0 = None
        set_0 = {connection_0}
        str_0 = 'disable -st'
        var_0 = module_0.send_data(set_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        var_0 = module_0.recv_data(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        connection_0 = module_0.Connection(bool_0)
        var_0 = module_0.recv_data(connection_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'unit-test-path'
        connection_0 = module_0.Connection(str_0)
        var_0 = connection_0.__rpc__(connection_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 763.45356
        connection_0 = module_0.Connection(float_0)
        str_0 = '/etc/shadow'
        connection_1 = module_0.Connection(str_0)
        var_0 = module_0.recv_data(connection_1)
    except BaseException:
        pass

def test_case_7():
    try:
        connection_0 = None
        connection_1 = module_0.Connection(connection_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        connection_0 = module_0.Connection(bool_0)
        var_0 = connection_0.__rpc__(connection_0)
    except BaseException:
        pass

def test_case_9():
    try:
        set_0 = None
        bool_0 = False
        connection_0 = module_0.Connection(bool_0)
        connection_error_0 = None
        bytes_0 = b'\x88'
        dict_0 = {connection_error_0: set_0, bool_0: bytes_0, connection_0: connection_error_0}
        dict_1 = None
        tuple_0 = (bytes_0, dict_0, dict_1)
        var_0 = connection_0.__getattr__(tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'Module'
        var_0 = ()
        var_1 = dict(_socket_path=var_0)
        var_2 = type(str_0, var_0, var_1)
        str_1 = 'foo'
        var_3 = module_0.exec_command(var_2, str_1)
    except BaseException:
        pass