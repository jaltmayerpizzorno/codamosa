# Automatically generated by Pynguin.
import ansible.module_utils.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    tuple_0 = ()
    var_0 = module_0.is_quoted(tuple_0)

def test_case_2():
    str_0 = 'LVs~hz'
    var_0 = module_0.unquote(str_0)

def test_case_3():
    str_0 = 'test'
    var_0 = module_0.is_quoted(str_0)
    var_1 = module_0.is_quoted(str_0)
    str_1 = '"test"'
    var_2 = module_0.is_quoted(str_1)

def test_case_4():
    str_0 = 'test'
    var_0 = module_0.is_quoted(str_0)
    str_1 = "'test'"
    var_1 = module_0.is_quoted(str_1)
    str_2 = '"test"'
    var_2 = module_0.is_quoted(str_2)