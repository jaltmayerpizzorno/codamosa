# Automatically generated by Pynguin.
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1
import ansible.inventory.group as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = 'ansible.parsing.dataloader.DaaLoder'
    vars_module_0 = module_0.VarsModule()
    host_0 = module_1.Host(str_0)
    var_0 = vars_module_0.get_vars(str_0, str_0, host_0)

def test_case_2():
    vars_module_0 = module_0.VarsModule()
    bool_0 = True
    str_0 = 'zmu\n7($(6#El\x0b[R+lDN4'
    list_0 = []
    var_0 = vars_module_0.get_vars(bool_0, str_0, list_0)

def test_case_3():
    bool_0 = False
    str_0 = 'host2'
    int_0 = 1785
    host_0 = module_1.Host(str_0, int_0)
    vars_module_0 = module_0.VarsModule()
    var_0 = vars_module_0.get_vars(str_0, host_0, host_0, bool_0)

def test_case_4():
    str_0 = 'host1'
    host_0 = module_1.Host(str_0)
    str_1 = 'group1'
    group_0 = module_2.Group(str_1)
    var_0 = [host_0, group_0]
    vars_module_0 = module_0.VarsModule()
    var_1 = None
    var_2 = vars_module_0.get_vars(var_1, var_1, group_0)
    var_3 = vars_module_0.get_vars(var_1, var_1, var_0)

def test_case_5():
    bool_0 = True
    str_0 = '/api'
    int_0 = 26
    vars_module_0 = module_0.VarsModule()
    host_0 = module_1.Host(str_0, int_0)
    var_0 = vars_module_0.get_vars(vars_module_0, str_0, host_0, bool_0)