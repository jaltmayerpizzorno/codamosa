# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        bool_0 = False
        int_0 = 255
        role_definition_0 = module_0.RoleDefinition(int_0)
        var_0 = role_definition_0.load(bool_0)
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
        role_definition_0 = module_0.RoleDefinition()
        dict_0 = {role_definition_0: role_definition_0, role_definition_0: role_definition_0}
        var_0 = role_definition_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_definition_0 = module_0.RoleDefinition()
        str_0 = 'foobar'
        var_0 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        int_0 = -1659
        var_1 = role_definition_0.preprocess_data(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        str_0 = '$Te_R4s]Y'
        dict_0 = {bool_0: str_0, str_0: bool_0}
        bool_1 = True
        bool_2 = True
        int_0 = -3472
        float_0 = 473.3358
        role_definition_0 = module_0.RoleDefinition(bool_1, float_0)
        var_0 = role_definition_0.get_role_path()
        str_1 = ' Load YAML Config Files in order, check merge flags, keep origin of settings'
        role_definition_1 = module_0.RoleDefinition(bool_2, int_0, str_1)
        role_definition_2 = module_0.RoleDefinition(bool_0, dict_0, bool_1)
        var_1 = role_definition_2.get_role_path()
        var_2 = role_definition_2.preprocess_data(bool_1)
    except BaseException:
        pass

def test_case_6():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        var_1 = role_definition_0.get_role_params()
        var_2 = role_definition_0.preprocess_data(role_definition_0)
    except BaseException:
        pass

def test_case_7():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        ansible_error_0 = None
        var_1 = role_definition_0.get_name(ansible_error_0)
        var_2 = role_definition_0.preprocess_data(ansible_error_0)
    except BaseException:
        pass

def test_case_8():
    try:
        role_definition_0 = module_0.RoleDefinition()
        str_0 = 'foobar'
        var_0 = dict(role=str_0)
        var_1 = role_definition_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_9():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_role_path()
        var_1 = dict(role=role_definition_0)
        var_2 = role_definition_0.preprocess_data(var_1)
    except BaseException:
        pass

def test_case_10():
    try:
        var_0 = None
        role_definition_0 = module_0.RoleDefinition(var_0)
        ansible_mapping_0 = module_1.AnsibleMapping()
        var_1 = role_definition_0.preprocess_data(ansible_mapping_0)
    except BaseException:
        pass