# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    pass

def test_case_1():
    lazy_regex_0 = module_0.LazyRegex()

def test_case_2():
    str_0 = 'jDSY=r[4="lOTP1{Yq*V'
    lazy_regex_0 = module_0.LazyRegex(str_0)
    var_0 = lazy_regex_0.__getstate__()

def test_case_3():
    var_0 = module_0.lazy_compile()

def test_case_4():
    var_0 = module_0.install_lazy_compile()

def test_case_5():
    var_0 = module_0.reset_compile()

def test_case_6():
    lazy_regex_0 = module_0.LazyRegex()
    str_0 = 'args'
    str_1 = 'kwargs'
    var_0 = ()
    var_1 = {}
    var_2 = {str_0: var_0, str_1: var_1}
    var_3 = lazy_regex_0.__setstate__(var_2)
    str_2 = 'regex'
    var_4 = ()
    var_5 = {}
    var_6 = ()
    var_7 = {str_0: var_4, str_1: var_5, str_2: var_6}
    var_8 = lazy_regex_0.__setstate__(var_7)