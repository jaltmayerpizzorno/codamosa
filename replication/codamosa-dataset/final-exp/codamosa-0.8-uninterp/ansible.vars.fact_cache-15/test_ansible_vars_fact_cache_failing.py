# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    try:
        int_0 = None
        bool_0 = False
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.first_order_merge(int_0, bool_0)
        bytes_0 = b'8x\xde\x8d\xca\x08\x86\x10U\xc1\x0c\x89i\xc6n \n\x08z\x06'
        var_1 = fact_cache_0.copy()
        fact_cache_1 = module_0.FactCache()
        var_2 = fact_cache_0.__getitem__(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__getitem__(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = 'tes_key_2'
        var_0 = fact_cache_0.first_order_merge(str_0, str_0)
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__delitem__(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = None
        bool_0 = False
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.first_order_merge(int_0, bool_0)
        var_1 = fact_cache_0.__iter__()
        bytes_0 = b'8x\xde\x8d\xca\x08\x86\x10U\xc1\x0c\x89i\xc6n \n\x08z\x06'
        var_2 = fact_cache_0.__getitem__(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = 'mek_key_2'
        var_0 = fact_cache_0.first_order_merge(str_0, fact_cache_0)
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
    except BaseException:
        pass