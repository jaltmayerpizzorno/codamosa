# Automatically generated by Pynguin.
import ansible.plugins.lookup.nested as module_0

def test_case_0():
    try:
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        var_0 = lookup_module_0.run(dict_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'o:g&'
        var_0 = lookup_module_0.run(str_0)
    except BaseException:
        pass