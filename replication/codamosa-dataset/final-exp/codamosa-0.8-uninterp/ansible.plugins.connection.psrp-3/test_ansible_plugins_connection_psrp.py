# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -2360
    list_0 = [int_0, int_0, int_0, int_0]
    connection_0 = module_0.Connection(*list_0)

def test_case_2():
    int_0 = 302
    list_0 = [int_0, int_0, int_0]
    connection_0 = module_0.Connection(*list_0)
    var_0 = connection_0.close()

def test_case_3():
    int_0 = -2360
    list_0 = [int_0, int_0, int_0, int_0]
    connection_0 = module_0.Connection(*list_0)
    var_0 = connection_0.reset()