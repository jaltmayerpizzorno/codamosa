# Automatically generated by Pynguin.
import ansible.plugins.filter.urls as module_0

def test_case_0():
    filter_module_0 = module_0.FilterModule()

def test_case_1():
    str_0 = ' -o StrictHostKeyChecking=no'
    var_0 = module_0.unicode_urldecode(str_0)

def test_case_2():
    str_0 = '(BYVpNBFwL?4)TiA'
    var_0 = module_0.unicode_urlencode(str_0)

def test_case_3():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_4():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()
    str_0 = 'q")g/\x0bnof7"\nCa*'
    var_1 = module_0.do_urlencode(str_0)
    var_2 = filter_module_0.filters()
    str_1 = ' -o StrictHostKeyCheck#ng=no'
    var_3 = module_0.unicode_urldecode(str_1)