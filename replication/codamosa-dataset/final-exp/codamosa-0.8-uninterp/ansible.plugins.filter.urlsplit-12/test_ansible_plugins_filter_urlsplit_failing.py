# Automatically generated by Pynguin.
import ansible.plugins.filter.urlsplit as module_0

def test_case_0():
    try:
        str_0 = 'Invalid params'
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.split_url(str_0, filter_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -1725.053485
        var_0 = module_0.split_url(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        int_0 = 2318
        list_0 = [var_0, var_0, int_0, int_0]
        str_0 = ''
        dict_0 = {str_0: list_0}
        filter_module_1 = module_0.FilterModule(*list_0, **dict_0)
    except BaseException:
        pass