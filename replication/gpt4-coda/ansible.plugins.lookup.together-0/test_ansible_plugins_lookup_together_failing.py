# Automatically generated by Pynguin.
import ansible.plugins.lookup.together as module_0

def test_case_0():
    try:
        tuple_0 = ()
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '{~"q n5'
        dict_0 = {str_0: str_0}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        list_0 = [dict_0, str_0, lookup_module_0, str_0]
        var_0 = lookup_module_0.run(list_0)
    except BaseException:
        pass