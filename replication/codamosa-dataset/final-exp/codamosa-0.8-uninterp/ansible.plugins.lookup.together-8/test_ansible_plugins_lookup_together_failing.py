# Automatically generated by Pynguin.
import ansible.plugins.lookup.together as module_0

def test_case_0():
    try:
        bool_0 = True
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'kLP4.P?)nyB:SVjF,QOM'
        list_0 = [str_0, str_0, str_0, str_0]
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        dict_0 = {}
        var_0 = lookup_module_0.run(dict_0)
    except BaseException:
        pass