# Automatically generated by Pynguin.
import ansible.plugins.lookup.vars as module_0

def test_case_0():
    try:
        bool_0 = False
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = None
        str_1 = 'ks}w\\w'
        dict_0 = {str_0: str_0, str_1: lookup_module_0}
        var_0 = lookup_module_0.run(lookup_module_0, dict_0)
    except BaseException:
        pass