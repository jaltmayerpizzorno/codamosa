# Automatically generated by Pynguin.
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1
import ansible.inventory.group as module_2

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    str_0 = 'reconnection_backoff'
    vars_module_0 = module_0.VarsModule()
    str_1 = 'SXvJt4yHq\n>.}$\r/6]j'
    host_0 = module_1.Host(str_1)
    set_0 = None
    var_0 = vars_module_0.get_vars(list_0, str_0, host_0, set_0)
    var_1 = vars_module_0.get_vars(set_0, vars_module_0, list_0)
    group_0 = module_2.Group()

def test_case_2():
    str_0 = 'testhos\x0ct'
    group_0 = module_2.Group(str_0)
    vars_module_0 = module_0.VarsModule()
    var_0 = vars_module_0.get_vars(str_0, str_0, group_0)

def test_case_3():
    str_0 = '/etc/rc.conf.d/hostname'
    group_0 = module_2.Group(str_0)
    vars_module_0 = module_0.VarsModule()
    var_0 = vars_module_0.get_vars(str_0, str_0, group_0)