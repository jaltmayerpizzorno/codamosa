# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    try:
        list_0 = []
        invalid_pattern_0 = module_0.InvalidPattern(list_0)
        var_0 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        invalid_pattern_0 = module_0.InvalidPattern(list_0)
        var_0 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\\A"(.*)"6X'
        bool_0 = True
        lazy_regex_0 = module_0.LazyRegex()
        float_0 = -2280.0686
        lazy_regex_1 = module_0.LazyRegex()
        list_0 = []
        tuple_0 = (bool_0, float_0, lazy_regex_1, list_0)
        invalid_pattern_0 = module_0.InvalidPattern(tuple_0)
        tuple_1 = ()
        invalid_pattern_1 = module_0.InvalidPattern(tuple_1)
        var_0 = invalid_pattern_1.__eq__(invalid_pattern_0)
        invalid_pattern_2 = module_0.InvalidPattern(str_0)
        var_1 = str(invalid_pattern_2)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 3
        int_1 = 1738
        invalid_pattern_0 = module_0.InvalidPattern(int_1)
        var_0 = invalid_pattern_0.__eq__(int_0)
        var_1 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -2135.6
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getattr__(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getstate__()
        var_1 = lazy_regex_0.__getattr__(lazy_regex_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\xbd=],\xe5\xd0\x06\xdeP\xa3\x91\xf1\x89\xd7\xe1\xc5wr-'
        lazy_regex_0 = module_0.LazyRegex()
        str_0 = '.[[\t@3N}%mFJ6R|\n\x0cY'
        tuple_0 = (bytes_0, lazy_regex_0, lazy_regex_0, str_0)
        var_0 = lazy_regex_0.__setstate__(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
        var_0 = module_0.finditer_public(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        lazy_regex_0 = module_0.LazyRegex()
        set_0 = {lazy_regex_0, lazy_regex_0, bool_0}
        var_0 = module_0.finditer_public(lazy_regex_0, set_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '7'
        str_1 = ';'
        lazy_regex_0 = module_0.LazyRegex(str_0)
        var_0 = lazy_regex_0.__getattr__(str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'aLazyRegexpObject'
        bytes_1 = (bytes_0,)
        lazy_regex_0 = module_0.LazyRegex(bytes_1)
        str_0 = 'pattern'
        var_0 = lazy_regex_0.__getattr__(str_0)
        str_1 = '_real_regex'
        var_1 = lazy_regex_0.__getattr__(str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = "~6b\t(.no.gu[d)x_S'"
        list_0 = [str_0]
        lazy_regex_0 = module_0.LazyRegex(list_0)
        lazy_regex_1 = module_0.LazyRegex(str_0)
        var_0 = lazy_regex_0.__getattr__(lazy_regex_1)
    except BaseException:
        pass