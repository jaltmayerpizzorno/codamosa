# Automatically generated by Pynguin.
import flutils.decorators as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '|wyO"`U?)J\'D2h6%XI-g'
    cached_property_0 = module_0.cached_property(str_0)

def test_case_2():
    dict_0 = None
    int_0 = 1067
    bool_0 = False
    cached_property_0 = module_0.cached_property(bool_0)
    var_0 = cached_property_0.__get__(dict_0, int_0)
    int_1 = 2115
    cached_property_1 = module_0.cached_property(int_1)

def test_case_3():
    var_0 = lambda x: x
    cached_property_0 = module_0.cached_property(var_0)
    var_1 = object()
    var_2 = cached_property_0.__get__(var_0, var_1)
    var_3 = object()
    int_0 = 1
    var_4 = lambda x: int_0