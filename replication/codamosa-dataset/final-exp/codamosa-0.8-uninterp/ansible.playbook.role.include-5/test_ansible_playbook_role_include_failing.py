# Automatically generated by Pynguin.
import ansible.playbook.role.include as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        role_include_0 = module_0.RoleInclude()
        float_0 = 1959.3
        var_0 = role_include_0.load(role_include_0, role_include_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 't'
        dict_0 = {str_0: str_0, str_0: str_0}
        set_0 = {str_0}
        dict_1 = {}
        bytes_0 = b''
        role_include_0 = module_0.RoleInclude(dict_1, bytes_0)
        var_0 = role_include_0.load(str_0, dict_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2.0
        bytes_0 = b''
        str_0 = "no root 'plugin' key found, '{0}' is not a valid YAML inventory plugin config file"
        bytes_1 = b'J+,A\xf5\x0f}\xe1\xbdn\xe6?\xa5'
        int_0 = 2423
        list_0 = [bytes_0]
        role_include_0 = module_0.RoleInclude(list_0)
        var_0 = role_include_0.load(str_0, float_0, bytes_1, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -1054
        role_include_0 = module_0.RoleInclude(int_0)
        role_include_1 = module_0.RoleInclude()
        dict_0 = {}
        bool_0 = True
        bytes_0 = b'\x1d'
        var_0 = role_include_0.load(dict_0, dict_0, bool_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = None
        str_0 = '\n|%tE'
        role_include_0 = module_0.RoleInclude(str_0, str_0)
        list_0 = [bool_0, bool_0, bool_0]
        str_1 = ')'
        role_include_1 = module_0.RoleInclude(str_1)
        tuple_0 = (list_0,)
        bytes_0 = b'\xd1|\xce'
        dict_0 = {}
        ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject(**dict_0)
        bytes_1 = b"'\xde\xe5mg\xfb!\xe5"
        dict_1 = {bool_0: str_1, bool_0: list_0, role_include_1: list_0, str_1: str_1}
        role_include_2 = module_0.RoleInclude(bytes_0, dict_1)
        var_0 = role_include_2.load(ansible_base_y_a_m_l_object_0, tuple_0, bytes_1, str_1)
    except BaseException:
        pass