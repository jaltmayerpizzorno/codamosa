# Automatically generated by Pynguin.
import ansible.plugins.lookup.sequence as module_0

def test_case_0():
    pass

def test_case_1():
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.reset()

def test_case_2():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '1'
    var_0 = lookup_module_0.parse_simple_args(str_0)

def test_case_3():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '1-5'
    str_1 = '1-5/2'
    str_2 = [str_0, str_1, str_0, str_1, str_1, str_1, str_0, str_0]
    var_0 = lookup_module_0.run(str_2, lookup_module_0)

def test_case_4():
    lookup_module_0 = module_0.LookupModule()
    str_0 = 'count=4'
    str_1 = 'start=10 end=0 stride=-1'
    str_2 = [str_0, str_1, str_1, str_0, str_0, str_0, str_1, str_1, str_1, str_1]
    var_0 = lookup_module_0.run(str_2, str_2)

def test_case_5():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '1'
    var_0 = lookup_module_0.parse_simple_args(str_0)
    str_1 = '4-8'
    var_1 = lookup_module_0.parse_simple_args(str_1)

def test_case_6():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '1-5'
    str_1 = '1-5/2:0x%02x'
    str_2 = [str_0, str_1, str_1, str_0, str_0]
    var_0 = None
    var_1 = lookup_module_0.run(str_2, var_0)