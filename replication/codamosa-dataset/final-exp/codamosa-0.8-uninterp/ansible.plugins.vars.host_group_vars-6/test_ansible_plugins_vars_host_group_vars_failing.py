# Automatically generated by Pynguin.
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1
import ansible.inventory.group as module_2

def test_case_0():
    try:
        vars_module_0 = module_0.VarsModule()
        dict_0 = {vars_module_0: vars_module_0, vars_module_0: vars_module_0}
        var_0 = vars_module_0.get_vars(dict_0, vars_module_0, vars_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        str_1 = 'aIth_timeout'
        host_0 = module_1.Host(str_1)
        vars_module_0 = module_0.VarsModule()
        str_2 = '/usr/bin/python'
        host_1 = module_1.Host(str_2)
        host_2 = [host_0, host_1]
        var_0 = vars_module_0.get_vars(str_0, str_0, host_2)
        var_1 = host_0.__getstate__()
        str_3 = '\nc_>'
        bytes_0 = b'[h\xf84\xa0\x8f\xbf\xc5g\xdd\x03\xd0'
        group_0 = module_2.Group()
        var_2 = vars_module_0.get_vars(str_3, bytes_0, group_0)
    except BaseException:
        pass