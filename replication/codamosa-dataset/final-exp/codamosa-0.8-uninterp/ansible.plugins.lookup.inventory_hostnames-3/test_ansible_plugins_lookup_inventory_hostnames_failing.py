# Automatically generated by Pynguin.
import ansible.plugins.lookup.inventory_hostnames as module_0

def test_case_0():
    try:
        str_0 = '8 ]@d\t&<9B>2@J\n'
        tuple_0 = (str_0,)
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'groups'
        lookup_module_0 = module_0.LookupModule()
        str_1 = {str_0: str_0, str_0: str_0}
        str_2 = {str_0: str_1}
        var_0 = lookup_module_0.run(str_1, str_2)
    except BaseException:
        pass