# Automatically generated by Pynguin.
import ansible.plugins.lookup.inventory_hostnames as module_0

def test_case_0():
    try:
        complex_0 = None
        lookup_module_0 = module_0.LookupModule(complex_0)
        dict_0 = {complex_0: lookup_module_0}
        var_0 = lookup_module_0.run(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'groups'
        str_1 = {str_0: str_0, str_0: str_0}
        str_2 = {str_0: str_1}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_2, str_2)
    except BaseException:
        pass