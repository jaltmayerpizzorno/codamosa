# Automatically generated by Pynguin.
import ansible.plugins.lookup.random_choice as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(lookup_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -1610.317
        tuple_0 = None
        str_0 = '<'
        dict_0 = {str_0: float_0}
        lookup_module_0 = module_0.LookupModule(dict_0)
        var_0 = lookup_module_0.run(tuple_0)
        int_0 = 528
        str_1 = "Y^\tohMo,@'U80fYC9`i"
        dict_1 = {str_1: str_1}
        lookup_module_1 = module_0.LookupModule(**dict_1)
        var_1 = lookup_module_1.run(float_0, int_0, **dict_0)
    except BaseException:
        pass