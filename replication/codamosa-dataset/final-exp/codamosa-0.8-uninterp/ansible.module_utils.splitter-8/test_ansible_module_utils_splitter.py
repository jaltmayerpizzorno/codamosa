# Automatically generated by Pynguin.
import ansible.module_utils.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'|m\xe2\xe3'
    var_0 = module_0.unquote(bytes_0)

def test_case_2():
    list_0 = []
    var_0 = module_0.unquote(list_0)

def test_case_3():
    str_0 = '"bar"'
    var_0 = module_0.unquote(str_0)
    str_1 = "'bar'"
    var_1 = module_0.unquote(str_1)
    str_2 = "'bar"
    var_2 = module_0.unquote(str_2)