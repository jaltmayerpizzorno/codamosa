# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'5@\xe3\xd0\xff\x10V'
    list_0 = [bytes_0, bytes_0, bytes_0]
    connection_0 = module_0.Connection(*list_0)

def test_case_2():
    bytes_0 = b'5@\xe3\xd0\xff\x10V'
    list_0 = [bytes_0, bytes_0, bytes_0]
    connection_0 = module_0.Connection(*list_0)
    var_0 = connection_0.reset()

def test_case_3():
    float_0 = 3079.0
    list_0 = [float_0, float_0, float_0]
    connection_0 = module_0.Connection(*list_0)
    var_0 = connection_0.close()