# Automatically generated by Pynguin.
import ansible.plugins.lookup.varnames as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(lookup_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 11
        list_0 = [int_0]
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(int_0, list_0)
    except BaseException:
        pass