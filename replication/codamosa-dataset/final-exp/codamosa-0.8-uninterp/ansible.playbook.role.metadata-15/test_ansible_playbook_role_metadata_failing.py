# Automatically generated by Pynguin.
import ansible.playbook.role.metadata as module_0
import ansible.playbook.role.requirement as module_1

def test_case_0():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        var_1 = role_metadata_0.load(var_0, var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        var_1 = role_metadata_0.serialize()
        dict_0 = {}
        role_metadata_1 = module_0.RoleMetadata()
        bytes_0 = b'3\xb3\x81\xd5n'
        role_metadata_2 = module_0.RoleMetadata()
        var_2 = role_metadata_1.serialize()
        var_3 = role_metadata_1.load(dict_0, role_metadata_1)
        var_4 = role_metadata_1.deserialize(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 0.0
        list_0 = [float_0, float_0, float_0, float_0]
        tuple_0 = (list_0,)
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.load(float_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        role_metadata_1 = module_0.RoleMetadata()
        str_0 = '\tu'
        var_1 = role_metadata_1.deserialize(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'dependencies'
        bool_0 = True
        var_0 = [str_0]
        var_1 = {str_0: bool_0, str_0: var_0}
        role_metadata_0 = module_0.RoleMetadata()
        role_requirement_0 = module_1.RoleRequirement()
        dict_0 = {role_metadata_0: var_0, role_metadata_0: str_0, str_0: bool_0, role_requirement_0: role_metadata_0}
        var_2 = role_metadata_0.deserialize(dict_0)
        var_3 = role_metadata_0.load_data(var_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'dependencies'
        bool_0 = False
        var_0 = {str_0: bool_0, str_0: str_0}
        role_metadata_0 = module_0.RoleMetadata()
        var_1 = role_metadata_0.load_data(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dependencies'
        bool_0 = False
        var_0 = {str_0: bool_0, str_0: bool_0}
        role_metadata_0 = module_0.RoleMetadata()
        var_1 = role_metadata_0.load_data(var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'allow_duplicates'
        str_1 = 'dependencies'
        bool_0 = False
        var_0 = []
        role_metadata_0 = module_0.RoleMetadata()
        role_metadata_1 = module_0.RoleMetadata(role_metadata_0)
        var_1 = role_metadata_1.serialize()
        var_2 = {str_0: bool_0, str_1: var_0}
        var_3 = role_metadata_1.load_data(var_2)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'dependencies'
        bool_0 = False
        var_0 = [str_0]
        var_1 = {str_0: bool_0, str_0: var_0}
        role_metadata_0 = module_0.RoleMetadata()
        var_2 = role_metadata_0.load_data(var_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'Added %s to loader search path'
        set_0 = {str_0, str_0, str_0, str_0}
        tuple_0 = (str_0, set_0, set_0)
        str_1 = 'dependencies'
        var_0 = [str_1, tuple_0, set_0, str_1, str_0]
        var_1 = {str_1: var_0}
        role_metadata_0 = module_0.RoleMetadata()
        var_2 = role_metadata_0.load_data(var_1)
    except BaseException:
        pass