# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    pass

def test_case_1():
    fact_cache_0 = module_0.FactCache()

def test_case_2():
    str_0 = '^*b`2`f%y;+^'
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.__contains__(str_0)

def test_case_3():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.flush()
    str_0 = 'localhost'
    str_1 = 'foo'
    str_2 = 'bar'
    str_3 = {str_1: str_2}
    var_1 = fact_cache_0.first_order_merge(str_0, str_3)
    str_4 = {str_1: str_1}
    var_2 = fact_cache_0.first_order_merge(str_0, str_4)