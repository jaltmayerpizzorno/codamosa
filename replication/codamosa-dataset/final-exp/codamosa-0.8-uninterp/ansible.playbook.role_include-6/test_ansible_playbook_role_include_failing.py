# Automatically generated by Pynguin.
import ansible.playbook.role_include as module_0
import ansible.playbook.task_include as module_1
import ansible.playbook.role as module_2

def test_case_0():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_block_list()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x8b\x87u\xaeO\x1bi\xd2\x91\xcb<\xf9l'
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_name()
        include_role_1 = module_0.IncludeRole(bytes_0)
        var_1 = include_role_0.get_include_params()
        var_2 = include_role_1.get_block_list(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        bool_1 = None
        tuple_0 = (bool_1, bool_0)
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.copy(dict_0, tuple_0)
        float_0 = -2170.0
        bytes_0 = b'\xceZ\x06m]\x13\xd6\xea\x85\xc2\xbc\xc9'
        str_0 = ' {\nbK-NplLrFEZ4U'
        var_1 = include_role_0.load(float_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        bool_1 = True
        include_role_0 = module_0.IncludeRole(bool_0, bool_1)
        var_0 = include_role_0.get_name()
        var_1 = include_role_0.get_include_params()
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\x84\xd9\x13\xd8\xa2\x10\xe8\x0f\x90v\x0b\xcb\xc9\xc2\xc3\xb8\x8f'
        set_0 = {bytes_0, bytes_0}
        include_role_0 = module_0.IncludeRole(set_0, bytes_0)
        var_0 = include_role_0.get_include_params()
    except BaseException:
        pass

def test_case_5():
    try:
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_name()
        task_include_0 = module_1.TaskInclude()
        role_0 = module_2.Role()
        include_role_1 = module_0.IncludeRole(task_include_0, role_0)
        var_1 = include_role_1.get_include_params()
        var_2 = include_role_1.get_block_list()
    except BaseException:
        pass