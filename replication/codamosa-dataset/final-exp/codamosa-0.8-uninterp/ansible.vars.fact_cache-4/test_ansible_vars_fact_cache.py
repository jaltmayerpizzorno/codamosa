# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    pass

def test_case_1():
    fact_cache_0 = module_0.FactCache()

def test_case_2():
    dict_0 = {}
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.copy()
    fact_cache_1 = module_0.FactCache(**dict_0)
    var_1 = fact_cache_1.__iter__()
    var_2 = fact_cache_1.copy()

def test_case_3():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.__len__()

def test_case_4():
    dict_0 = {}
    fact_cache_0 = module_0.FactCache(**dict_0)
    var_0 = fact_cache_0.keys()
    fact_cache_1 = module_0.FactCache()
    var_1 = fact_cache_1.flush()

def test_case_5():
    fact_cache_0 = module_0.FactCache()
    str_0 = 'hello'
    var_0 = fact_cache_0.keys()
    str_1 = 'world'
    str_2 = {str_0: str_1}
    str_3 = '192.168.1.1'
    var_1 = fact_cache_0.first_order_merge(str_3, str_2)
    var_2 = fact_cache_0.copy()
    str_4 = 'universe'
    str_5 = {str_0: str_4}
    var_3 = fact_cache_0.first_order_merge(str_3, str_5)