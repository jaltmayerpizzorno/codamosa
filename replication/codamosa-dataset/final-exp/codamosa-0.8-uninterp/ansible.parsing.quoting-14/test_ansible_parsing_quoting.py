# Automatically generated by Pynguin.
import ansible.parsing.quoting as module_0

def test_case_0():
    bytes_0 = b'\x89\xbc\xb0\xafZ\xd4\xee\xa9\x03\xf3,\xeb+\x83PA\x89'
    var_0 = module_0.is_quoted(bytes_0)

def test_case_1():
    list_0 = []
    var_0 = module_0.unquote(list_0)

def test_case_2():
    str_0 = 'u'
    var_0 = module_0.unquote(str_0)
    str_1 = " $/2'p#BPyK_?VW"
    var_1 = module_0.unquote(str_1)
    var_2 = module_0.is_quoted(str_1)

def test_case_3():
    str_0 = '"This is a double quoted string"'
    var_0 = module_0.unquote(str_0)
    str_1 = "'This is a single quoted string'"
    var_1 = module_0.unquote(str_1)
    str_2 = "'This is a string with 'single quotes' inside'"
    var_2 = module_0.unquote(str_2)
    str_3 = "'"
    var_3 = module_0.unquote(str_3)
    str_4 = 'This is an unquoted string'
    var_4 = module_0.unquote(str_4)

def test_case_4():
    str_0 = '"foo"'
    var_0 = module_0.is_quoted(str_0)
    str_1 = '"foo'
    var_1 = module_0.is_quoted(str_1)
    str_2 = '"foo""'
    var_2 = module_0.is_quoted(str_0)
    var_3 = module_0.is_quoted(str_2)