# Automatically generated by Pynguin.
import ansible.module_utils.splitter as module_0

def test_case_0():
    str_0 = 'n-&k.\x0b1~O'
    var_0 = module_0.unquote(str_0)

def test_case_1():
    tuple_0 = ()
    var_0 = module_0.unquote(tuple_0)

def test_case_2():
    str_0 = '"hello"'
    var_0 = module_0.unquote(str_0)

def test_case_3():
    str_0 = '"hello"'
    var_0 = module_0.is_quoted(str_0)

def test_case_4():
    str_0 = "'bH\\B$"
    var_0 = module_0.unquote(str_0)

def test_case_5():
    str_0 = '"helo'
    var_0 = module_0.is_quoted(str_0)