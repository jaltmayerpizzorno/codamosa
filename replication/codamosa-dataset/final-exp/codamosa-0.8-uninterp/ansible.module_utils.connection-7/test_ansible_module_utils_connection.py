# Automatically generated by Pynguin.
import ansible.module_utils.connection as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Q6M'
    connection_0 = module_0.Connection(str_0)

def test_case_2():
    bool_0 = False
    int_0 = -37
    var_0 = module_0.write_to_file_descriptor(bool_0, int_0)
    str_0 = ''
    dict_0 = {str_0: bool_0, str_0: str_0, str_0: var_0}
    connection_error_0 = module_0.ConnectionError(str_0, **dict_0)
    float_0 = -1685.0
    connection_0 = module_0.Connection(float_0)
    bytes_0 = b'\x1d\xc7\x98\xac\x08\xabt^\xd4\xee\x83W\xef\xff\x8cp\xc3'
    list_0 = []
    connection_error_1 = module_0.ConnectionError(bytes_0, *list_0)