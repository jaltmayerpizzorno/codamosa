# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    try:
        bool_0 = False
        dict_0 = {}
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.first_order_merge(bool_0, dict_0)
        bytes_0 = b'B\x89\xd96x'
        fact_cache_1 = module_0.FactCache()
        var_1 = fact_cache_1.first_order_merge(bytes_0, dict_0)
        var_2 = fact_cache_1.copy()
        var_3 = fact_cache_1.__setitem__(fact_cache_0, fact_cache_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        list_0 = []
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__setitem__(bool_0, list_0)
        fact_cache_1 = module_0.FactCache()
        var_1 = fact_cache_1.keys()
        var_2 = fact_cache_1.__len__()
        var_3 = fact_cache_1.__len__()
        list_1 = None
        var_4 = fact_cache_0.keys()
        var_5 = fact_cache_1.__getitem__(list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        fact_cache_0 = module_0.FactCache()
        bool_0 = False
        var_0 = fact_cache_0.__contains__(bool_0)
        var_1 = fact_cache_0.__getitem__(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'l^k~IWi%_h'
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = '2.18.%131'
        var_0 = fact_cache_0.__iter__()
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
        var_2 = fact_cache_0.keys()
        var_3 = fact_cache_0.first_order_merge(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.copy()
    except BaseException:
        pass

def test_case_6():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = '!,ID$c%eAk{5_rtrdW'
        var_0 = fact_cache_0.first_order_merge(str_0, str_0)
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
    except BaseException:
        pass