# Automatically generated by Pynguin.
import ansible.vars.hostvars as module_0

def test_case_0():
    pass

def test_case_1():
    set_0 = set()
    int_0 = 887
    bool_0 = False
    host_vars_vars_0 = module_0.HostVarsVars(int_0, bool_0)
    host_vars_0 = module_0.HostVars(set_0, host_vars_vars_0, host_vars_vars_0)
    var_0 = host_vars_0.__setstate__(set_0)

def test_case_2():
    float_0 = -959.36
    str_0 = '\x0c'
    list_0 = [float_0, str_0, str_0, str_0]
    set_0 = set()
    int_0 = 892
    bool_0 = True
    host_vars_vars_0 = module_0.HostVarsVars(int_0, bool_0)
    host_vars_0 = module_0.HostVars(set_0, host_vars_vars_0, host_vars_vars_0)
    var_0 = host_vars_0.set_inventory(list_0)

def test_case_3():
    var_0 = None
    str_0 = 'foo'
    str_1 = 'baz'
    str_2 = 'nested'
    str_3 = 'bar'
    str_4 = 'qux'
    str_5 = 'key'
    str_6 = {str_5: str_1}
    str_7 = {str_0: str_3, str_1: str_4, str_2: str_6}
    host_vars_vars_0 = module_0.HostVarsVars(str_7, var_0)
    var_1 = iter(host_vars_vars_0)
    var_2 = list(var_1)
    var_3 = len(var_2)