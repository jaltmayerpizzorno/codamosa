# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    try:
        int_0 = 1354
        invalid_pattern_0 = module_0.InvalidPattern(int_0)
        var_0 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '}\r<xdq)?S`'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        var_0 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1335
        invalid_pattern_0 = module_0.InvalidPattern(int_0)
        var_0 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '!2IuS.\\\tX8'
        bool_0 = True
        invalid_pattern_0 = module_0.InvalidPattern(bool_0)
        var_0 = invalid_pattern_0.__eq__(str_0)
        var_1 = invalid_pattern_0.__eq__(invalid_pattern_0)
        invalid_pattern_1 = module_0.InvalidPattern(str_0)
        set_0 = set()
        lazy_regex_0 = module_0.LazyRegex(str_0)
        var_2 = lazy_regex_0.__getattr__(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'vY'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        list_0 = []
        var_0 = invalid_pattern_0.__eq__(list_0)
        var_1 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_5():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        str_0 = 'bq?X'
        var_0 = module_0.finditer_public(lazy_regex_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'MZ}(]\n=~-8'
        lazy_regex_0 = module_0.LazyRegex()
        lazy_regex_1 = module_0.LazyRegex(lazy_regex_0)
        set_0 = {str_0, str_0, str_0}
        lazy_regex_2 = module_0.LazyRegex(set_0)
        var_0 = lazy_regex_2.__getattr__(lazy_regex_1)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0]
        var_0 = module_0.lazy_compile(*list_0)
        dict_0 = None
        var_1 = module_0.finditer_public(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '}'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        set_0 = set()
        lazy_regex_0 = module_0.LazyRegex(str_0)
        var_0 = lazy_regex_0.__getattr__(set_0)
    except BaseException:
        pass