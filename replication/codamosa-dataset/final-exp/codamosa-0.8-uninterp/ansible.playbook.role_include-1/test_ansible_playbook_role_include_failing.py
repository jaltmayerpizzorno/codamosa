# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0

def test_case_0():
    try:
        str_0 = '@J'
        bool_0 = True
        include_role_0 = module_0.IncludeRole(str_0, bool_0)
        list_0 = [bool_0]
        var_0 = include_role_0.get_block_list(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        include_role_0 = module_0.IncludeRole()
        bool_0 = True
        tuple_0 = None
        tuple_1 = (bool_0, tuple_0)
        var_0 = include_role_0.copy(tuple_1)
        list_0 = [include_role_0]
        var_1 = include_role_0.copy(include_role_0, list_0)
        var_2 = include_role_0.get_block_list()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '--playbook-dir'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.load(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_name()
        dict_0 = {}
        bytes_0 = b't5H\x04a\xcb\xd8Wu\xb8\xa7\x16(\xe5\xcb5\xe2\x8b\x9e'
        include_role_1 = module_0.IncludeRole(dict_0, bytes_0)
        var_1 = include_role_1.get_include_params()
    except BaseException:
        pass