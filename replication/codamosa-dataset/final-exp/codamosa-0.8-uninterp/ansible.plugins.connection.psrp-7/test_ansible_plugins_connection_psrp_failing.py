# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    try:
        connection_0 = module_0.Connection()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'nhYT'
        list_0 = [str_0, str_0, str_0, str_0]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.put_file(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 3687
        list_0 = [int_0, int_0, int_0, int_0]
        connection_0 = module_0.Connection(*list_0)
        str_0 = 'B|Z.tSznA*Pe_`R\x0b'
        dict_0 = None
        var_0 = connection_0.exec_command(str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 1983.9635
        set_0 = {float_0}
        list_0 = [set_0, set_0, set_0]
        list_1 = [list_0, set_0, list_0]
        connection_0 = module_0.Connection(*list_1)
        complex_0 = None
        bool_0 = False
        var_0 = connection_0.fetch_file(complex_0, bool_0)
    except BaseException:
        pass