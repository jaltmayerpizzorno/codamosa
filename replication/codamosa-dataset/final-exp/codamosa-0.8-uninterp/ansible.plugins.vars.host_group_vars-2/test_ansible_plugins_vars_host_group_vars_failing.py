# Automatically generated by Pynguin.
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.group as module_1
import ansible.inventory.host as module_2

def test_case_0():
    try:
        vars_module_0 = module_0.VarsModule()
        var_0 = None
        var_1 = vars_module_0.get_vars(var_0, var_0, var_0, var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        vars_module_0 = module_0.VarsModule()
        vars_module_1 = module_0.VarsModule()
        dict_0 = {}
        dict_1 = {}
        list_0 = []
        str_0 = 'rhel'
        var_0 = vars_module_1.get_vars(dict_0, dict_1, list_0, str_0)
        vars_module_2 = module_0.VarsModule()
        int_0 = 49
        bool_0 = True
        str_1 = '\n        Initializes this object with a valid Templar() object, as\n        well as several dictionaries of variables representing\n        different scopes (in jinja2 terminology).\n        '
        tuple_0 = (int_0, bool_0, str_1)
        var_1 = vars_module_1.get_vars(tuple_0, bool_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        vars_module_0 = None
        list_0 = [vars_module_0, vars_module_0]
        vars_module_1 = module_0.VarsModule()
        list_1 = [list_0, vars_module_1]
        str_0 = 'QFx[.ON\n"(yk#Z'
        group_0 = module_1.Group()
        vars_module_2 = module_0.VarsModule()
        var_0 = vars_module_2.get_vars(list_1, str_0, group_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/Ru'
        host_0 = module_2.Host(str_0)
        vars_module_0 = module_0.VarsModule()
        float_0 = -119.0
        vars_module_1 = module_0.VarsModule()
        list_0 = [host_0, host_0, host_0]
        str_1 = 'EhQ3'
        var_0 = vars_module_1.get_vars(list_0, str_1, host_0)
        vars_module_2 = module_0.VarsModule()
        float_1 = 2647.44014
        int_0 = -2308
        list_1 = None
        dict_0 = {list_1: host_0, int_0: float_1, float_0: list_0, vars_module_1: list_1}
        var_1 = vars_module_2.get_vars(float_1, host_0, dict_0)
    except BaseException:
        pass