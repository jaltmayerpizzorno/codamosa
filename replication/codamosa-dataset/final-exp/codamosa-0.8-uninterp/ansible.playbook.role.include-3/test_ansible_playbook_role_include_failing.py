# Automatically generated by Pynguin.
import ansible.playbook.role.include as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        bool_0 = None
        bytes_0 = b'\xb1\xb96\xd0\xf5\x80\xaa\xe0J\xd5'
        role_include_0 = module_0.RoleInclude(bytes_0)
        var_0 = role_include_0.load(bool_0, role_include_0, role_include_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "/s'QL0ft34[4iF"
        int_0 = None
        str_1 = '@'
        set_0 = {str_1, str_0, str_1}
        dict_0 = {str_0: str_0, int_0: set_0, int_0: str_1, int_0: str_0}
        bytes_0 = b'\xe9|'
        role_include_0 = module_0.RoleInclude(bytes_0)
        var_0 = role_include_0.load(str_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        bytes_0 = b'\xcf\xbc\xe1\xeb\xca\xb3\x8d"w\x15\xddM\x07\x81\xac\xed\x0c'
        int_0 = -4605
        str_0 = '%s is a Container App role, and should only be installed using Ansible Container'
        bool_1 = False
        dict_0 = {int_0: bytes_0, bytes_0: bytes_0, bool_1: bool_1, int_0: bool_1}
        float_0 = 868.80185
        bytes_1 = b'2'
        role_include_0 = module_0.RoleInclude(bool_0)
        var_0 = role_include_0.load(str_0, dict_0, float_0, bytes_1, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "'M\t7k"
        list_0 = [str_0, str_0, str_0]
        float_0 = 0.0001
        role_include_0 = module_0.RoleInclude(str_0, list_0, float_0)
        float_1 = 892.30152
        role_include_1 = module_0.RoleInclude(str_0)
        role_include_2 = module_0.RoleInclude()
        complex_0 = None
        dict_0 = {role_include_1: float_1}
        var_0 = role_include_0.load(dict_0, role_include_2, complex_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '(yeRti{'
        dict_0 = None
        bool_0 = False
        int_0 = -131
        str_1 = "\n# Test we can logon to 'webservers' and execute python with json lib.\n# ansible webservers -m ping\n\n- name: Example from an Ansible Playbook\n  ansible.builtin.ping:\n\n- name: Induce an exception to see what happens\n  ansible.builtin.ping:\n    data: crash\n"
        tuple_0 = (bool_0, int_0, bool_0, str_1)
        set_0 = {int_0}
        role_include_0 = module_0.RoleInclude(tuple_0, set_0)
        role_include_1 = module_0.RoleInclude()
        float_0 = -2451.22
        list_0 = [set_0, bool_0, float_0, tuple_0]
        role_include_2 = module_0.RoleInclude(list_0, list_0)
        int_1 = None
        role_include_3 = module_0.RoleInclude(dict_0, int_1)
        dict_1 = {}
        ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject(**dict_1)
        ansible_base_y_a_m_l_object_1 = module_1.AnsibleBaseYAMLObject()
        role_include_4 = module_0.RoleInclude(tuple_0, ansible_base_y_a_m_l_object_1)
        var_0 = role_include_4.load(ansible_base_y_a_m_l_object_0, tuple_0, str_0)
    except BaseException:
        pass