# Automatically generated by Pynguin.
import flutils.decorators as module_0

def test_case_0():
    try:
        list_0 = []
        cached_property_0 = module_0.cached_property(list_0)
        var_0 = cached_property_0.__get__(cached_property_0, cached_property_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = None
        bool_0 = True
        cached_property_0 = None
        cached_property_1 = module_0.cached_property(bytes_0)
        var_0 = cached_property_1.__get__(cached_property_0, cached_property_0)
        var_1 = cached_property_1.__get__(bool_0, cached_property_0)
    except BaseException:
        pass