# Automatically generated by Pynguin.
import ansible.plugins.lookup.sequence as module_0

def test_case_0():
    lookup_module_0 = module_0.LookupModule()

def test_case_1():
    str_0 = 'NY2{pMA%'
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.parse_simple_args(str_0)

def test_case_2():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '1'
    var_0 = lookup_module_0.run(str_0, lookup_module_0)

def test_case_3():
    lookup_module_0 = module_0.LookupModule()
    str_0 = 'start=1 count=5'
    list_0 = [str_0]
    var_0 = lookup_module_0.run(list_0, str_0)

def test_case_4():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '5-8'
    var_0 = lookup_module_0.parse_simple_args(str_0)

def test_case_5():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '1-10/2:%02d'
    var_0 = lookup_module_0.parse_simple_args(str_0)