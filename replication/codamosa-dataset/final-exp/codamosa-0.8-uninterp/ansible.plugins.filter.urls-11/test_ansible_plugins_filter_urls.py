# Automatically generated by Pynguin.
import ansible.plugins.filter.urls as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'I#\x0bR86#{&T$\nh$"F9|'
    var_0 = module_0.do_urldecode(str_0)

def test_case_2():
    str_0 = 'Hq+\x0bnT'
    var_0 = module_0.do_urlencode(str_0)

def test_case_3():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_4():
    str_0 = 'Hq+\x0bnT'
    var_0 = module_0.unicode_urldecode(str_0)
    filter_module_0 = module_0.FilterModule()
    var_1 = filter_module_0.filters()
    var_2 = filter_module_0.filters()
    var_3 = filter_module_0.filters()
    var_4 = filter_module_0.filters()
    str_1 = '|$z6mQuwJ.1a+\x0cNsdI'
    var_5 = module_0.do_urlencode(str_1)
    bytes_0 = b''
    filter_module_1 = module_0.FilterModule()
    var_6 = module_0.do_urlencode(bytes_0)