# Automatically generated by Pynguin.
import ansible.playbook.role.metadata as module_0

def test_case_0():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        var_1 = role_metadata_0.load(var_0, role_metadata_0, role_metadata_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -433.39775
        str_0 = 'yum'
        dict_0 = {}
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.load(float_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 0.0
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.deserialize(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.deserialize(dict_0)
        role_metadata_1 = module_0.RoleMetadata()
        var_1 = role_metadata_1.serialize()
        str_0 = 'R"Cr:d&J'
        role_metadata_2 = module_0.RoleMetadata()
        var_2 = role_metadata_2.deserialize(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        dict_0 = {}
        str_0 = 'Dz6In\tUS\ra\ncb3 g&KZ'
        var_0 = role_metadata_0.load(dict_0, str_0)
        tuple_0 = ()
        float_0 = -3128.57
        set_0 = {tuple_0}
        var_1 = role_metadata_0.load(float_0, set_0)
    except BaseException:
        pass