# Automatically generated by Pynguin.
import ansible.playbook.role.metadata as module_0

def test_case_0():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        str_0 = ')~*aP"S{}j2'
        var_1 = role_metadata_0.load(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'RO;Fa2\x0bR40'
        bool_0 = True
        role_metadata_0 = module_0.RoleMetadata(bool_0)
        var_0 = role_metadata_0.deserialize(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        role_metadata_1 = module_0.RoleMetadata()
        float_0 = 1815.439
        dict_0 = {float_0: float_0}
        role_metadata_2 = module_0.RoleMetadata()
        var_0 = role_metadata_2.deserialize(dict_0)
        int_0 = 500
        var_1 = role_metadata_1.deserialize(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        var_1 = role_metadata_0.load(var_0, var_0)
    except BaseException:
        pass

def test_case_4():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        dict_0 = {}
        list_0 = None
        str_0 = '652J-~Nr\x0bN\n\r XbJw'
        role_metadata_1 = module_0.RoleMetadata()
        var_0 = role_metadata_1.load(dict_0, list_0, str_0)
        var_1 = role_metadata_0.serialize()
        var_2 = role_metadata_0.serialize()
        var_3 = role_metadata_0.serialize()
        role_metadata_2 = module_0.RoleMetadata()
        var_4 = role_metadata_2.serialize()
        var_5 = role_metadata_2.load(var_3, var_3)
    except BaseException:
        pass