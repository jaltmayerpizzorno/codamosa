# Automatically generated by Pynguin.
import ansible.playbook.role.include as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        bool_0 = True
        role_include_0 = module_0.RoleInclude(bool_0)
        var_0 = role_include_0.load(role_include_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject()
        str_0 = 'failed to find the executable specified %s. Please verify if the executable exists and re-try.'
        list_0 = [str_0]
        role_include_0 = module_0.RoleInclude()
        var_0 = role_include_0.load(ansible_base_y_a_m_l_object_0, str_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ge_distribuion'
        str_1 = 'R'
        list_0 = []
        bytes_0 = b'\xbb\xa9yy\xc2'
        str_2 = '$LpB>yY!E8&>O'
        dict_0 = {str_2: str_0, str_2: str_0}
        role_include_0 = module_0.RoleInclude(str_2, dict_0)
        var_0 = role_include_0.load(str_1, list_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '!^1*93BuI^vms0L\r'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        role_include_0 = module_0.RoleInclude()
        var_0 = role_include_0.load(dict_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 152
        dict_0 = {int_0: int_0}
        role_include_0 = module_0.RoleInclude()
        float_0 = -1728.80881
        tuple_0 = (dict_0, role_include_0, float_0, int_0)
        role_include_1 = module_0.RoleInclude(int_0, tuple_0)
        float_1 = 1802.2
        bool_0 = True
        role_include_2 = module_0.RoleInclude()
        bytes_0 = b'\xa2\xd1C\x82\x00,\xb8\xf5~\xe5'
        role_include_3 = module_0.RoleInclude(role_include_2, float_1, bytes_0)
        list_0 = None
        tuple_1 = (float_1, bool_0, list_0)
        dict_1 = {list_0: list_0, bool_0: list_0, float_1: tuple_1}
        int_1 = -506
        role_include_4 = module_0.RoleInclude(tuple_1, dict_1, int_1)
        role_include_5 = module_0.RoleInclude(list_0)
        bytes_1 = b'j\x87\xff'
        str_0 = 'H8,)'
        set_0 = {float_0, bytes_1}
        var_0 = role_include_2.load(str_0, set_0, float_1, dict_1)
    except BaseException:
        pass