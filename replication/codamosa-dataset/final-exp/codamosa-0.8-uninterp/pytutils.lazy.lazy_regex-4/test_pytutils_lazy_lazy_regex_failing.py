# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        invalid_pattern_0 = module_0.InvalidPattern(lazy_regex_0)
        var_0 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        invalid_pattern_0 = module_0.InvalidPattern(list_0)
        var_0 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 373.80025318230963
        invalid_pattern_0 = module_0.InvalidPattern(float_0)
        var_0 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 312
        var_0 = module_0.lazy_compile()
        var_1 = module_0.reset_compile()
        var_2 = module_0.install_lazy_compile()
        dict_0 = {}
        set_0 = {var_0, var_0, var_2, int_0}
        lazy_regex_0 = module_0.LazyRegex(set_0)
        var_3 = lazy_regex_0.__getattr__(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getattr__(lazy_regex_0)
    except BaseException:
        pass

def test_case_5():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getstate__()
        lazy_regex_1 = module_0.LazyRegex()
        var_1 = lazy_regex_1.__getattr__(lazy_regex_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        list_0 = [bool_0]
        list_1 = []
        lazy_regex_0 = module_0.LazyRegex(list_1)
        var_0 = lazy_regex_0.__setstate__(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        var_0 = module_0.lazy_compile(*list_0)
        bytes_0 = b'6\xb6)\xff~\x19F\xc3\x8a#\x05+\xber\xef&P\x08'
        invalid_pattern_0 = module_0.InvalidPattern(bytes_0)
        var_1 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '.K"gP\rM\'r\x0cc.Bq\x0csWdm\r'
        str_1 = None
        str_2 = None
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_1}
        invalid_pattern_0 = module_0.InvalidPattern(dict_0)
        bool_0 = False
        bool_1 = False
        var_0 = module_0.finditer_public(invalid_pattern_0, bool_0, bool_1)
    except BaseException:
        pass

def test_case_9():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        str_0 = 'c!\nSo\x0b:TMEQA}A\ry'
        var_0 = module_0.finditer_public(lazy_regex_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'u'
        lazy_regex_0 = module_0.LazyRegex(str_0)
        str_1 = "Re*`r\t~=:v'B"
        var_0 = lazy_regex_0.__getattr__(str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        dict_0 = {}
        invalid_pattern_0 = module_0.InvalidPattern(dict_0)
        var_0 = invalid_pattern_0.__eq__(invalid_pattern_0)
        bytes_0 = b'\x9e\x15\x03\xca35\xe0i\x18\xd9C\xd8\\\x7f\xa9#k\x15'
        var_1 = lazy_regex_0.__getattr__(bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = -1359.6010982661585
        lazy_regex_0 = module_0.LazyRegex()
        bytes_0 = b'\x1d'
        list_0 = [float_0]
        str_0 = '_real_obj'
        str_1 = 'args'
        dict_0 = {str_0: str_0, str_1: bytes_0}
        var_0 = module_0.lazy_compile(**dict_0)
        var_1 = module_0.finditer_public(bytes_0, bytes_0)
        invalid_pattern_0 = module_0.InvalidPattern(list_0)
        var_2 = lazy_regex_0.__setstate__(dict_0)
    except BaseException:
        pass