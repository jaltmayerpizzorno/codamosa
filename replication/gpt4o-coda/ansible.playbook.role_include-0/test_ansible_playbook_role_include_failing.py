# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0

def test_case_0():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_include_params()
        var_1 = include_role_0.get_block_list()
    except BaseException:
        pass

def test_case_1():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_include_params()
        bytes_0 = b'\xbd\xa1\x01\x18\x1c&Fe\xcd'
        set_0 = set()
        var_1 = include_role_0.get_block_list(bytes_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        include_role_0 = module_0.IncludeRole()
        bytes_0 = b'\xe2\x82\xf1H'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
        include_role_1 = module_0.IncludeRole(dict_0)
        var_0 = include_role_1.load(include_role_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 1360
        include_role_0 = module_0.IncludeRole(int_0)
        var_0 = include_role_0.copy()
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 0.5
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_include_params()
        var_1 = include_role_0.copy()
        set_0 = {float_0}
        include_role_1 = module_0.IncludeRole(include_role_0, set_0)
        var_2 = include_role_1.get_include_params()
    except BaseException:
        pass