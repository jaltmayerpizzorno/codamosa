# Automatically generated by Pynguin.
import ansible.template.vars as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'test1'
    str_1 = {str_0: str_0}
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_1, str_0, str_1)

def test_case_2():
    bytes_0 = b'\xb2\xef'
    str_0 = 'lj/]laN'
    dict_0 = {bytes_0: str_0, str_0: bytes_0, bytes_0: str_0}
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(dict_0, str_0, dict_0)
    var_0 = ansible_j2_vars_0.__getitem__(str_0)

def test_case_3():
    bytes_0 = b'\xb2\xef'
    str_0 = 'lj/]laN'
    dict_0 = {bytes_0: str_0, str_0: bytes_0, bytes_0: str_0}
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(dict_0, str_0, dict_0)
    var_0 = ansible_j2_vars_0.__contains__(bytes_0)
    var_1 = ansible_j2_vars_0.__getitem__(str_0)