# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    var_0 = module_0.lazy_compile()

def test_case_1():
    lazy_regex_0 = module_0.LazyRegex()
    invalid_pattern_0 = module_0.InvalidPattern(lazy_regex_0)

def test_case_2():
    float_0 = None
    str_0 = '@-'
    invalid_pattern_0 = module_0.InvalidPattern(str_0)
    var_0 = invalid_pattern_0.__eq__(float_0)

def test_case_3():
    var_0 = module_0.install_lazy_compile()

def test_case_4():
    var_0 = module_0.reset_compile()

def test_case_5():
    lazy_regex_0 = module_0.LazyRegex()
    str_0 = 'args'
    str_1 = 'kwargs'
    str_2 = '1'
    str_3 = (str_2,)
    var_0 = {}
    var_1 = {str_0: str_3, str_1: var_0}
    var_2 = lazy_regex_0.__setstate__(var_1)