# Automatically generated by Pynguin.
import ansible.template.vars as module_0

def test_case_0():
    try:
        bytes_0 = b'\xfd\x03\x00\x85\xaa\xfd\xaczH\xa1$$\xa6\xbc\x822;'
        str_0 = "Y'>}"
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, str_0, str_0)
        var_0 = ansible_j2_vars_0.__contains__(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'makecache'
        bytes_0 = b'\x8a\xa1'
        str_1 = '*&5j%y2IX#qs,m'
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, bytes_0, str_1)
        var_0 = ansible_j2_vars_0.__iter__()
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 311.364411
        str_0 = 'tZZa%hJ1'
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(float_0, str_0)
        var_0 = ansible_j2_vars_0.__len__()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -1417
        bool_0 = False
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(int_0, bool_0)
        var_0 = ansible_j2_vars_0.__getitem__(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'jP '
        str_1 = 'The collection(s) name or path/url to a tar.gz collection artifact. This is mutually exclusive with --requirements-file.'
        bool_0 = False
        set_0 = {str_1, bool_0}
        float_0 = 3021.59
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_1, set_0, float_0)
        var_0 = ansible_j2_vars_0.add_locals(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'7>\n'
        int_0 = 4787
        float_0 = None
        dict_0 = {int_0: int_0, int_0: int_0, int_0: bytes_0, bytes_0: bytes_0}
        bool_0 = False
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(dict_0, bool_0)
        var_0 = ansible_j2_vars_0.add_locals(float_0)
        bytes_1 = b'M\xbccU\xe5\xc6\x7fo'
        tuple_0 = (int_0, bytes_1)
        str_0 = ''
        ansible_j2_vars_1 = module_0.AnsibleJ2Vars(tuple_0, str_0)
        var_1 = ansible_j2_vars_1.__getitem__(bytes_0)
    except BaseException:
        pass