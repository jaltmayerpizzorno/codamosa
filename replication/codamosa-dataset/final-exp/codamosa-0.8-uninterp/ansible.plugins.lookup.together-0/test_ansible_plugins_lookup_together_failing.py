# Automatically generated by Pynguin.
import ansible.plugins.lookup.together as module_0

def test_case_0():
    try:
        int_0 = -4457
        lookup_module_0 = module_0.LookupModule(int_0)
        var_0 = lookup_module_0.run(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0]
        list_1 = [dict_0, list_0, dict_0, list_0]
        str_0 = '~\t24_g DA3[y%o3l1'
        str_1 = ' $Ao,Q'
        dict_1 = {str_0: str_0, str_1: str_0}
        lookup_module_0 = module_0.LookupModule(**dict_1)
        var_0 = lookup_module_0.run(list_1, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b''
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(bytes_0)
    except BaseException:
        pass