# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    try:
        dict_0 = {}
        invalid_pattern_0 = module_0.InvalidPattern(dict_0)
        var_0 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xc6i\x051\xe9\x03\x9a\x1d8c\xbaZ\x1f\x16\n\xbc\x19\xc8'
        invalid_pattern_0 = module_0.InvalidPattern(bytes_0)
        var_0 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1249
        invalid_pattern_0 = module_0.InvalidPattern(int_0)
        int_1 = 1521
        var_0 = invalid_pattern_0.__eq__(int_1)
        var_1 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = None
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getattr__(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = None
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getstate__()
        var_1 = lazy_regex_0.__getattr__(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = module_0.reset_compile()
        var_1 = module_0.lazy_compile()
        list_0 = [var_0, var_0]
        var_2 = module_0.finditer_public(list_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        int_0 = -418
        invalid_pattern_0 = module_0.InvalidPattern(int_0)
        var_0 = invalid_pattern_0.__eq__(lazy_regex_0)
        var_1 = invalid_pattern_0.__eq__(invalid_pattern_0)
        var_2 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = 2780.761
        str_0 = 'p\nB@_sYt'
        set_0 = {str_0, str_0}
        lazy_regex_0 = module_0.LazyRegex(set_0)
        var_0 = lazy_regex_0.__getattr__(float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        dict_0 = {}
        var_0 = module_0.finditer_public(lazy_regex_0, dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = module_0.install_lazy_compile()
        bytes_0 = b'nj\x0c\x8cN\x0f\xc3ic\x08\xb2\xe7='
        str_0 = 't_)U${[zSKO/HV'
        dict_0 = {str_0: str_0}
        lazy_regex_0 = module_0.LazyRegex(dict_0)
        var_1 = lazy_regex_0.__getattr__(bytes_0)
    except BaseException:
        pass