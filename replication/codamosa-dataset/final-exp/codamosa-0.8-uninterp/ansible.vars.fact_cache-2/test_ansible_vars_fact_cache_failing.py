# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    try:
        bytes_0 = None
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__len__()
        fact_cache_1 = module_0.FactCache()
        var_1 = fact_cache_1.__getitem__(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'c\xd1t'
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__delitem__(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.flush()
        str_0 = 'first_order_merge_test'
        str_1 = 'test'
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
        var_2 = fact_cache_0.first_order_merge(str_0, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = 'test'
        var_0 = fact_cache_0.first_order_merge(str_0, str_0)
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
    except BaseException:
        pass