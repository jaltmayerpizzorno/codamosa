# Automatically generated by Pynguin.
import ansible.vars.hostvars as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ';nS7'
    set_0 = set()
    list_0 = [str_0, str_0, str_0, set_0]
    host_vars_vars_0 = module_0.HostVarsVars(list_0, set_0)
    host_vars_0 = module_0.HostVars(list_0, host_vars_vars_0, str_0)
    var_0 = host_vars_0.__setstate__(set_0)

def test_case_2():
    bool_0 = True
    tuple_0 = None
    int_0 = 920
    host_vars_vars_0 = module_0.HostVarsVars(tuple_0, int_0)
    host_vars_0 = module_0.HostVars(tuple_0, host_vars_vars_0, tuple_0)
    var_0 = host_vars_0.__deepcopy__(bool_0)
    float_0 = 60.0
    dict_0 = {float_0: float_0, float_0: float_0}
    var_1 = host_vars_0.__setstate__(dict_0)

def test_case_3():
    host_vars_0 = None
    float_0 = -1548.803088
    host_vars_vars_0 = module_0.HostVarsVars(host_vars_0, float_0)

def test_case_4():
    str_0 = 'bar'
    str_1 = '{{ not_defined }}'
    str_2 = {str_0: str_1}
    var_0 = None
    host_vars_vars_0 = module_0.HostVarsVars(str_2, var_0)
    var_1 = host_vars_vars_0.get(str_0)
    str_3 = {str_0: str_1}
    host_vars_vars_1 = module_0.HostVarsVars(str_3, var_0)