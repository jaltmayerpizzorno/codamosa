# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    fact_cache_0 = module_0.FactCache()

def test_case_1():
    int_0 = 2574
    fact_cache_0 = module_0.FactCache()
    str_0 = '-4^/gxHd&}~9LJ)'
    var_0 = fact_cache_0.first_order_merge(str_0, int_0)
    var_1 = fact_cache_0.copy()
    tuple_0 = ()
    var_2 = fact_cache_0.__contains__(int_0)
    float_0 = 1720.654463
    var_3 = fact_cache_0.__setitem__(tuple_0, float_0)

def test_case_2():
    str_0 = ' freeze'
    fact_cache_0 = module_0.FactCache()
    fact_cache_1 = module_0.FactCache()
    var_0 = fact_cache_1.__setitem__(str_0, fact_cache_0)

def test_case_3():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.keys()
    var_1 = fact_cache_0.flush()
    float_0 = -2488.1
    set_0 = None
    var_2 = fact_cache_0.__iter__()
    var_3 = fact_cache_0.first_order_merge(float_0, set_0)

def test_case_4():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.flush()
    var_1 = fact_cache_0.keys()
    var_2 = fact_cache_0.flush()
    fact_cache_1 = module_0.FactCache()

def test_case_5():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.flush()

def test_case_6():
    bytes_0 = b'3\xac\xcb'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.first_order_merge(bytes_0, dict_0)