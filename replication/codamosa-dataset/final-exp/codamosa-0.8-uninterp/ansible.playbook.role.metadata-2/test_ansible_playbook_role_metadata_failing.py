# Automatically generated by Pynguin.
import ansible.playbook.role.metadata as module_0

def test_case_0():
    try:
        str_0 = 'D7=p'
        int_0 = -988
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.load(str_0, int_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        var_1 = role_metadata_0.load(var_0, role_metadata_0, role_metadata_0, role_metadata_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        str_0 = ''
        var_1 = role_metadata_0.deserialize(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'STju:A^[<F!Sw\x0ct5C<\t'
        role_metadata_0 = module_0.RoleMetadata()
        float_0 = 0.001
        dict_0 = {float_0: float_0}
        set_0 = {float_0, float_0, str_0, float_0}
        role_metadata_1 = module_0.RoleMetadata(set_0)
        var_0 = role_metadata_1.deserialize(dict_0)
        role_metadata_2 = module_0.RoleMetadata()
        role_metadata_3 = module_0.RoleMetadata(float_0)
        int_0 = -1328
        var_1 = role_metadata_1.deserialize(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        role_metadata_0 = module_0.RoleMetadata()
        str_0 = 'D\tp^Lg\r^\x0bk%i{{z_:O8z'
        role_metadata_1 = module_0.RoleMetadata(str_0)
        list_0 = [dict_0, role_metadata_0, str_0, role_metadata_1]
        role_metadata_2 = module_0.RoleMetadata(list_0)
        float_0 = -1772.0
        role_metadata_3 = module_0.RoleMetadata(float_0)
        var_0 = role_metadata_3.load(dict_0, role_metadata_1)
        var_1 = role_metadata_2.deserialize(role_metadata_2)
    except BaseException:
        pass

def test_case_5():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        bool_0 = True
        str_0 = 'dependencies'
        var_0 = [str_0, str_0]
        var_1 = {str_0: bool_0, str_0: var_0}
        var_2 = role_metadata_0.load_data(var_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dependencies'
        bool_0 = True
        var_0 = [str_0]
        var_1 = {str_0: bool_0, str_0: var_0}
        int_0 = 17
        role_metadata_0 = module_0.RoleMetadata(int_0)
        var_2 = role_metadata_0.load_data(var_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'allow_duplicates'
        str_1 = 'dependencies'
        bool_0 = True
        var_0 = []
        var_1 = {str_0: bool_0, str_1: var_0}
        int_0 = 1
        role_metadata_0 = module_0.RoleMetadata(int_0)
        var_2 = role_metadata_0.load_data(var_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'allow_duplicates'
        str_1 = 'dependencies'
        role_metadata_0 = module_0.RoleMetadata()
        bool_0 = True
        var_0 = [bool_0]
        var_1 = {str_0: bool_0, str_1: var_0}
        int_0 = 17
        role_metadata_1 = module_0.RoleMetadata(int_0)
        var_2 = role_metadata_1.load_data(var_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'dependencies'
        bool_0 = True
        role_metadata_0 = module_0.RoleMetadata(bool_0)
        var_0 = role_metadata_0.serialize()
        var_1 = [var_0, str_0, str_0, str_0]
        var_2 = {str_0: bool_0, str_0: var_1}
        var_3 = role_metadata_0.load_data(var_2)
    except BaseException:
        pass