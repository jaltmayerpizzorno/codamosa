# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0
import ansible.playbook.block as module_1
import ansible.playbook.role.include as module_2
import ansible.playbook.role as module_3

def test_case_0():
    try:
        bytes_0 = b'<D\x06\xb0P\xad\xf5'
        bool_0 = False
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_block_list(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_include_params()
        include_role_1 = module_0.IncludeRole()
        var_1 = include_role_1.get_block_list()
    except BaseException:
        pass

def test_case_2():
    try:
        include_role_0 = module_0.IncludeRole()
        bytes_0 = b"\xe3\xdb\xc6`\xf3\xa6O'\xcd\x9dv"
        var_0 = include_role_0.load(include_role_0, include_role_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x14'
        bool_0 = True
        set_0 = {bool_0, bool_0, bytes_0, bool_0}
        tuple_0 = (bytes_0, bool_0, set_0, bool_0)
        include_role_0 = module_0.IncludeRole(tuple_0)
        var_0 = include_role_0.get_include_params()
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        float_0 = 3086.184891
        include_role_0 = module_0.IncludeRole(list_0, float_0)
        var_0 = include_role_0.get_name()
        var_1 = include_role_0.get_include_params()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Unit test for method load of class IncludeRole.'
        str_1 = 'include_role'
        include_role_0 = module_0.IncludeRole()
        str_2 = 'test'
        var_0 = dict(module=str_1, args=str_2)
        var_1 = dict(action=var_0)
        var_2 = dict()
        var_3 = dict()
        var_4 = dict()
        var_5 = dict(name=str_2, defaults=var_2, vars=var_3, tasks=var_4)
        bool_0 = False
        include_role_1 = module_0.IncludeRole(bool_0)
        var_6 = include_role_1.get_name()
        var_7 = include_role_1.get_name()
        block_0 = module_1.Block(str_0, str_2, include_role_0, var_5)
        include_role_2 = module_0.IncludeRole(block_0, var_5)
        var_8 = include_role_2.load(var_1, block_0, var_5)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        str_0 = '?Gqt]LfU.>m'
        role_include_0 = module_2.RoleInclude()
        role_include_1 = module_2.RoleInclude(str_0, dict_0, role_include_0)
        role_0 = module_3.Role(dict_0, role_include_1)
        include_role_0 = module_0.IncludeRole(bool_0, role_0)
        var_0 = include_role_0.get_include_params()
        str_1 = 'include_role'
        str_2 = 'test'
        var_1 = dict(name=str_2)
        var_2 = dict(module=str_1, args=var_1)
        var_3 = dict(action=var_2)
        var_4 = dict()
        var_5 = dict()
        var_6 = dict()
        include_role_1 = module_0.IncludeRole()
        var_7 = include_role_1.get_name()
        var_8 = dict(name=str_2, defaults=var_4, vars=var_3, tasks=var_6)
        var_9 = include_role_1.copy()
        var_10 = include_role_1.get_name()
        bytes_0 = None
        role_1 = module_3.Role(bytes_0)
        str_3 = 'e\taz\tG|DBa\x0bMhP]_@#a1'
        include_role_2 = module_0.IncludeRole(role_1, str_3)
        var_11 = include_role_2.get_name()
        var_12 = include_role_1.get_name()
        block_0 = module_1.Block(include_role_1)
        bool_1 = False
        include_role_3 = module_0.IncludeRole(bool_1)
        var_13 = include_role_1.load(role_1, include_role_2, include_role_2)
    except BaseException:
        pass