# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0

def test_case_0():
    pass

def test_case_1():
    role_definition_0 = module_0.RoleDefinition()

def test_case_2():
    role_definition_0 = module_0.RoleDefinition()
    var_0 = role_definition_0.get_role_params()

def test_case_3():
    tuple_0 = ()
    role_definition_0 = module_0.RoleDefinition(tuple_0)
    var_0 = role_definition_0.get_role_path()

def test_case_4():
    role_definition_0 = module_0.RoleDefinition()
    var_0 = role_definition_0.get_name()

def test_case_5():
    int_0 = 4294967295
    list_0 = []
    float_0 = 0.0
    role_definition_0 = module_0.RoleDefinition(list_0, int_0, float_0)
    role_definition_1 = module_0.RoleDefinition(int_0)
    var_0 = role_definition_1.get_name()
    tuple_0 = ()
    var_1 = role_definition_1.get_name(tuple_0)
    var_2 = role_definition_1.get_role_params()