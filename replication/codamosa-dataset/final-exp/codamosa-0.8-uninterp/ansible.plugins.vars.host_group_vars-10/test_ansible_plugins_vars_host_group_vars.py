# Automatically generated by Pynguin.
import ansible.inventory.group as module_0
import ansible.plugins.vars.host_group_vars as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'test_group'
    group_0 = module_0.Group(str_0)
    vars_module_0 = module_1.VarsModule()
    var_0 = vars_module_0.get_vars(str_0, str_0, group_0)

def test_case_2():
    str_0 = '/sys/devices/virtual/dmi/id/chassis_type'
    group_0 = module_0.Group(str_0)
    vars_module_0 = module_1.VarsModule()
    var_0 = vars_module_0.get_vars(str_0, str_0, group_0)