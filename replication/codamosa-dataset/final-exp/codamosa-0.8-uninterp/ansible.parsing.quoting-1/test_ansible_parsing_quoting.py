# Automatically generated by Pynguin.
import ansible.parsing.quoting as module_0

def test_case_0():
    str_0 = 'C6]'
    var_0 = module_0.is_quoted(str_0)

def test_case_1():
    bytes_0 = b'\xba-\xe6Y`\xd4K~\x05\xa0\xf3\xca\xd3\xb2\xdb'
    var_0 = module_0.unquote(bytes_0)

def test_case_2():
    float_0 = None
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.is_quoted(list_0)

def test_case_3():
    float_0 = None
    set_0 = {float_0, float_0, float_0}
    var_0 = module_0.is_quoted(set_0)

def test_case_4():
    str_0 = 'abc'
    var_0 = module_0.unquote(str_0)
    str_1 = '"abc"'
    var_1 = module_0.unquote(str_1)
    str_2 = "'abc'"
    var_2 = module_0.unquote(str_2)
    str_3 = '"a\\"bc"'
    var_3 = module_0.unquote(str_3)
    str_4 = "'a\\'bc'"
    var_4 = module_0.unquote(str_4)
    str_5 = '"a\tbc"'
    var_5 = module_0.unquote(str_5)
    str_6 = "'a\tbc'"
    var_6 = module_0.unquote(str_6)

def test_case_5():
    str_0 = "'s"
    var_0 = module_0.is_quoted(str_0)
    str_1 = "'s\\'"
    var_1 = module_0.is_quoted(str_1)