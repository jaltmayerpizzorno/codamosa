# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    fact_cache_0 = module_0.FactCache()

def test_case_1():
    str_0 = 'test_key'
    str_1 = 'test_value'
    str_2 = {str_0: str_1}
    str_3 = 'test_key_m1'
    str_4 = 'test_m1'
    str_5 = {str_3: str_4}
    str_6 = 'test_key_m2'
    str_7 = {str_6: str_5}
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.__setitem__(str_0, str_2)
    var_1 = fact_cache_0.first_order_merge(str_0, str_5)
    var_2 = fact_cache_0.copy()
    var_3 = fact_cache_0.first_order_merge(str_0, str_7)

def test_case_2():
    fact_cache_0 = module_0.FactCache()
    float_0 = 408.0
    var_0 = fact_cache_0.first_order_merge(float_0, fact_cache_0)

def test_case_3():
    list_0 = []
    fact_cache_0 = module_0.FactCache(*list_0)
    var_0 = fact_cache_0.__iter__()
    list_1 = []
    fact_cache_1 = module_0.FactCache(*list_1)
    var_1 = fact_cache_1.__iter__()
    dict_0 = {}
    fact_cache_2 = module_0.FactCache(*list_1, **dict_0)
    var_2 = fact_cache_1.copy()
    var_3 = fact_cache_2.keys()

def test_case_4():
    tuple_0 = None
    str_0 = ''
    set_0 = None
    fact_cache_0 = None
    tuple_1 = (tuple_0, str_0, set_0, fact_cache_0)
    fact_cache_1 = module_0.FactCache()
    var_0 = fact_cache_1.__setitem__(tuple_1, tuple_1)
    fact_cache_2 = module_0.FactCache()
    var_1 = fact_cache_2.keys()

def test_case_5():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.flush()