# Automatically generated by Pynguin.
import ansible.plugins.lookup.ini as module_0

def test_case_0():
    try:
        str_0 = 'O?Rzw)'
        dict_0 = None
        dict_1 = {}
        lookup_module_0 = module_0.LookupModule(**dict_1)
        var_0 = lookup_module_0.get_value(str_0, dict_0, dict_1, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '^V"fb\t"1o}4G'
        str_1 = None
        tuple_0 = (str_0, str_1)
        bool_0 = True
        dict_0 = {}
        lookup_module_0 = module_0.LookupModule(**dict_0)
        var_0 = lookup_module_0.get_value(tuple_0, str_1, str_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Z)`h76>A>Sgk!X\tYR'
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0)
    except BaseException:
        pass