# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    pass

def test_case_1():
    fact_cache_0 = module_0.FactCache()

def test_case_2():
    bytes_0 = b'\xb2\xe6\xfdY6\x19*\xcf\xb5\x89\xf2\xbb\xddP:\x16'
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.__contains__(bytes_0)
    bool_0 = True
    str_0 = '!YEj=.g`j]1'
    fact_cache_1 = module_0.FactCache()
    var_1 = fact_cache_1.__setitem__(bool_0, str_0)

def test_case_3():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.__len__()

def test_case_4():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.flush()