# Automatically generated by Pynguin.
import ansible.plugins.lookup.first_found as module_0

def test_case_0():
    try:
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        set_0 = {lookup_module_0}
        lookup_module_1 = module_0.LookupModule()
        var_0 = lookup_module_1.run(set_0, lookup_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xdd\xaf7C=e\xeb\x85\xcd\x1dGh\xe4\xfd\x0c[Y=f\xcf'
        float_0 = -410.374
        list_0 = [bytes_0, float_0]
        str_0 = 'e'
        dict_0 = {str_0: bytes_0, str_0: float_0}
        dict_1 = {str_0: str_0, str_0: str_0}
        lookup_module_0 = module_0.LookupModule(dict_1)
        var_0 = lookup_module_0.run(list_0, str_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(set_0, lookup_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        lookup_module_1 = module_0.LookupModule()
        str_0 = '6<\x0c<jv\tHOzm'
        var_0 = lookup_module_0.run(str_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        tuple_0 = (dict_0,)
        float_0 = 2069.121
        set_0 = None
        tuple_1 = (tuple_0, float_0, set_0)
        bool_0 = True
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(tuple_1, bool_0, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        str_0 = 'jwP&#fL8Wg{'
        bytes_0 = b''
        set_0 = {bytes_0, bytes_0, str_0, lookup_module_0}
        int_0 = None
        var_0 = lookup_module_0.run(set_0, int_0)
    except BaseException:
        pass