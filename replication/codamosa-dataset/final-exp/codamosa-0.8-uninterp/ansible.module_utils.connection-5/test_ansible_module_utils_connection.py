# Automatically generated by Pynguin.
import ansible.module_utils.connection as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    connection_error_0 = module_0.ConnectionError(bool_0)

def test_case_2():
    var_0 = ()
    str_0 = '_socket_path'
    str_1 = '/dev/null'
    str_2 = {str_0: str_1}
    var_1 = type(str_1, var_0, str_2)
    var_2 = module_0.exec_command(var_1, str_1)

def test_case_3():
    float_0 = 140.74
    connection_0 = module_0.Connection(float_0)

def test_case_4():
    var_0 = ()
    str_0 = '_socket_path'
    str_1 = {str_0: str_0}
    var_1 = type(str_0, var_0, str_1)
    var_2 = module_0.exec_command(var_1, str_0)