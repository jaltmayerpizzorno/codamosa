# Automatically generated by Pynguin.
import ansible.template.vars as module_0

def test_case_0():
    try:
        bool_0 = False
        str_0 = '%/\x0c-'
        bytes_0 = b'\x00\x08i.\x95\x96Z\x1a\xcezT\x05+\x89\xc2\xe2_'
        list_0 = [str_0, bytes_0, str_0]
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, bytes_0, list_0)
        var_0 = ansible_j2_vars_0.__contains__(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        int_0 = -1070
        list_0 = [int_0, int_0, int_0]
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(dict_0, list_0)
        var_0 = ansible_j2_vars_0.__iter__()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "{N}\x0c'\x0bK)NST(Ow"
        list_0 = [str_0, str_0, str_0, str_0]
        bytes_0 = b'#\xf7\xe2\xb1\x07o\x99\x9d\x80|\xc6+\x8fW!'
        set_0 = {bytes_0, bytes_0, str_0, str_0}
        dict_0 = {}
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(list_0, set_0, dict_0)
        var_0 = ansible_j2_vars_0.__len__()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        str_0 = 'n'
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(bool_0, str_0)
        var_0 = ansible_j2_vars_0.__getitem__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\'Z3fHDw\x0b;"|%Z5()y:\nO'
        str_1 = 'pTr-r\r7|FIi'
        list_0 = [str_0, str_0, str_1, str_0]
        bytes_0 = b''
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_1, bytes_0)
        var_0 = ansible_j2_vars_0.add_locals(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = None
        str_0 = 'g_var_a'
        str_1 = 'g_var_b'
        int_0 = 1
        int_1 = 2
        int_2 = {str_0: int_0, str_1: int_1}
        str_2 = 'l_var_a'
        str_3 = 'l_var_b'
        int_3 = {str_2: int_0, str_3: int_1}
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(var_0, int_2, int_3)
        var_1 = len(ansible_j2_vars_0)
    except BaseException:
        pass