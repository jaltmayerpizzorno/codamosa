# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    pass

def test_case_1():
    fact_cache_0 = module_0.FactCache()

def test_case_2():
    fact_cache_0 = module_0.FactCache()
    str_0 = '\tX[WPwkI9WHS2Qu#2Rh"'
    var_0 = fact_cache_0.__contains__(str_0)

def test_case_3():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.keys()
    fact_cache_1 = module_0.FactCache()
    var_1 = fact_cache_0.__iter__()
    var_2 = fact_cache_1.__iter__()

def test_case_4():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
    list_0 = []
    float_0 = 1418.14
    bytes_0 = b'rw\xae\x7f'
    fact_cache_0 = module_0.FactCache(*list_0)
    var_0 = fact_cache_0.__setitem__(float_0, bytes_0)
    fact_cache_1 = module_0.FactCache(*list_0)
    var_1 = fact_cache_1.first_order_merge(tuple_0, dict_0)