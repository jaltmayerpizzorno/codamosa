# Automatically generated by Pynguin.
import flutils.decorators as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = None
    cached_property_0 = module_0.cached_property(bool_0)

def test_case_2():
    bool_0 = None
    str_0 = 'p'
    int_0 = 128
    cached_property_0 = module_0.cached_property(int_0)
    var_0 = cached_property_0.__get__(bool_0, str_0)