# Automatically generated by Pynguin.
import ansible.parsing.quoting as module_0

def test_case_0():
    bytes_0 = b'\x1c'
    var_0 = module_0.unquote(bytes_0)

def test_case_1():
    float_0 = 179.7655464685886
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.unquote(list_0)

def test_case_2():
    str_0 = '"hello"'
    var_0 = module_0.unquote(str_0)

def test_case_3():
    bytes_0 = b'\xef\x8cB\xa6\xe4\xa4\xc5\xb9\x9b\xba\x11\xf6Z\xa3&\xd3Gm'
    var_0 = module_0.unquote(bytes_0)