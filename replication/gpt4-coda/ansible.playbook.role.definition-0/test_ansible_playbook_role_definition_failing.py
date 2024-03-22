# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        int_0 = 641
        bytes_0 = b'\x9b\xbe\xfa\xfd`\x91\x9bO;'
        bool_0 = True
        role_definition_0 = module_0.RoleDefinition(bool_0)
        role_definition_1 = module_0.RoleDefinition(bytes_0)
        var_0 = role_definition_1.load(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x19K\x1d\xf1O\xa8\xcf\x17\xce\xfc\xaf_\xe6\xaab|'
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.preprocess_data(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_definition_0 = module_0.RoleDefinition()
        bool_0 = True
        var_0 = role_definition_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '(4?f'
        str_1 = 'O-!6rR(^aC'
        bytes_0 = b'6\xb0\x8bm`'
        tuple_0 = ()
        role_definition_0 = module_0.RoleDefinition(str_1, bytes_0, tuple_0)
        var_0 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 19
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_role_params()
        var_1 = role_definition_0.get_name(role_definition_0)
        var_2 = role_definition_0.preprocess_data(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        dict_0 = {}
        var_1 = role_definition_0.get_name(dict_0)
        ansible_mapping_0 = module_1.AnsibleMapping()
        bytes_0 = b'\xee_\xa7\xce\xe9\xf0\xbfX\xfba\x83}s\xe6\xe0\x99'
        var_2 = role_definition_0.preprocess_data(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        role_definition_0 = module_0.RoleDefinition()
        dict_0 = {bool_0: role_definition_0, role_definition_0: role_definition_0}
        var_0 = role_definition_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        bool_0 = False
        var_1 = role_definition_0.get_name(bool_0)
        str_0 = 'Na<u)Nz1nbq'
        dict_0 = {str_0: role_definition_0, str_0: str_0}
        ansible_mapping_0 = module_1.AnsibleMapping(**dict_0)
        var_2 = role_definition_0.preprocess_data(ansible_mapping_0)
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = None
        var_1 = None
        var_2 = None
        str_0 = '/fake/roles'
        str_1 = 'fake.collection'
        str_2 = [str_1]
        role_definition_0 = module_0.RoleDefinition(var_2, str_0, var_1, var_0, str_2)
        str_3 = 'simple_role'
        var_3 = role_definition_0.preprocess_data(str_3)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = []
        role_definition_0 = module_0.RoleDefinition(list_0)
        str_0 = 'role'
        var_0 = role_definition_0.get_name()
        str_1 = 'dict_role'
        str_2 = {str_0: str_1}
        var_1 = role_definition_0.get_role_params()
        var_2 = role_definition_0.preprocess_data(str_2)
    except BaseException:
        pass

def test_case_10():
    try:
        var_0 = None
        list_0 = []
        role_definition_0 = module_0.RoleDefinition(list_0)
        var_1 = role_definition_0.get_role_params()
        str_0 = 'fake.collection'
        str_1 = [str_0]
        var_2 = role_definition_0.get_role_params()
        role_definition_1 = module_0.RoleDefinition(str_0, str_1, str_0, var_0, str_1)
        str_2 = 'role'
        str_3 = 'dict_role'
        str_4 = {str_2: str_3}
        var_3 = role_definition_1.get_role_params()
        var_4 = role_definition_1.preprocess_data(str_4)
    except BaseException:
        pass

def test_case_11():
    try:
        list_0 = []
        role_definition_0 = module_0.RoleDefinition(list_0)
        str_0 = 'fakeco|lejion'
        str_1 = [str_0]
        str_2 = 'role'
        var_0 = role_definition_0.get_name()
        str_3 = {str_2: str_1}
        var_1 = role_definition_0.get_role_params()
        var_2 = role_definition_0.preprocess_data(str_3)
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = []
        role_definition_0 = module_0.RoleDefinition(list_0)
        var_0 = role_definition_0.get_role_path()
        str_0 = '1.7.5'
        var_1 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass