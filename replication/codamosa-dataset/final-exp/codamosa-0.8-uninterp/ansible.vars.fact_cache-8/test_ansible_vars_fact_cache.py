# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    pass

def test_case_1():
    fact_cache_0 = module_0.FactCache()

def test_case_2():
    float_0 = None
    str_0 = '8<Zbp4^Zm\\ j^$'
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.first_order_merge(float_0, str_0)

def test_case_3():
    list_0 = []
    fact_cache_0 = module_0.FactCache(*list_0)
    var_0 = fact_cache_0.keys()
    fact_cache_1 = module_0.FactCache()
    var_1 = fact_cache_1.flush()
    fact_cache_2 = module_0.FactCache()
    var_2 = fact_cache_2.copy()

def test_case_4():
    fact_cache_0 = module_0.FactCache()
    str_0 = 'in local.exec_command()'
    str_1 = "8|c'\n"
    dict_0 = {str_0: fact_cache_0}
    var_0 = fact_cache_0.__setitem__(str_1, dict_0)
    tuple_0 = None
    var_1 = fact_cache_0.copy()
    var_2 = fact_cache_0.copy()
    bool_0 = False
    var_3 = fact_cache_0.first_order_merge(tuple_0, bool_0)
    fact_cache_1 = module_0.FactCache()
    var_4 = fact_cache_1.flush()
    var_5 = fact_cache_0.flush()