# Automatically generated by Pynguin.
import ansible.plugins.lookup.first_found as module_0

def test_case_0():
    try:
        float_0 = -501.47
        list_0 = [float_0]
        float_1 = 537.05596
        lookup_module_0 = module_0.LookupModule(float_1)
        var_0 = lookup_module_0.run(list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        dict_1 = {}
        lookup_module_0 = module_0.LookupModule()
        tuple_0 = ()
        list_0 = [dict_0, tuple_0]
        tuple_1 = (tuple_0, list_0)
        var_0 = lookup_module_0.run(tuple_1, dict_1)
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        int_0 = 6
        str_0 = '(B,+,tQ%o '
        var_0 = lookup_module_0.run(int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'ZDw9\\0eBKit"z3:FIX:'
        float_0 = -2375.0
        var_0 = lookup_module_0.run(str_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        int_0 = -328
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(dict_0, int_0)
    except BaseException:
        pass