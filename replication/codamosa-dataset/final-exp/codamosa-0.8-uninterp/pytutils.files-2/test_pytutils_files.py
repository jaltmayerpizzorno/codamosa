# Automatically generated by Pynguin.
import pytutils.files as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '-'
    list_0 = [str_0, str_0]
    var_0 = module_0.burp(str_0, str_0, list_0)

def test_case_2():
    str_0 = '/dev/null'
    var_0 = module_0.islurp(str_0)
    var_1 = list(var_0)

def test_case_3():
    str_0 = 'rPi}\\L\\rD6\x0c`b0.a'
    var_0 = module_0.burp(str_0, str_0)
    str_1 = ']1r#M&\\X9;JWOhx(]@'
    var_1 = module_0.islurp(str_1)
    var_2 = list(var_1)
    var_3 = module_0.islurp(str_0)
    var_4 = list(var_3)