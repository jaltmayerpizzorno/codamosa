# Automatically generated by Pynguin.
import ansible.playbook.role.definition as module_0

def test_case_0():
    try:
        int_0 = -2459
        bytes_0 = b';\xbf\x03UO\xe8a\xc5\xc7\xa7\xdd'
        role_definition_0 = module_0.RoleDefinition(bytes_0, bytes_0)
        var_0 = role_definition_0.load(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        role_definition_0 = module_0.RoleDefinition()
        str_0 = 'FL_o|\x0c_'
        var_0 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        role_definition_0 = module_0.RoleDefinition(bool_0)
        var_0 = role_definition_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        role_definition_0 = module_0.RoleDefinition(bool_0)
        var_0 = role_definition_0.preprocess_data(role_definition_0)
    except BaseException:
        pass

def test_case_4():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_role_path()
        var_1 = role_definition_0.get_name()
        str_0 = 'FL_o|\x0c_'
        var_2 = role_definition_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_name()
        bool_0 = False
        var_1 = role_definition_0.get_name(bool_0)
        bytes_0 = b'\xb9%\x11\xcdR\xce\xff\t\x89Nj\xa1\x0e\xbd\xd1\x07\x00'
        var_2 = role_definition_0.preprocess_data(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        bytes_0 = b'F\x06yo\xf8D\xe2\xdd@\x83\xce\xa5\x9b\xb3\x16\x9a5\xcc\xc1'
        int_0 = -1990
        role_definition_0 = module_0.RoleDefinition(bytes_0, int_0)
        var_0 = role_definition_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x1a\xc6\x1fokQ\x1d\xd4\xd2\xb8\xf7@\xb7'
        int_0 = -1967
        tuple_0 = ()
        role_definition_0 = module_0.RoleDefinition(bytes_0, int_0, tuple_0)
        bool_0 = True
        var_0 = role_definition_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        role_definition_0 = module_0.RoleDefinition()
        str_0 = 'role'
        str_1 = '/\rT'
        str_2 = {str_0: str_1, str_0: str_1}
        var_0 = role_definition_0.preprocess_data(str_2)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'the_role'
        var_0 = dict(role=str_0)
        var_1 = dict(role=var_0)
        str_1 = 'var_man'
        str_2 = 'ldr'
        var_2 = dict(role=var_1, variable_manager=str_1, loader=str_2)
        role_definition_0 = module_0.RoleDefinition()
        var_3 = role_definition_0.preprocess_data(var_2)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = 2304.25801
        bytes_0 = b'S\xa99\n\xeaQNw\xa5\xd5\xbd\xd1U\x13'
        role_definition_0 = module_0.RoleDefinition(float_0, bytes_0, float_0)
        var_0 = role_definition_0.get_name()
        str_0 = 'role'
        str_1 = ';F7'
        str_2 = {str_1: str_1, str_0: str_1}
        var_1 = role_definition_0.preprocess_data(str_2)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'role'
        role_definition_0 = module_0.RoleDefinition(str_0, str_0, str_0, str_0, str_0)
        var_0 = role_definition_0.load_data(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'role'
        str_1 = 'redis'
        str_2 = {str_0: str_1}
        var_0 = None
        role_definition_0 = module_0.RoleDefinition(var_0, var_0, var_0, var_0, var_0)
        var_1 = role_definition_0.load_data(str_2)
    except BaseException:
        pass