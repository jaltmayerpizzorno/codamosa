# Automatically generated by Pynguin.
import ansible.plugins.filter.urls as module_0

def test_case_0():
    try:
        int_0 = 520
        var_0 = module_0.do_urlencode(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'bTPB%vH'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0, str_0, dict_0]
        bytes_0 = b'I\x8a\xe7\xd0\xd6'
        var_0 = module_0.unicode_urlencode(list_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'zj7\r'
        list_0 = [str_0, str_0]
        var_0 = module_0.do_urlencode(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        filter_module_0 = module_0.FilterModule()
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        str_0 = "R\r'#]r?j~87zInVNG>+"
        var_0 = module_0.unicode_urldecode(str_0)
        var_1 = module_0.do_urlencode(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        filter_module_0 = module_0.FilterModule()
        str_0 = "]cu_D]<o'0#|xiGp1"
        var_0 = filter_module_0.filters()
        str_1 = '--json'
        var_1 = module_0.do_urlencode(str_1)
        bytes_0 = b'\xa0\xdb\xedo<\xf3\x8f4\xd3\xcf'
        var_2 = filter_module_0.filters()
        str_2 = '"[4'
        var_3 = module_0.do_urldecode(str_0)
        int_0 = -785
        float_0 = 512.0
        dict_0 = {str_2: int_0, float_0: bytes_0, float_0: var_3}
        var_4 = module_0.do_urlencode(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'PSRP RC: %d'
        dict_0 = {str_0: str_0, str_0: str_0}
        var_0 = module_0.do_urlencode(dict_0)
        complex_0 = None
        var_1 = module_0.do_urlencode(complex_0)
    except BaseException:
        pass