# Automatically generated by Pynguin.
import ansible.inventory.group as module_0
import ansible.plugins.vars.host_group_vars as module_1
import ansible.inventory.host as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = 'prodbox0'
    group_0 = module_0.Group(str_0)
    vars_module_0 = module_1.VarsModule()
    var_0 = vars_module_0.get_vars(str_0, str_0, group_0)

def test_case_2():
    str_0 = 'devbox01'
    host_0 = module_2.Host(str_0)
    group_0 = module_0.Group(str_0)
    var_0 = [host_0, host_0, host_0, group_0, group_0, group_0]
    vars_module_0 = module_1.VarsModule()
    var_1 = vars_module_0.get_vars(str_0, str_0, var_0)

def test_case_3():
    str_0 = '/tmp/inventory'
    host_0 = module_2.Host(str_0)
    str_1 = 'prodbox01'
    group_0 = module_0.Group(str_1)
    var_0 = [host_0, host_0, host_0, group_0, group_0, group_0]
    vars_module_0 = module_1.VarsModule()
    var_1 = vars_module_0.get_vars(str_0, str_0, var_0)

def test_case_4():
    str_0 = '/tmp/inventory'
    host_0 = module_2.Host(str_0)
    str_1 = 'prodbox01'
    host_1 = module_2.Host(str_1)
    str_2 = 'devs'
    group_0 = module_0.Group(str_2)
    str_3 = 'prods'
    group_1 = module_0.Group(str_3)
    vars_module_0 = module_1.VarsModule()
    float_0 = 116.9
    int_0 = 2452
    int_1 = None
    var_0 = vars_module_0.get_vars(float_0, int_0, host_1, int_1)