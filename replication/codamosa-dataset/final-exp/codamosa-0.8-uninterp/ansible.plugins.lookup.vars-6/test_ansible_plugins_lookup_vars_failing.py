# Automatically generated by Pynguin.
import ansible.plugins.lookup.vars as module_0

def test_case_0():
    try:
        list_0 = []
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        list_0 = [int_0, int_0, int_0]
        list_1 = [list_0, list_0, int_0]
        str_0 = 'RN<vgo+MP[a=z+F;ojn}'
        dict_0 = {}
        bool_0 = None
        tuple_0 = (str_0, dict_0, bool_0, str_0)
        lookup_module_0 = module_0.LookupModule(tuple_0)
        set_0 = {lookup_module_0}
        lookup_module_1 = module_0.LookupModule(set_0)
        var_0 = lookup_module_1.run(list_1, list_0)
    except BaseException:
        pass