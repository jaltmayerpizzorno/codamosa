# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0
import ansible.playbook.block as module_1
import ansible.playbook.role as module_2

def test_case_0():
    pass

def test_case_1():
    include_role_0 = module_0.IncludeRole()

def test_case_2():
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.get_name()

def test_case_3():
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.copy()

def test_case_4():
    include_role_0 = module_0.IncludeRole()
    var_0 = include_role_0.get_include_params()
    var_1 = include_role_0.copy()
    var_2 = include_role_0.get_name()

def test_case_5():
    tuple_0 = ()
    int_0 = -2789
    block_0 = module_1.Block(int_0)
    dict_0 = {int_0: int_0, int_0: block_0}
    role_0 = module_2.Role(dict_0)
    include_role_0 = module_0.IncludeRole(block_0, role_0)
    var_0 = include_role_0.get_include_params()
    include_role_1 = module_0.IncludeRole(tuple_0)
    var_1 = include_role_1.copy()