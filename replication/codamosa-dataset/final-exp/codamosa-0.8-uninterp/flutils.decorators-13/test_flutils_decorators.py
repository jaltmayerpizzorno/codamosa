# Automatically generated by Pynguin.
import flutils.decorators as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'HHHH'
    cached_property_0 = module_0.cached_property(str_0)

def test_case_2():
    bytes_0 = None
    dict_0 = {}
    bool_0 = True
    cached_property_0 = module_0.cached_property(bool_0)
    var_0 = cached_property_0.__get__(bytes_0, dict_0)