# Automatically generated by Pynguin.
import ansible.plugins.filter.urls as module_0

def test_case_0():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.do_urldecode(filter_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        var_0 = module_0.do_urlencode(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'serole'
        str_1 = "wU9m's?5xFNT[z%%j\\X*"
        int_0 = 512
        dict_0 = {int_0: int_0, str_1: str_0, str_0: int_0, int_0: str_0}
        tuple_0 = (str_0, str_1, dict_0)
        bool_0 = True
        tuple_1 = (tuple_0, bool_0)
        str_2 = '09\x0bl5ZmBu5Lf=H'
        str_3 = ''
        dict_1 = {str_2: str_0, str_3: int_0}
        tuple_2 = (tuple_1, dict_0, dict_1, dict_0)
        var_0 = module_0.unicode_urlencode(tuple_2, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'MS'
        var_0 = module_0.do_urlencode(str_0)
        var_1 = module_0.unicode_urlencode(str_0)
        bytes_0 = b"7\x96P\xcf\xdfd'c\xe5\xd7\xac6\x81\xc0\x15\x8b"
        var_2 = module_0.do_urlencode(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        str_0 = None
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        dict_0 = {str_0: str_0}
        var_1 = filter_module_0.filters()
        tuple_0 = (dict_0, dict_0)
        dict_1 = {filter_module_0: tuple_0, bool_0: str_0}
        var_2 = module_0.do_urlencode(dict_1)
    except BaseException:
        pass

def test_case_5():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        dict_0 = None
        dict_1 = {}
        var_1 = module_0.do_urlencode(dict_1)
        var_2 = module_0.do_urldecode(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ' 9'
        set_0 = {str_0}
        var_0 = module_0.do_urlencode(set_0)
    except BaseException:
        pass