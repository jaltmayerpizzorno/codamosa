# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    pass

def test_case_1():
    lazy_regex_0 = module_0.LazyRegex()

def test_case_2():
    str_0 = 'I^N_'
    dict_0 = {str_0: str_0}
    var_0 = module_0.lazy_compile(**dict_0)

def test_case_3():
    var_0 = module_0.reset_compile()

def test_case_4():
    var_0 = []
    lazy_regex_0 = module_0.LazyRegex(var_0)
    str_0 = 'args'
    str_1 = 'kwargs'
    var_1 = []
    var_2 = {}
    var_3 = {str_0: var_1, str_1: var_2}
    var_4 = lazy_regex_0.__setstate__(var_3)
    var_5 = module_0.install_lazy_compile()