# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    try:
        bool_0 = False
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.flush()
        var_1 = fact_cache_0.first_order_merge(bool_0, bool_0)
        var_2 = fact_cache_0.copy()
        var_3 = fact_cache_0.flush()
        str_0 = 'gz2'
        var_4 = fact_cache_0.copy()
        dict_0 = {str_0: str_0}
        fact_cache_1 = module_0.FactCache(**dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        fact_cache_0 = module_0.FactCache(**dict_0)
        var_0 = fact_cache_0.__iter__()
        bytes_0 = b'\x9a\x15\x96\r\xd8\xef\xef\xbe\xf4\xa8S\x9b7\x06\x0c\x1cJ\xa4I'
        fact_cache_1 = module_0.FactCache()
        bytes_1 = b'\xa1\xdd!\xd9\xa6BLB\x05\xde\xb7\x19O\xa4\xd8\xfb\xed'
        fact_cache_2 = module_0.FactCache()
        str_0 = '`\\quzC/c|(c.G5nJ\\b'
        var_1 = fact_cache_1.copy()
        var_2 = fact_cache_1.first_order_merge(bytes_1, str_0)
        var_3 = fact_cache_1.__contains__(bytes_0)
        var_4 = fact_cache_1.__getitem__(fact_cache_1)
    except BaseException:
        pass

def test_case_2():
    try:
        fact_cache_0 = module_0.FactCache()
        str_0 = 'val'
        var_0 = fact_cache_0.first_order_merge(str_0, str_0)
        var_1 = fact_cache_0.first_order_merge(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        fact_cache_0 = module_0.FactCache()
        bytes_0 = b'\xa1\xdd!\xd9\xa6BLB\x05\xde\xb7\x19O\xa4\xd8\xfb\xed'
        fact_cache_1 = module_0.FactCache()
        str_0 = '`\\quzC/c|(c.G5nJ\\b'
        var_0 = fact_cache_0.copy()
        var_1 = fact_cache_0.first_order_merge(bytes_0, str_0)
        fact_cache_2 = module_0.FactCache()
        var_2 = fact_cache_2.flush()
        bool_0 = False
        var_3 = fact_cache_2.__delitem__(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n        This method does the low-level evaluation of each conditional\n        set on this object, using jinja2 to wrap the conditionals for\n        evaluation.\n        '
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.copy()
        dict_0 = {str_0: str_0}
        dict_1 = None
        fact_cache_1 = module_0.FactCache()
        var_1 = fact_cache_1.__setitem__(dict_0, dict_1)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = []
        int_0 = -66
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.first_order_merge(list_0, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        fact_cache_0 = module_0.FactCache()
        var_0 = fact_cache_0.flush()
        str_0 = 'oDCKwxT\r%i|\x0c>/K$#8t'
        var_1 = fact_cache_0.__len__()
        dict_0 = {}
        fact_cache_1 = module_0.FactCache(**dict_0)
        var_2 = fact_cache_1.__len__()
        var_3 = fact_cache_1.copy()
        var_4 = fact_cache_1.flush()
        var_5 = fact_cache_1.__getitem__(str_0)
    except BaseException:
        pass