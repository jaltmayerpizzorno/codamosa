# Automatically generated by Pynguin.
import ansible.plugins.filter.urlsplit as module_0

def test_case_0():
    filter_module_0 = module_0.FilterModule()

def test_case_1():
    str_0 = 'X}?e"k[\t$1\\no\r0}`AP'
    tuple_0 = ()
    var_0 = module_0.split_url(str_0, tuple_0)

def test_case_2():
    str_0 = 'http://example.com/path?query=1#fragment'
    str_1 = 'scheme'
    str_2 = 'netloc'
    str_3 = 'path'
    var_0 = module_0.split_url(str_0)
    var_1 = module_0.split_url(str_0, str_1)
    var_2 = module_0.split_url(str_0, str_2)
    var_3 = module_0.split_url(str_0, str_3)