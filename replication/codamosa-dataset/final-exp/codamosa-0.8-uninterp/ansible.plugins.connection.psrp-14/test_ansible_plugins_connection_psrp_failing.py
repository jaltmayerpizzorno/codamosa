# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    try:
        connection_0 = module_0.Connection()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 2678
        list_0 = [int_0, int_0, int_0, int_0]
        dict_0 = {}
        connection_0 = module_0.Connection(*list_0, **dict_0)
        var_0 = connection_0.exec_command(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 2678
        list_0 = [int_0, int_0, int_0, int_0]
        dict_0 = {}
        connection_0 = module_0.Connection(*list_0, **dict_0)
        var_0 = connection_0.reset()
        var_1 = connection_0.close()
        int_1 = -239
        list_1 = [int_0, var_1, var_1]
        var_2 = connection_0.put_file(int_1, list_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '%m3\x0cV&AKa5\x0bH\x0c>Yaq0h'
        int_0 = 214
        float_0 = 0.1
        list_0 = [float_0, float_0, float_0]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.fetch_file(str_0, int_0)
    except BaseException:
        pass