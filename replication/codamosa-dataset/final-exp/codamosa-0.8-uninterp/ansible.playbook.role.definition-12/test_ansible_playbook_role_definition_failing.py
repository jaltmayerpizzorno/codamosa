# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0
import ansible.parsing.yaml.objects as module_1
import ansible.playbook.base as module_2

def test_case_0():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.load(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.preprocess_data(role_definition_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'b\\p'
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        str_0 = '?BAlD5H_{F?rb75)'
        var_1 = role_definition_0.get_name(var_0)
        var_2 = role_definition_0.get_role_params()
        var_3 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'cZ6uZg'
        str_1 = "JPc\x0bx/iJ/k'#P \tBEfj+"
        bool_0 = True
        dict_0 = {bool_0: str_1, bool_0: bool_0}
        tuple_0 = (dict_0,)
        str_2 = 'na0c@j\\\t7n'
        role_definition_0 = module_0.RoleDefinition(str_1, bool_0, tuple_0, str_2)
        var_0 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        role_definition_0 = module_0.RoleDefinition()
        bool_0 = True
        var_0 = role_definition_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        ansible_mapping_0 = module_1.AnsibleMapping()
        list_0 = []
        role_definition_0 = module_0.RoleDefinition(list_0)
        var_0 = role_definition_0.preprocess_data(ansible_mapping_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -109
        role_definition_0 = module_0.RoleDefinition(int_0)
        var_0 = role_definition_0.get_name()
        role_definition_1 = module_0.RoleDefinition()
        str_0 = '1.7.5'
        var_1 = role_definition_1.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        role_definition_0 = module_0.RoleDefinition()
        str_0 = 'roles/test'
        var_0 = dict(role=str_0)
        str_1 = '{{ test }}'
        var_1 = dict(role=str_1)
        var_2 = role_definition_0.preprocess_data(var_1)
    except BaseException:
        pass

def test_case_9():
    try:
        role_definition_0 = module_0.RoleDefinition()
        str_0 = 'test-role'
        var_0 = dict(name=str_0, path=str_0)
        var_1 = dict(role=var_0)
        var_2 = role_definition_0.preprocess_data(var_1)
    except BaseException:
        pass

def test_case_10():
    try:
        ansible_mapping_0 = module_1.AnsibleMapping()
        float_0 = 1405.92
        set_0 = {float_0, float_0, float_0, float_0}
        list_0 = [float_0, set_0]
        list_1 = [list_0, set_0, set_0, list_0]
        str_0 = ''
        str_1 = 'fqcn'
        str_2 = '9S"UKDTY{=\x0b~ B@n>1,;'
        dict_0 = {str_0: list_1, str_1: list_0, str_2: str_2}
        role_definition_0 = module_0.RoleDefinition(ansible_mapping_0, dict_0, ansible_mapping_0)
        var_0 = role_definition_0.get_name()
        role_definition_1 = module_0.RoleDefinition(set_0, list_0, list_1)
        var_1 = role_definition_1.get_name(ansible_mapping_0)
        str_3 = 'test-role'
        var_2 = dict(name=str_3, path=str_3)
        base_0 = module_2.Base()
        var_3 = role_definition_1.get_name(base_0)
        var_4 = role_definition_1.preprocess_data(var_2)
    except BaseException:
        pass