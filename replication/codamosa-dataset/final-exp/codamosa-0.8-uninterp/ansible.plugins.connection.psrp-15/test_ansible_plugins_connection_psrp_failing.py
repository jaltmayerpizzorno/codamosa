# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    try:
        connection_0 = module_0.Connection()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1948.5401241319453
        list_0 = [float_0, float_0, float_0, float_0]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.exec_command(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 1947.643463
        list_0 = [float_0, float_0, float_0, float_0]
        connection_0 = module_0.Connection(*list_0)
        int_0 = -134
        set_0 = {int_0, connection_0, int_0}
        var_0 = connection_0.fetch_file(int_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '%'
        list_0 = [str_0, str_0, str_0, str_0]
        dict_0 = {}
        connection_0 = module_0.Connection(*list_0, **dict_0)
        str_1 = '\x0bI\x0bCZXQhATK4z`7*Z*6'
        var_0 = connection_0.put_file(str_1, connection_0)
    except BaseException:
        pass