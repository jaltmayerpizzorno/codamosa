# Automatically generated by Pynguin.
import flutils.decorators as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = None
    cached_property_0 = module_0.cached_property(dict_0)

def test_case_2():
    bytes_0 = b'\r\xc9\x0b\xa3\x19'
    float_0 = None
    str_0 = 'K{KzI8{'
    bool_0 = True
    tuple_0 = (bool_0,)
    float_1 = None
    set_0 = {tuple_0, float_0, float_1}
    list_0 = [bytes_0, float_0, set_0]
    cached_property_0 = module_0.cached_property(float_0)
    var_0 = cached_property_0.__get__(float_0, list_0)
    str_1 = 'w-\x0b\te?PXBu_\n+U'
    cached_property_1 = module_0.cached_property(str_1)
    cached_property_2 = module_0.cached_property(cached_property_1)
    var_1 = cached_property_2.__get__(float_0, str_0)
    cached_property_3 = module_0.cached_property(bytes_0)