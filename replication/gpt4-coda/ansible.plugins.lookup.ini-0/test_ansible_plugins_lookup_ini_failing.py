# Automatically generated by Pynguin.
import ansible.plugins.lookup.ini as module_0

def test_case_0():
    try:
        tuple_0 = None
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.get_value(tuple_0, tuple_0, lookup_module_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 117
        set_0 = {int_0, int_0, int_0}
        str_0 = 'EVENT_READ'
        str_1 = 'm;FwL\txoi;]O'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_1: str_0}
        lookup_module_0 = module_0.LookupModule(dict_0, **dict_0)
        var_0 = lookup_module_0.get_value(int_0, set_0, int_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        bool_1 = False
        lookup_module_0 = module_0.LookupModule(bool_1)
        var_0 = lookup_module_0.run(bool_0)
    except BaseException:
        pass