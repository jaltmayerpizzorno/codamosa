# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0

def test_case_0():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_block_list(include_role_0)
    except BaseException:
        pass

def test_case_1():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_include_params()
        var_1 = include_role_0.get_name()
        var_2 = include_role_0.get_block_list()
    except BaseException:
        pass

def test_case_2():
    try:
        include_role_0 = module_0.IncludeRole()
        bool_0 = False
        list_0 = []
        var_0 = include_role_0.load(bool_0, list_0)
    except BaseException:
        pass