# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = 'name'
        var_0 = fact_cache_0.get(str_0)
        str_1 = 'value'
        var_1 = fact_cache_0.keys()
        var_2 = fact_cache_0.flush()
        str_2 = {str_0: str_1}
        var_3 = fact_cache_0.update(str_2)
        var_4 = fact_cache_0.copy()
        var_5 = fact_cache_0.first_order_merge(str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = 'name'
        var_0 = fact_cache_0.get(str_0)
        str_1 = 'value'
        var_1 = fact_cache_0.flush()
        str_2 = {str_0: str_1}
        var_2 = fact_cache_0.update(str_2)
        var_3 = fact_cache_0.first_order_merge(str_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = 'value'
        str_1 = {str_0: str_0}
        var_0 = fact_cache_0.update(str_1)
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__delitem__(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ';D+ADA*V(cStkbF=\x0c4V'
        float_0 = -1165.284
        str_1 = 'h@xKjv\\akP\nM|'
        str_2 = 'Mr8%C@~F4Ue!<#qvX'
        dict_0 = {str_0: float_0, str_1: str_2}
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__contains__(dict_0)
    except BaseException:
        pass