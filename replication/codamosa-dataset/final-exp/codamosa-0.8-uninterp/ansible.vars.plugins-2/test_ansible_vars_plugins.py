# Automatically generated by Pynguin.
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    int_0 = 265
    list_0 = []
    set_0 = {int_0}
    var_0 = module_0.get_vars_from_path(bool_0, int_0, list_0, set_0)

def test_case_2():
    set_0 = set()
    var_0 = module_0.get_vars_from_inventory_sources(set_0, set_0, set_0, set_0)

def test_case_3():
    str_0 = ''
    host_0 = module_1.Host(str_0)
    str_1 = '/tmp/test.yml'
    str_2 = [str_1]
    host_1 = [host_0]
    var_0 = None
    str_3 = 'inventory'
    var_1 = module_0.get_vars_from_inventory_sources(var_0, str_2, host_1, str_3)