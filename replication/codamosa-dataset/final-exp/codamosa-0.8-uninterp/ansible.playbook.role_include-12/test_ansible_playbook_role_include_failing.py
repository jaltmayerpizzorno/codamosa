# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0

def test_case_0():
    try:
        str_0 = 'zKjJFuWwdkal1Rg'
        tuple_0 = ()
        list_0 = [str_0]
        bytes_0 = b'\x16\xad\x98]aS\x0f\r\x9b\x8a],\x93N\xd5'
        include_role_0 = module_0.IncludeRole(bytes_0)
        include_role_1 = module_0.IncludeRole(include_role_0)
        var_0 = include_role_1.get_block_list(tuple_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'ZpWq5{j`o/'
        float_0 = -443.2281
        include_role_0 = module_0.IncludeRole(str_0)
        include_role_1 = module_0.IncludeRole(str_0, float_0)
        var_0 = include_role_0.get_name()
        var_1 = include_role_1.get_name()
        var_2 = include_role_1.get_block_list()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'CQ3Z'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.load(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 599.0
        set_0 = {float_0}
        bytes_0 = b'\n\xca\xef\xf7\x014\xc4\xa9\x9a\xef\tH\x80\x00='
        include_role_0 = module_0.IncludeRole(set_0, bytes_0)
        var_0 = include_role_0.copy()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        include_role_0 = module_0.IncludeRole(bool_0)
        var_0 = include_role_0.get_include_params()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '=g"Oq13>;'
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_include_params()
        include_role_1 = module_0.IncludeRole(include_role_0)
        var_1 = include_role_0.get_name()
        var_2 = include_role_1.copy(str_0)
        float_0 = -654.0
        dict_0 = {}
        tuple_0 = (float_0, dict_0)
        var_3 = include_role_1.load(tuple_0, dict_0)
    except BaseException:
        pass