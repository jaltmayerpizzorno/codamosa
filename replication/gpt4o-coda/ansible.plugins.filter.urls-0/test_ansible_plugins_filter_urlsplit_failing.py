# Automatically generated by Pynguin.
import ansible.plugins.filter.urlsplit as module_0

def test_case_0():
    try:
        str_0 = 'lSIN'
        str_1 = '.'
        var_0 = module_0.split_url(str_1, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'lSIN'
        dict_0 = {}
        var_0 = module_0.split_url(dict_0, dict_0)
        str_1 = '.'
        var_1 = module_0.split_url(str_1, str_0)
    except BaseException:
        pass