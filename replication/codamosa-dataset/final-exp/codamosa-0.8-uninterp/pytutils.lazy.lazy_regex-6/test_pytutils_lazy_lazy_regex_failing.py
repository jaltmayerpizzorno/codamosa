# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    try:
        int_0 = -2269
        invalid_pattern_0 = module_0.InvalidPattern(int_0)
        var_0 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'O'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        var_0 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        invalid_pattern_0 = module_0.InvalidPattern(bool_0)
        var_0 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "fzx&'?ce*cJ 8t"
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getattr__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -164
        invalid_pattern_0 = module_0.InvalidPattern(int_0)
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getstate__()
        var_1 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = None
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__setstate__(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '-'
        lazy_regex_0 = module_0.LazyRegex(str_0)
        var_0 = lazy_regex_0.__getstate__()
        dict_0 = {}
        invalid_pattern_0 = module_0.InvalidPattern(dict_0)
        set_0 = None
        invalid_pattern_1 = module_0.InvalidPattern(set_0)
        var_1 = module_0.finditer_public(invalid_pattern_0, invalid_pattern_0)
    except BaseException:
        pass

def test_case_7():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        bytes_0 = b'\x98\x90.\x07\x06P\x14\x98\xe9\x1c\xb8_'
        var_0 = module_0.finditer_public(lazy_regex_0, bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'r'
        lazy_regex_0 = module_0.LazyRegex(str_0)
        bytes_0 = b'X\x7fj\xd8=\xb7\xed\xc4'
        var_0 = lazy_regex_0.__getattr__(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        tuple_0 = None
        invalid_pattern_0 = module_0.InvalidPattern(tuple_0)
        bytes_0 = b'\x9c\xcb\xb4\x91\xf2\x1b9\x0f\xe4\x1c\xd7'
        invalid_pattern_1 = module_0.InvalidPattern(bytes_0)
        var_0 = invalid_pattern_1.__eq__(invalid_pattern_0)
        dict_0 = {}
        lazy_regex_0 = module_0.LazyRegex()
        var_1 = lazy_regex_0.__getattr__(dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '@-'
        str_1 = '_preformatted_string'
        str_2 = '{f%d}`As o)^HL'
        dict_0 = {str_2: str_0, str_2: str_2}
        lazy_regex_0 = module_0.LazyRegex(dict_0)
        var_0 = lazy_regex_0.__getattr__(str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '[a-z]'
        int_0 = 8
        var_0 = (str_0, int_0)
        lazy_regex_0 = module_0.LazyRegex(var_0)
        var_1 = lazy_regex_0.flags
        bool_0 = False
        var_2 = lazy_regex_0.__getattr__(bool_0)
    except BaseException:
        pass