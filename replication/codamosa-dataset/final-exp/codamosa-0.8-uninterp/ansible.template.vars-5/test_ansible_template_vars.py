# Automatically generated by Pynguin.
import ansible.template.vars as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'global'
    var_0 = dict(lcl=str_0)
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, var_0, var_0)

def test_case_2():
    list_0 = None
    float_0 = 910.90845
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(list_0, float_0)

def test_case_3():
    str_0 = '[y'
    str_1 = '#K\\1ylR?'
    int_0 = 2004
    list_0 = [str_0, str_0, str_0]
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_1, int_0, list_0)
    var_0 = ansible_j2_vars_0.add_locals(list_0)