# Automatically generated by Pynguin.
import ansible.plugins.lookup.sequence as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'et\\xD hfPnPYk'
        var_0 = lookup_module_0.run(str_0, lookup_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'w\nR:Iv6E,'
        var_0 = lookup_module_0.run(str_0, lookup_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        str_0 = 'Y.:7oj~E\t|'
        lookup_module_0 = module_0.LookupModule(str_0)
        var_0 = lookup_module_0.parse_kv_args(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '1kIuw8<|:"%.M\x0bcg>'
        var_0 = lookup_module_0.run(str_0, lookup_module_0)
    except BaseException:
        pass

def test_case_4():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.reset()
        var_1 = lookup_module_0.sanity_check()
    except BaseException:
        pass

def test_case_5():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '1kRuw8<|:"%.M\x0bAg>'
        bytes_0 = b'\x14\xff{\xe6\xb7'
        var_0 = lookup_module_0.run(bytes_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '7)M} m:;YU;.'
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.parse_simple_args(str_0)
        lookup_module_1 = module_0.LookupModule()
        list_0 = []
        var_1 = lookup_module_0.run(list_0, lookup_module_1)
        str_1 = 'MIME-Version'
        str_2 = 'Soft Errors'
        dict_0 = {str_1: lookup_module_1, str_1: str_1, str_2: str_1, str_0: str_2}
        int_0 = 211
        str_3 = 'et\\xD hfPnPYk'
        tuple_0 = (int_0, lookup_module_1, str_3)
        var_2 = lookup_module_0.run(dict_0, tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'end'
        str_1 = 'stride'
        str_2 = 'format'
        lookup_module_1 = module_0.LookupModule()
        str_3 = '0'
        str_4 = '10'
        str_5 = '2'
        str_6 = '%s'
        str_7 = {str_3: str_3, str_0: str_4, str_1: str_5, str_2: str_6}
        var_0 = lookup_module_0.parse_kv_args(str_7)
    except BaseException:
        pass

def test_case_8():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'start'
        str_1 = 'end'
        str_2 = 'stride'
        str_3 = 'format'
        str_4 = '0'
        str_5 = '2'
        str_6 = '%s'
        str_7 = {str_0: str_4, str_1: str_3, str_2: str_5, str_3: str_6}
        var_0 = lookup_module_0.parse_kv_args(str_7)
    except BaseException:
        pass

def test_case_9():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'Q]'
        int_0 = -825
        dict_0 = {str_0: str_0}
        lookup_module_1 = module_0.LookupModule(str_0, int_0, **dict_0)
        str_1 = '110'
        var_0 = lookup_module_0.parse_simple_args(str_1)
        list_0 = [str_1, str_1, str_1, lookup_module_0]
        tuple_0 = (list_0,)
        var_1 = lookup_module_0.run(str_1, tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '1-1/0'
        list_0 = [str_0, str_0, str_0, lookup_module_0]
        float_0 = 0.001
        var_0 = lookup_module_0.run(list_0, float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '1-1/b'
        var_0 = lookup_module_0.parse_simple_args(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '5'
        str_1 = '5-8'
        str_2 = '2-10/2'
        str_3 = '4:host%02d'
        str_4 = 'start=5 end=11 stride=2 format=0x%02x'
        str_5 = 'count=5'
        str_6 = 'start=0x0f00 count=4 format=%04x'
        str_7 = 'start=0 count=5 stride=2'
        str_8 = 'start=1 count=5 stride=2'
        str_9 = 'start=1 end=10'
        str_10 = '1-15/-1'
        str_11 = [str_0, str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8, str_9, str_10]
        lookup_module_0 = module_0.LookupModule()
        var_0 = None
        var_1 = lookup_module_0.run(str_11, var_0)
    except BaseException:
        pass