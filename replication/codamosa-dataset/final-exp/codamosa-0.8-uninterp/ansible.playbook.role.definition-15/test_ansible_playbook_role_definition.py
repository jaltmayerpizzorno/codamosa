# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0

def test_case_0():
    pass

def test_case_1():
    role_definition_0 = module_0.RoleDefinition()

def test_case_2():
    bytes_0 = b'\xad\x1fx\\\xb0P\xa5\x86\xb4\xe0PPE\xa7'
    role_definition_0 = module_0.RoleDefinition(bytes_0)
    var_0 = role_definition_0.get_role_params()
    int_0 = 2
    dict_0 = {}
    role_definition_1 = module_0.RoleDefinition(int_0, dict_0)

def test_case_3():
    set_0 = set()
    int_0 = 19
    role_definition_0 = module_0.RoleDefinition(set_0, int_0)
    var_0 = role_definition_0.get_role_path()

def test_case_4():
    role_definition_0 = module_0.RoleDefinition()
    var_0 = role_definition_0.get_name()