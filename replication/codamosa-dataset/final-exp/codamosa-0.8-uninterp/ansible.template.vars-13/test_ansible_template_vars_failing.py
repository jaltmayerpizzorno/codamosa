# Automatically generated by Pynguin.
import ansible.template.vars as module_0

def test_case_0():
    try:
        list_0 = None
        bool_0 = True
        bool_1 = False
        set_0 = {bool_1}
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(bool_1, set_0)
        ansible_j2_vars_1 = module_0.AnsibleJ2Vars(bool_0, ansible_j2_vars_0)
        var_0 = ansible_j2_vars_1.__contains__(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0]
        str_0 = 'min_os_version'
        set_0 = {str_0, str_0, str_0}
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, set_0)
        var_0 = ansible_j2_vars_0.__contains__(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Hosts'
        str_1 = 'o'
        var_0 = None
        str_2 = "8ox'qXP\n<f3BW"
        float_0 = 3614.0
        set_0 = {float_0, var_0, float_0}
        bytes_0 = b'\xcf0-\x15c\xa2\x99\xe0\x82'
        dict_0 = {str_0: var_0, str_2: bytes_0, str_1: var_0}
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(float_0, set_0, dict_0)
        var_1 = ansible_j2_vars_0.__contains__(str_1)
        var_2 = ansible_j2_vars_0.__getitem__(str_2)
        var_3 = ansible_j2_vars_0.__iter__()
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        bool_0 = False
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(tuple_0, bool_0)
        var_0 = ansible_j2_vars_0.__len__()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1282
        set_0 = {int_0, int_0, int_0, int_0}
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(int_0, set_0)
        var_0 = ansible_j2_vars_0.__getitem__(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = None
        bool_0 = True
        set_0 = {bool_0}
        str_0 = 'eFF\n|Y\x0c=:S%\nzd\\=-'
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(set_0, str_0)
        var_0 = ansible_j2_vars_0.add_locals(bytes_0)
        str_1 = '*\r'
        int_0 = -3059
        ansible_j2_vars_1 = module_0.AnsibleJ2Vars(int_0, int_0)
        var_1 = ansible_j2_vars_1.__contains__(str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = "a'v@Y1Q!Z@"
        float_0 = 3603.5814220244492
        set_0 = {float_0, float_0, str_0}
        dict_0 = {str_0: float_0}
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(float_0, set_0, dict_0)
        var_0 = ansible_j2_vars_0.__contains__(str_0)
        var_1 = ansible_j2_vars_0.__getitem__(str_0)
        var_2 = ansible_j2_vars_0.__getitem__(float_0)
    except BaseException:
        pass