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
        lookup_module_0 = module_0.LookupModule()
        bool_0 = True
        str_0 = 'T&shu=wu2?\x0c-UW/M'
        tuple_0 = (str_0, str_0, lookup_module_0)
        var_0 = lookup_module_0.run(bool_0, tuple_0)
    except BaseException:
        pass