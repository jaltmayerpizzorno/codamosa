# Automatically generated by Pynguin.
import ansible.playbook.role.metadata as module_0

def test_case_0():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        str_0 = 'dependencies'
        str_1 = [str_0, str_0]
        str_2 = {str_0: str_1}
        var_0 = role_metadata_0.load(str_2, role_metadata_0, role_metadata_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "!%'9Qmux}]Tqg&B?z"
        str_1 = 'dr\rCW:}zQ\n0Y'
        int_0 = -4493
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.load(str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        str_0 = 'EXPECTED FAILURE'
        var_1 = role_metadata_0.deserialize(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 65001
        role_metadata_0 = module_0.RoleMetadata(int_0)
        dict_0 = {role_metadata_0: role_metadata_0, role_metadata_0: role_metadata_0}
        role_metadata_1 = module_0.RoleMetadata()
        var_0 = role_metadata_1.deserialize(dict_0)
        set_0 = None
        float_0 = -3129.0
        role_metadata_2 = module_0.RoleMetadata()
        var_1 = role_metadata_2.load(set_0, float_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        role_metadata_1 = module_0.RoleMetadata()
        role_metadata_2 = module_0.RoleMetadata()
        str_0 = None
        var_1 = role_metadata_1.load(dict_0, dict_0)
        var_2 = role_metadata_1.deserialize(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        str_0 = 'dependencies'
        str_1 = [str_0, str_0]
        str_2 = {str_0: str_1}
        var_0 = None
        var_1 = role_metadata_0.load(str_2, var_0, var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        str_0 = 'dependencies'
        str_1 = 'role'
        str_2 = 'role1'
        str_3 = {str_1: str_2}
        str_4 = 'role2'
        str_5 = {str_1: str_4}
        str_6 = [str_3, str_5]
        str_7 = {str_0: str_6}
        var_0 = role_metadata_0.load(str_7, role_metadata_0, role_metadata_0)
    except BaseException:
        pass

def test_case_7():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        str_0 = 'dependencies'
        str_1 = 'role1'
        str_2 = {str_1: str_1}
        str_3 = [str_0, str_2]
        str_4 = {str_0: str_3}
        var_0 = role_metadata_0.load(str_4, str_2, str_2)
    except BaseException:
        pass

def test_case_8():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        str_0 = 'dependencies'
        str_1 = 'role1'
        str_2 = {str_0: str_1}
        var_0 = role_metadata_0.load(str_2, str_2, str_2)
    except BaseException:
        pass

def test_case_9():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        str_0 = 'dependencies'
        str_1 = []
        str_2 = {str_0: str_1}
        var_0 = None
        var_1 = role_metadata_0.load(str_2, var_0, var_0)
    except BaseException:
        pass