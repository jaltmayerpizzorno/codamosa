# Automatically generated by Pynguin.
import ansible.playbook.role.include as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        str_0 = '~%+^/f#'
        set_0 = {str_0, str_0, str_0}
        role_include_0 = module_0.RoleInclude()
        var_0 = role_include_0.load(str_0, str_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xc2Q\x90\xdd\x16'
        int_0 = -1524
        role_include_0 = module_0.RoleInclude(int_0)
        var_0 = role_include_0.load(role_include_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2.023377518419771
        role_include_0 = module_0.RoleInclude(float_0)
        ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject()
        var_0 = role_include_0.load(ansible_base_y_a_m_l_object_0, float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        float_0 = -5990.6
        str_0 = 'ansible-core 2.13 will require Python 2.7 or newer on the target. Current version: %s'
        str_1 = '6kQW&'
        role_include_0 = module_0.RoleInclude()
        role_include_1 = module_0.RoleInclude(str_1, role_include_0)
        var_0 = role_include_1.load(dict_0, float_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\x0c\x0b,r7v*woC)m6Fc0\x0c '
        bytes_0 = None
        float_0 = -108.115248
        role_include_0 = module_0.RoleInclude(float_0)
        var_0 = role_include_0.load(str_0, bytes_0)
    except BaseException:
        pass