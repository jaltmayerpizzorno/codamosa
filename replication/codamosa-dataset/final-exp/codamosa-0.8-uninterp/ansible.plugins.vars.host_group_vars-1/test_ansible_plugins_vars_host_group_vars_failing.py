# Automatically generated by Pynguin.
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1
import ansible.inventory.group as module_2

def test_case_0():
    try:
        vars_module_0 = module_0.VarsModule()
        float_0 = 1000.0
        var_0 = vars_module_0.get_vars(float_0, float_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        vars_module_0 = module_0.VarsModule()
        int_0 = -139
        set_0 = {int_0, int_0}
        bool_0 = True
        list_0 = [vars_module_0, vars_module_0, set_0, bool_0]
        var_0 = vars_module_0.get_vars(int_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        vars_module_0 = module_0.VarsModule()
        str_0 = 'test_host'
        host_0 = module_1.Host(str_0)
        list_0 = [str_0, host_0, str_0, str_0]
        float_0 = 1.5
        str_1 = 'r+zO?8uknDF%'
        group_0 = module_2.Group(str_1)
        bool_0 = False
        var_0 = vars_module_0.get_vars(list_0, float_0, group_0, bool_0)
        group_1 = module_2.Group()
        int_0 = 4518
        str_2 = 'z=7\x0b_02fBKDpc6\t_'
        var_1 = vars_module_0.get_vars(int_0, str_2, vars_module_0)
    except BaseException:
        pass