# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0
import ansible.playbook.role as module_1

def test_case_0():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.copy()
        bool_0 = True
        include_role_1 = module_0.IncludeRole(bool_0)
        var_1 = include_role_1.get_block_list()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'f*kZ!|Py'
        bytes_0 = b'Zl\x89$\xbc\x1f\nepj\x9c\x00^\xda\x89\xe27\xb9\x1ez'
        include_role_0 = module_0.IncludeRole(str_0, bytes_0)
        include_role_1 = module_0.IncludeRole()
        var_0 = include_role_1.get_block_list(include_role_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        list_0 = [tuple_0]
        int_0 = 702
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.load(list_0, int_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        bytes_0 = b'\x89O\xcd'
        bool_0 = False
        include_role_0 = module_0.IncludeRole(bytes_0, bool_0)
        var_0 = include_role_0.copy(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_name()
        var_1 = include_role_0.get_include_params()
        var_2 = include_role_0.get_include_params()
        dict_0 = {}
        bool_0 = False
        tuple_0 = ()
        role_0 = module_1.Role(bool_0, tuple_0)
        include_role_1 = module_0.IncludeRole(dict_0, role_0)
        var_3 = include_role_1.get_include_params()
        bool_1 = False
        float_0 = -2879.71
        float_1 = 1546.0388
        str_0 = 'LGMQ<z"w-cm&l3>'
        tuple_1 = (bool_1, float_0, float_1, str_0)
        var_4 = include_role_0.get_block_list(tuple_1)
    except BaseException:
        pass