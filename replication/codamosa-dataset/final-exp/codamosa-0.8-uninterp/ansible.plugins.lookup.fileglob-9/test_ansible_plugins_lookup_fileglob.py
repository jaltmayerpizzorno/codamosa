# Automatically generated by Pynguin.
import ansible.plugins.lookup.fileglob as module_0

def test_case_0():
    pass

def test_case_1():
    lookup_module_0 = module_0.LookupModule()
    str_0 = 'ansible_search_path'
    str_1 = {str_0: str_0, str_0: str_0}
    var_0 = lookup_module_0.run(str_1, str_1)

def test_case_2():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '\r&%pr\r553a>#B_&'
    str_1 = [str_0]
    str_2 = 'some_variable'
    str_3 = 'ansible_search_path'
    str_4 = ''
    str_5 = '|)r6e'
    str_6 = [str_4, str_4, str_5, str_5]
    str_7 = {str_2: str_6, str_3: str_6}
    var_0 = lookup_module_0.run(str_1, str_7)
    lookup_module_1 = module_0.LookupModule()