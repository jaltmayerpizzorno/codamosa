# Automatically generated by Pynguin.
import ansible.plugins.lookup.fileglob as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        int_0 = -3520
        str_0 = 'ClH$b9U9*P-h\nYjBv'
        set_0 = {str_0, int_0}
        lookup_module_1 = module_0.LookupModule(set_0)
        var_0 = lookup_module_1.run(str_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 's>'
        var_0 = lookup_module_0.run(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'cached'
        str_1 = '(f?2R/oT\n'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        float_0 = 512.0
        list_0 = [str_1, str_0, float_0, str_0]
        var_0 = lookup_module_0.run(list_0, lookup_module_0)
    except BaseException:
        pass