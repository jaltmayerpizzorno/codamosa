# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0
import re as module_1

def test_case_0():
    try:
        tuple_0 = ()
        invalid_pattern_0 = module_0.InvalidPattern(tuple_0)
        var_0 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        invalid_pattern_0 = module_0.InvalidPattern(lazy_regex_0)
        var_0 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        invalid_pattern_0 = module_0.InvalidPattern(bool_0)
        var_0 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '[ PY\x0c'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        str_1 = 'q+2'
        var_0 = invalid_pattern_0.__eq__(str_1)
        invalid_pattern_1 = module_0.InvalidPattern(invalid_pattern_0)
        var_1 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '[ PY\x0c'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        var_0 = invalid_pattern_0.__eq__(invalid_pattern_0)
        var_1 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_5():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        invalid_pattern_0 = module_0.InvalidPattern(lazy_regex_0)
        var_0 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_6():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        bool_0 = True
        var_0 = lazy_regex_0.__getattr__(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        bool_0 = True
        var_0 = lazy_regex_0.__getstate__()
        var_1 = lazy_regex_0.__getattr__(bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        str_0 = '\\A"(.*)"\\Z'
        lazy_regex_0 = module_0.LazyRegex(str_0)
        var_0 = lazy_regex_0.__setstate__(bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = module_0.install_lazy_compile()
        lazy_regex_0 = module_0.LazyRegex()
        bool_0 = True
        var_1 = lazy_regex_0.__getattr__(bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        str_0 = '\n        A standin for a module to prevent it from being imported\n        '
        var_0 = module_0.finditer_public(str_0, str_0)
        invalid_pattern_0 = module_0.InvalidPattern(bool_0)
        var_1 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_11():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        str_0 = 'ShPDv~'
        var_0 = module_0.finditer_public(lazy_regex_0, str_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'Hello world!'
        str_1 = '(?P<one>.+) (?P<two>.+)'
        var_0 = module_1.compile(str_1)
        str_2 = (str_1,)
        lazy_regex_0 = module_0.LazyRegex(str_2)
        var_1 = lazy_regex_0.pattern
        var_2 = module_1.search(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '^foo$'
        str_1 = [str_0]
        lazy_regex_0 = module_0.LazyRegex(str_1)
        str_2 = 'match'
        var_0 = getattr(lazy_regex_0, str_2)
        var_1 = getattr(lazy_regex_0, str_2)
        bool_0 = False
        var_2 = lazy_regex_0.__getattr__(bool_0)
    except BaseException:
        pass