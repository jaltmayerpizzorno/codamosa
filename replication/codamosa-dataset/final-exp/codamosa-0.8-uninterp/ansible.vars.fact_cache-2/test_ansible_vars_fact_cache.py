# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    pass

def test_case_1():
    fact_cache_0 = module_0.FactCache()

def test_case_2():
    list_0 = None
    bytes_0 = b'\xf4&\xb0\xf4\x9f\xf0'
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.__setitem__(list_0, bytes_0)

def test_case_3():
    bytes_0 = b'C\xc2KF^#\x1d\xfd\x95\xed\xaf\xb3\xfe@%\xba\x7f'
    list_0 = []
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.first_order_merge(bytes_0, list_0)
    int_0 = -3066
    fact_cache_1 = module_0.FactCache()
    var_1 = fact_cache_1.__contains__(int_0)

def test_case_4():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.flush()
    bytes_0 = b'-\xaa\xf6\xe0\xa7\xf9\x8a\xed\xda)\x98\xa7\xec\n'
    var_1 = fact_cache_0.flush()
    int_0 = -1675
    fact_cache_1 = module_0.FactCache()
    tuple_0 = ()
    var_2 = fact_cache_1.__contains__(tuple_0)
    var_3 = fact_cache_0.__iter__()
    var_4 = fact_cache_1.__setitem__(bytes_0, int_0)

def test_case_5():
    dict_0 = {}
    fact_cache_0 = module_0.FactCache(**dict_0)
    var_0 = fact_cache_0.__len__()

def test_case_6():
    dict_0 = {}
    fact_cache_0 = module_0.FactCache(**dict_0)
    var_0 = fact_cache_0.copy()

def test_case_7():
    bytes_0 = b'C\xc2KF^#\x1d\xfd\x95\xed\xaf\xb3\xfe@%\xba\x7f'
    list_0 = []
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.first_order_merge(bytes_0, list_0)
    int_0 = -3066
    fact_cache_1 = module_0.FactCache()
    var_1 = fact_cache_0.copy()
    var_2 = fact_cache_1.__contains__(int_0)
    list_1 = []
    dict_0 = {}
    fact_cache_2 = module_0.FactCache(*list_1, **dict_0)
    str_0 = 'SCs{gXR0T]%|U([?aOwJ'
    var_3 = fact_cache_2.__setitem__(str_0, list_1)