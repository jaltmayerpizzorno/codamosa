# Automatically generated by Pynguin.
import ansible.plugins.filter.urls as module_0

def test_case_0():
    filter_module_0 = module_0.FilterModule()

def test_case_1():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_2():
    str_0 = 'hello world'
    var_0 = module_0.do_urlencode(str_0)

def test_case_3():
    str_0 = 'parameter'
    var_0 = module_0.unicode_urldecode(str_0)
    str_1 = '<uJ'
    var_1 = module_0.do_urlencode(str_1)
    list_0 = []
    var_2 = module_0.do_urlencode(list_0)