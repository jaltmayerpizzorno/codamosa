# Automatically generated by Pynguin.
import ansible.plugins.lookup.sequence as module_0

def test_case_0():
    pass

def test_case_1():
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.reset()

def test_case_2():
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.reset()
    str_0 = '1'
    str_1 = '3'
    var_1 = dict(start=str_0, end=str_1)
    var_2 = lookup_module_0.parse_kv_args(var_1)
    var_3 = len(var_1)
    str_2 = '0x2'
    str_3 = '0x5'
    str_4 = '2'
    str_5 = '0x%%02x'
    var_4 = dict(start=str_2, end=str_3, stride=str_4, format=str_5)
    var_5 = lookup_module_0.reset()
    var_6 = lookup_module_0.parse_kv_args(var_4)

def test_case_3():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '2-10/2'
    var_0 = lookup_module_0.parse_simple_args(str_0)
    lookup_module_1 = module_0.LookupModule()
    str_1 = '5'
    var_1 = lookup_module_1.parse_simple_args(str_1)
    lookup_module_2 = module_0.LookupModule()