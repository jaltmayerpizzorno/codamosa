# Automatically generated by Pynguin.
import ansible.plugins.lookup.first_found as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        tuple_0 = ()
        set_0 = {tuple_0}
        str_0 = 'uTCVt?sC{vl6oA'
        var_0 = lookup_module_0.run(set_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        list_0 = []
        var_0 = lookup_module_0.run(list_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        bytes_0 = b'\xf8\xab~\x00\xa2\xab\xa1\xea\x83\x8a'
        list_0 = [bool_0, bytes_0]
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(bytes_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        str_0 = 'k_w{Oz'
        list_0 = [dict_0, str_0, dict_0]
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0]
        float_0 = -231.09
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(list_0, float_0)
    except BaseException:
        pass