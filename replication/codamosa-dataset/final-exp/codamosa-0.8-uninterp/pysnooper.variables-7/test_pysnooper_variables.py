# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '__main__'
    common_variable_0 = module_0.CommonVariable(str_0)

def test_case_2():
    str_0 = 'x'
    attrs_0 = module_0.Attrs(str_0)
    attrs_1 = module_0.Attrs(str_0)
    var_0 = attrs_0.__eq__(attrs_1)

def test_case_3():
    str_0 = 'v_aar'
    keys_0 = module_0.Keys(str_0)
    var_0 = keys_0.items(keys_0)

def test_case_4():
    str_0 = 'items.params'
    indices_0 = module_0.Indices(str_0)
    var_0 = indices_0[:]
    var_1 = None
    var_2 = slice(var_1)

def test_case_5():
    str_0 = 'v*aar'
    keys_0 = module_0.Keys(str_0)
    var_0 = keys_0.items(keys_0)

def test_case_6():
    str_0 = 'var1'
    str_1 = 'exclude1'
    str_2 = 'exclude2'
    str_3 = [str_1, str_2]
    attrs_0 = module_0.Attrs(str_0, str_3)
    str_4 = 'var2'
    str_5 = 'exclude3'
    str_6 = [str_2, str_5]
    bool_0 = False
    var_0 = attrs_0.__eq__(bool_0)
    attrs_1 = module_0.Attrs(str_4, str_6)
    str_7 = [str_1, str_2]
    attrs_2 = module_0.Attrs(str_0, str_7)
    var_1 = attrs_0.__eq__(attrs_2)
    var_2 = attrs_0.__eq__(attrs_1)