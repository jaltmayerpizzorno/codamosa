# Automatically generated by Pynguin.
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        vars_module_0 = module_0.VarsModule()
        set_0 = set()
        list_0 = [set_0]
        var_0 = vars_module_0.get_vars(set_0, list_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        vars_module_0 = module_0.VarsModule()
        set_0 = set()
        list_0 = [set_0]
        var_0 = vars_module_0.get_vars(list_0, list_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        vars_module_0 = module_0.VarsModule()
        bytes_0 = b'\xcf\x90g\xa0\xa8`\xb4\x85U\x11h\x0eg4\xbdB\x19\x85\xa5'
        float_0 = 3085.8
        host_0 = module_1.Host()
        var_0 = vars_module_0.get_vars(bytes_0, float_0, host_0)
    except BaseException:
        pass