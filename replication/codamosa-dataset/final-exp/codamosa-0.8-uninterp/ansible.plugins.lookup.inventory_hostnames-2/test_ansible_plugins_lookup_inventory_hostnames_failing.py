# Automatically generated by Pynguin.
import ansible.plugins.lookup.inventory_hostnames as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        complex_0 = None
        var_0 = lookup_module_0.run(complex_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'host3'
        var_0 = dict(all=str_0)
        var_1 = dict(groups=var_0)
        str_1 = [var_1, str_0, var_1]
        var_2 = lookup_module_0.run(str_1, var_1)
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = 'host2'
        str_1 = [str_0, str_0, str_0]
        var_0 = dict(all=str_0)
        var_1 = dict(groups=var_0)
        str_2 = 'all:!host2'
        var_2 = lookup_module_0.run(str_2, var_1)
        str_3 = [str_1]
        var_3 = lookup_module_0.run(str_3, var_1)
    except BaseException:
        pass