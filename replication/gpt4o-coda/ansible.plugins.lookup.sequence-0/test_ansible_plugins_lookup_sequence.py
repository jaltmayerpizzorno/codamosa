# Automatically generated by Pynguin.
import ansible.plugins.lookup.sequence as module_0

def test_case_0():
    lookup_module_0 = module_0.LookupModule()

def test_case_1():
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.reset()

def test_case_2():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '8'
    var_0 = lookup_module_0.run(str_0, str_0)

def test_case_3():
    lookup_module_0 = module_0.LookupModule()
    dict_0 = {}
    var_0 = lookup_module_0.parse_kv_args(dict_0)