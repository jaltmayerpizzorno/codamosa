# Automatically generated by Pynguin.
import ansible.plugins.lookup.ini as module_0

def test_case_0():
    try:
        set_0 = None
        str_0 = "^l'(A_"
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.get_value(set_0, str_0, lookup_module_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '@h]4)Zo_(\r@yk}](v'
        set_0 = {str_0, str_0}
        list_0 = [str_0, str_0, set_0]
        int_0 = -1858
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        var_0 = lookup_module_0.get_value(str_0, list_0, int_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -2147
        str_0 = 'sx#}BvzL%RczIUxf'
        str_1 = ''
        dict_0 = {str_0: str_0, str_1: str_0, str_1: str_1}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(int_0, **dict_0)
    except BaseException:
        pass