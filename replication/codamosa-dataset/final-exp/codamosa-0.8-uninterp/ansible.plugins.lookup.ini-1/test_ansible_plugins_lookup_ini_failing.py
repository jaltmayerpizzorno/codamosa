# Automatically generated by Pynguin.
import ansible.plugins.lookup.ini as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        set_0 = {lookup_module_0}
        bool_0 = False
        var_0 = lookup_module_0.get_value(set_0, lookup_module_0, lookup_module_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = None
        list_0 = [lookup_module_0, lookup_module_0, lookup_module_0, lookup_module_0]
        bool_0 = True
        str_0 = 'H'
        lookup_module_1 = module_0.LookupModule()
        tuple_0 = (lookup_module_1,)
        lookup_module_2 = module_0.LookupModule(tuple_0)
        var_0 = lookup_module_2.get_value(lookup_module_0, list_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ' run a command on the local host '
        dict_0 = {str_0: str_0, str_0: str_0}
        bool_0 = None
        list_0 = [bool_0]
        list_1 = [list_0, bool_0, list_0, bool_0]
        str_1 = '%s/%s.override'
        dict_1 = {str_1: list_0}
        lookup_module_0 = module_0.LookupModule(list_1, bool_0, **dict_1)
        var_0 = lookup_module_0.run(dict_0, **dict_0)
    except BaseException:
        pass