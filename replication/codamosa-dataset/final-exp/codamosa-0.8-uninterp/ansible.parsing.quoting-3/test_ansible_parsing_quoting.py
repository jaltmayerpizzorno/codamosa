# Automatically generated by Pynguin.
import ansible.parsing.quoting as module_0

def test_case_0():
    str_0 = 'WIf@:@/ab.];3KJ36kS'
    var_0 = module_0.is_quoted(str_0)

def test_case_1():
    str_0 = 'b^u^}R='
    var_0 = module_0.unquote(str_0)

def test_case_2():
    str_0 = "'foo bar'"
    var_0 = module_0.is_quoted(str_0)
    str_1 = '"foo bar"'
    var_1 = module_0.is_quoted(str_1)
    list_0 = [var_0, var_0]
    var_2 = module_0.is_quoted(list_0)

def test_case_3():
    str_0 = '"foo"'
    var_0 = module_0.is_quoted(str_0)
    str_1 = '\'fo"o\''
    var_1 = module_0.is_quoted(str_1)

def test_case_4():
    str_0 = 'b^^}R='
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.unquote(dict_0)
    var_1 = module_0.unquote(str_0)

def test_case_5():
    str_0 = 'foo'
    var_0 = module_0.unquote(str_0)
    str_1 = "'foo'"
    var_1 = module_0.unquote(str_1)
    str_2 = '"fo\'o"'
    var_2 = module_0.unquote(str_2)
    str_3 = '\'"foo"\''
    var_3 = module_0.unquote(str_3)
    var_4 = module_0.unquote(str_3)