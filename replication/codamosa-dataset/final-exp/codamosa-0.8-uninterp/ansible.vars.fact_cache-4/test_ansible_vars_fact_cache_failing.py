# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    try:
        str_0 = "LGl\ny5'vot!"
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__getitem__(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = '127.0.0.1'
        var_0 = fact_cache_0.first_order_merge(str_0, str_0)
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x8d\x9be\xd4\x1a\xb9\x11^\x87\xdeG\x82\xa6'
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.__delitem__(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = 'foo'
        tuple_0 = ()
        var_0 = fact_cache_0.__contains__(tuple_0)
        str_1 = 'v'
        int_0 = -7
        int_1 = {str_0: int_0}
        var_1 = fact_cache_0.first_order_merge(str_1, int_1)
        var_2 = fact_cache_0.first_order_merge(str_1, int_0)
    except BaseException:
        pass