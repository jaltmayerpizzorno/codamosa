# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '^-|oll'
    list_0 = [str_0, str_0, str_0]
    connection_0 = module_0.Connection(*list_0)

def test_case_2():
    bytes_0 = b'\x18\x8b(`C\xcf\xa5\xa4\xaa\xedk\x03r\x90\x0c\x94'
    int_0 = 82
    list_0 = [bytes_0, bytes_0, int_0]
    connection_0 = module_0.Connection(*list_0)
    var_0 = connection_0.reset()

def test_case_3():
    str_0 = 'q1+s3'
    list_0 = [str_0, str_0, str_0]
    connection_0 = module_0.Connection(*list_0)
    var_0 = connection_0.close()