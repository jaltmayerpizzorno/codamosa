# Automatically generated by Pynguin.
import ansible.template.vars as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'key'
    str_1 = {str_0: str_0}
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_1, str_0, str_1)

def test_case_2():
    float_0 = 1373.0
    int_0 = 1024
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(float_0, int_0)

def test_case_3():
    bool_0 = True
    int_0 = -2403
    str_0 = "uGj{!2f'!}2_e!1"
    str_1 = 'sha256:%s'
    list_0 = None
    bytes_0 = b'\x83'
    dict_0 = {str_1: bool_0, str_0: int_0}
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(int_0, bytes_0, dict_0)
    var_0 = ansible_j2_vars_0.add_locals(list_0)
    var_1 = ansible_j2_vars_0.__getitem__(str_1)