# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = 0.1
    list_0 = [float_0, float_0, float_0]
    connection_0 = module_0.Connection(*list_0)

def test_case_2():
    int_0 = 2678
    list_0 = [int_0, int_0, int_0, int_0]
    dict_0 = {}
    connection_0 = module_0.Connection(*list_0, **dict_0)
    var_0 = connection_0.close()

def test_case_3():
    float_0 = -2.2391871688796003
    list_0 = [float_0, float_0, float_0]
    connection_0 = module_0.Connection(*list_0)
    var_0 = connection_0.reset()