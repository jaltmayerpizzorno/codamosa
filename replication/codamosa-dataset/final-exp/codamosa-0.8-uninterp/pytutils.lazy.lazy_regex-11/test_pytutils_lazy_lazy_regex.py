# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '8>{B\nA\x0b\\8"@5'
    invalid_pattern_0 = module_0.InvalidPattern(str_0)

def test_case_2():
    lazy_regex_0 = module_0.LazyRegex()

def test_case_3():
    str_0 = 'a regex'
    lazy_regex_0 = module_0.LazyRegex(str_0)
    var_0 = lazy_regex_0.__getstate__()
    var_1 = lazy_regex_0.__setstate__(var_0)

def test_case_4():
    list_0 = []
    var_0 = module_0.lazy_compile(*list_0)

def test_case_5():
    var_0 = module_0.install_lazy_compile()

def test_case_6():
    var_0 = module_0.reset_compile()