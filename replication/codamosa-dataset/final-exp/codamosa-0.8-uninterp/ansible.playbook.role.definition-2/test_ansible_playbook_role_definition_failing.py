# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        role_definition_0 = None
        role_definition_1 = module_0.RoleDefinition(role_definition_0)
        bool_0 = False
        role_definition_2 = module_0.RoleDefinition()
        var_0 = role_definition_2.load(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        role_definition_0 = module_0.RoleDefinition(int_0)
        var_0 = role_definition_0.preprocess_data(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_definition_0 = module_0.RoleDefinition()
        bool_0 = False
        var_0 = role_definition_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        bool_0 = False
        set_0 = set()
        var_1 = role_definition_0.get_name(set_0)
        var_2 = role_definition_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 82
        set_0 = set()
        str_0 = "M{CAwD,7n')2~I8R"
        set_1 = {str_0}
        role_definition_0 = module_0.RoleDefinition(set_0, str_0, set_1)
        var_0 = role_definition_0.preprocess_data(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        role_definition_0 = module_0.RoleDefinition()
        str_0 = '42'
        var_0 = dict(role=str_0)
        var_1 = role_definition_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        ansible_mapping_0 = module_1.AnsibleMapping()
        var_1 = role_definition_0.preprocess_data(ansible_mapping_0)
    except BaseException:
        pass

def test_case_7():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = dict(role=role_definition_0)
        var_1 = role_definition_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -2626
        role_definition_0 = module_0.RoleDefinition(int_0)
        set_0 = {role_definition_0, int_0}
        float_0 = 2.0
        role_definition_1 = module_0.RoleDefinition(set_0, float_0, float_0)
        var_0 = role_definition_1.get_name()
        str_0 = '{{ 42 }}'
        set_1 = {role_definition_1, str_0}
        var_1 = role_definition_0.get_name(set_1)
        var_2 = dict(role=str_0)
        var_3 = role_definition_1.preprocess_data(var_2)
    except BaseException:
        pass

def test_case_9():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        list_0 = []
        ansible_base_y_a_m_l_object_0 = module_1.AnsibleBaseYAMLObject(*list_0)
        var_1 = role_definition_0.preprocess_data(ansible_base_y_a_m_l_object_0)
    except BaseException:
        pass