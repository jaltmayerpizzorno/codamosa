# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0
import ansible.playbook.role as module_1

def test_case_0():
    pass

def test_case_1():
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.get_include_params()

def test_case_2():
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.get_name()

def test_case_3():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    bool_0 = True
    include_role_0 = module_0.IncludeRole(bool_0)
    var_0 = include_role_0.copy(list_0)

def test_case_4():
    list_0 = []
    bytes_0 = b'F\xe3 \x99'
    role_0 = module_1.Role(bytes_0)
    include_role_0 = module_0.IncludeRole(list_0, role_0)
    var_0 = include_role_0.get_include_params()
    include_role_1 = module_0.IncludeRole()