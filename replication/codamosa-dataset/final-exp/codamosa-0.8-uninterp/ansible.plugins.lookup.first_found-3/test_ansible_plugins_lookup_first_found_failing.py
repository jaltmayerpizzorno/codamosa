# Automatically generated by Pynguin.
import ansible.plugins.lookup.first_found as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        dict_0 = {lookup_module_0: lookup_module_0, lookup_module_0: lookup_module_0}
        set_0 = None
        var_0 = lookup_module_0.run(dict_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        dict_0 = {}
        lookup_module_1 = module_0.LookupModule(dict_0, **dict_0)
        int_0 = 19
        tuple_0 = (int_0,)
        bool_0 = True
        tuple_1 = (tuple_0, dict_0, lookup_module_1, bool_0)
        var_0 = lookup_module_0.run(tuple_1, lookup_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b''
        dict_0 = {}
        dict_1 = {}
        bytes_1 = b'\xb5b\xa2\xe5\xc3\x8f\xa9i\xbc'
        lookup_module_0 = module_0.LookupModule(bytes_1)
        lookup_module_1 = module_0.LookupModule(dict_1, **dict_1)
        float_0 = 0.5
        lookup_module_2 = module_0.LookupModule(lookup_module_1, float_0)
        complex_0 = None
        list_0 = [float_0, dict_1, dict_0]
        tuple_0 = (bytes_0, complex_0, list_0)
        var_0 = lookup_module_1.run(tuple_0, complex_0, **dict_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x95\x92\x97\xaa"u\xcf\x8a\xe6N9'
        dict_0 = {bytes_0: bytes_0}
        list_0 = [dict_0, bytes_0, bytes_0]
        tuple_0 = (list_0, dict_0)
        int_0 = 2217
        str_0 = 'o8jn]wSmN'
        dict_1 = {str_0: str_0, str_0: str_0, str_0: int_0, str_0: str_0}
        lookup_module_0 = module_0.LookupModule(int_0, **dict_1)
        var_0 = lookup_module_0.run(tuple_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b''
        str_0 = 'HP nPar'
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(bytes_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'L"j5\n"(GhI\'0"=KB'
        int_0 = 3600
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0, int_0)
    except BaseException:
        pass