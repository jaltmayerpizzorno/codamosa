# Automatically generated by Pynguin.
import ansible.plugins.lookup.random_choice as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(lookup_module_0, lookup_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = None
        bytes_0 = None
        lookup_module_1 = module_0.LookupModule(lookup_module_0)
        dict_0 = {}
        lookup_module_2 = module_0.LookupModule(**dict_0)
        var_0 = lookup_module_2.run(lookup_module_0, bytes_0)
        float_0 = 1000.0
        lookup_module_3 = module_0.LookupModule(float_0)
        dict_1 = {}
        var_1 = lookup_module_2.run(lookup_module_2, **dict_1)
    except BaseException:
        pass