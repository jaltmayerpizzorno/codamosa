# Automatically generated by Pynguin.
import ansible.plugins.filter.urls as module_0

def test_case_0():
    try:
        dict_0 = {}
        var_0 = module_0.unicode_urldecode(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        var_0 = module_0.do_urlencode(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'dK[~PQ40(fx:=%[\x0bPfQ'
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.unicode_urlencode(str_0, filter_module_0)
        filter_module_1 = module_0.FilterModule()
        var_1 = filter_module_1.filters()
        set_0 = set()
        dict_0 = {}
        var_2 = filter_module_1.filters()
        var_3 = module_0.do_urlencode(dict_0)
        var_4 = module_0.unicode_urlencode(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        dict_0 = {}
        var_1 = filter_module_0.filters()
        var_2 = module_0.do_urlencode(dict_0)
        float_0 = 73.6031
        var_3 = module_0.unicode_urlencode(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 254
        tuple_0 = ()
        dict_0 = {tuple_0: int_0}
        var_0 = module_0.do_urlencode(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        str_0 = '>r=h#GMWkf4L'
        dict_0 = {str_0: bool_0}
        var_0 = module_0.do_urlencode(dict_0)
    except BaseException:
        pass