# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'5\xba\xbecS\xa9o\xac\xa8\x82\xca'
    invalid_pattern_0 = module_0.InvalidPattern(bytes_0)

def test_case_2():
    lazy_regex_0 = module_0.LazyRegex()

def test_case_3():
    str_0 = 'test'
    str_1 = (str_0,)
    var_0 = {}
    lazy_regex_0 = module_0.LazyRegex(str_1, var_0)
    var_1 = lazy_regex_0.match
    var_2 = callable(var_1)

def test_case_4():
    lazy_regex_0 = module_0.LazyRegex()
    var_0 = lazy_regex_0.__getstate__()

def test_case_5():
    var_0 = module_0.lazy_compile()

def test_case_6():
    var_0 = module_0.install_lazy_compile()

def test_case_7():
    var_0 = module_0.reset_compile()

def test_case_8():
    lazy_regex_0 = module_0.LazyRegex()