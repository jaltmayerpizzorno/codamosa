# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0

def test_case_0():
    try:
        str_0 = 'A'
        include_role_0 = module_0.IncludeRole(str_0)
        var_0 = include_role_0.get_block_list()
    except BaseException:
        pass

def test_case_1():
    try:
        include_role_0 = module_0.IncludeRole()
        str_0 = 'A file containing a list of roles to be installed.'
        str_1 = 'PSRP FETCH %s to %s (offset=%d'
        dict_0 = {}
        tuple_0 = (str_0, str_1, dict_0)
        include_role_1 = module_0.IncludeRole(tuple_0)
        var_0 = include_role_0.get_block_list(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        str_0 = '%s=%-4s'
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.load(bool_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        int_0 = -849
        include_role_0 = module_0.IncludeRole(bool_0, int_0)
        var_0 = include_role_0.get_include_params()
    except BaseException:
        pass