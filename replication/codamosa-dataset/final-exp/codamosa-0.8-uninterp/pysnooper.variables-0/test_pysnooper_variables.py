# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = None
    var_0 = module_0.needs_parentheses(int_0)

def test_case_2():
    str_0 = 'path'
    indices_0 = module_0.Indices(str_0)

def test_case_3():
    str_0 = '__load^ker__'
    exploding_0 = module_0.Exploding(str_0)
    var_0 = exploding_0.items(str_0)

def test_case_4():
    str_0 = '{}.x'
    attrs_0 = module_0.Attrs(str_0)
    set_0 = {attrs_0}
    var_0 = attrs_0.__eq__(set_0)
    bool_0 = True
    var_1 = attrs_0.__eq__(bool_0)

def test_case_5():
    str_0 = 'a'
    exploding_0 = module_0.Exploding(str_0)
    var_0 = exploding_0.items(str_0)

def test_case_6():
    str_0 = 'a'
    str_1 = 'foo'
    str_2 = (str_1,)
    indices_0 = module_0.Indices(str_0, str_2)
    int_0 = 5
    int_1 = 10
    var_0 = indices_0[int_0:int_1]
    var_1 = slice(int_0, int_1)

def test_case_7():
    str_0 = '{}.x'
    attrs_0 = module_0.Attrs(str_0)
    bool_0 = True
    var_0 = attrs_0.__eq__(bool_0)
    bool_1 = None
    var_1 = attrs_0.items(bool_1)