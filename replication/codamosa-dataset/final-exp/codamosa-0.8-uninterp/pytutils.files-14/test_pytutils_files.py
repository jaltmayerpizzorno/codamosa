# Automatically generated by Pynguin.
import pytutils.files as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Test file contents'
    var_0 = module_0.burp(str_0, str_0)

def test_case_2():
    str_0 = '/dev/null'
    var_0 = module_0.islurp(str_0)
    var_1 = next(var_0, str_0)