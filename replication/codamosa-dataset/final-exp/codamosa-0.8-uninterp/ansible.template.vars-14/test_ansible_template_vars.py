# Automatically generated by Pynguin.
import ansible.template.vars as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\x0cs<-q'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    tuple_0 = ()
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(tuple_0, tuple_0)
    var_0 = ansible_j2_vars_0.add_locals(dict_0)

def test_case_2():
    int_0 = 663
    int_1 = -590
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(int_0, int_1)

def test_case_3():
    str_0 = '$'
    str_1 = 'BQr$$'
    str_2 = '%'
    bool_0 = True
    dict_0 = {str_1: str_0, str_2: bool_0}
    int_0 = -3211
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(dict_0, int_0, dict_0)
    var_0 = ansible_j2_vars_0.__getitem__(str_2)
    var_1 = ansible_j2_vars_0.__contains__(str_1)

def test_case_4():
    str_0 = 'l_foo'
    str_1 = 'bar'
    str_2 = {str_0: str_1}
    str_3 = 'helloworld'
    str_4 = 'g_foo'
    str_5 = {str_4: str_1}
    ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_3, str_5, str_2)