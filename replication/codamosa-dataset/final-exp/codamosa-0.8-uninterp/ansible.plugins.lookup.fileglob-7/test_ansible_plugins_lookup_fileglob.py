# Automatically generated by Pynguin.
import ansible.plugins.lookup.fileglob as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'ansible_search_path'
    str_1 = {str_0: str_0}
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.run(str_1, str_1)

def test_case_2():
    str_0 = 'ansible_search_path'
    str_1 = '.U.tese_lokup_pl*ins'
    str_2 = {str_0: str_1}
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.run(str_0, str_2)
    var_1 = lookup_module_0.run(str_1, str_2)