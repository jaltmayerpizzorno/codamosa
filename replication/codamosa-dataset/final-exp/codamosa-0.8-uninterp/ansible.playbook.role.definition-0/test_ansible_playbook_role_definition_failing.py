# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        float_0 = 3733.4
        float_1 = -1666.0
        list_0 = [float_1, float_1, float_1, float_1]
        role_definition_0 = module_0.RoleDefinition(float_1, list_0)
        var_0 = role_definition_0.load(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = None
        role_definition_0 = module_0.RoleDefinition(var_0)
        var_1 = role_definition_0.preprocess_data(role_definition_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'X-W'
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        str_0 = 'V.~O8.9 FbM\tGW~'
        role_definition_0 = module_0.RoleDefinition(str_0)
        var_0 = role_definition_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = None
        role_definition_0 = module_0.RoleDefinition(var_0)
        var_1 = {}
        var_2 = role_definition_0.preprocess_data(var_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'Z_\x07\x1al\x96_'
        role_definition_0 = module_0.RoleDefinition(bytes_0, bytes_0)
        var_0 = role_definition_0.get_role_params()
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        float_0 = 0.2
        bytes_0 = None
        int_0 = 15
        role_definition_0 = module_0.RoleDefinition(float_0, bytes_0, int_0)
        var_0 = role_definition_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'V.~O8.9 FbM\tGW~'
        role_definition_0 = module_0.RoleDefinition(str_0)
        ansible_mapping_0 = module_1.AnsibleMapping()
        var_0 = role_definition_0.preprocess_data(ansible_mapping_0)
    except BaseException:
        pass

def test_case_8():
    try:
        role_definition_0 = module_0.RoleDefinition()
        str_0 = 'base'
        var_0 = dict(role=str_0)
        var_1 = role_definition_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'role'
        str_1 = {str_0: str_0}
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        str_2 = 'values'
        str_3 = {str_0: str_1, str_2: str_2}
        var_1 = role_definition_0.preprocess_data(str_3)
    except BaseException:
        pass

def test_case_10():
    try:
        role_definition_0 = module_0.RoleDefinition()
        ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject()
        var_0 = role_definition_0.preprocess_data(ansible_base_y_a_m_l_object_0)
    except BaseException:
        pass