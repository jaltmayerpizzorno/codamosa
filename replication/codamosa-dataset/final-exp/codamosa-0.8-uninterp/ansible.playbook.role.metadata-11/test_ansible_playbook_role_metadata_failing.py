# Automatically generated by Pynguin.
import ansible.playbook.role.metadata as module_0

def test_case_0():
    try:
        str_0 = ''
        str_1 = 'AF&,wc:""Mc'
        dict_0 = {str_0: str_1, str_1: str_1}
        bytes_0 = b'\\"\x02*\x01\xc8\xf4el\x1f\x12\x0f'
        tuple_0 = (bytes_0,)
        role_metadata_0 = module_0.RoleMetadata(tuple_0)
        str_2 = 'p;"i4g9x `Oe."'
        bool_0 = False
        role_metadata_1 = module_0.RoleMetadata(bool_0)
        bool_1 = False
        role_metadata_2 = module_0.RoleMetadata(bool_1)
        var_0 = role_metadata_2.load(dict_0, role_metadata_0, str_2)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 944.8749
        bytes_0 = b'm\x02\xc4\x93q\xeb\xc4\x81\xcd\x9c\xc7A\x95|\xe3\x82\xc3'
        float_1 = -2035.0
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.load(float_0, bytes_0, float_1)
    except BaseException:
        pass

def test_case_2():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.deserialize(role_metadata_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = None
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.deserialize(dict_0)
        role_metadata_1 = module_0.RoleMetadata()
        str_0 = "%-1L<2\tYJW)v('"
        set_0 = None
        float_0 = None
        var_1 = role_metadata_1.load(str_0, set_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        str_0 = "8T_:a2[mjo''2/)!"
        complex_0 = None
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.load(dict_0, str_0, complex_0)
        str_1 = "Wt !G`od' Xm"
        role_metadata_1 = module_0.RoleMetadata()
        var_1 = role_metadata_1.deserialize(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'dependencies'
        str_1 = [str_0, str_0]
        var_0 = {str_0: str_1}
        role_metadata_0 = module_0.RoleMetadata()
        var_1 = role_metadata_0.load_data(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'allow_duplicates'
        str_1 = 'dependencies'
        bool_0 = False
        str_2 = 'role'
        str_3 = 'test2'
        str_4 = {str_2: str_3}
        var_0 = {str_0: bool_0, str_1: str_4}
        role_metadata_0 = module_0.RoleMetadata()
        var_1 = role_metadata_0.load_data(var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'allow_duplicates'
        str_1 = 'dependencies'
        bool_0 = False
        str_2 = 'role'
        str_3 = '1.0'
        str_4 = 'test2'
        str_5 = {str_2: str_4}
        str_6 = 'test3'
        str_7 = [str_3, str_5, str_6]
        var_0 = {str_0: bool_0, str_1: str_7}
        role_metadata_0 = module_0.RoleMetadata()
        var_1 = role_metadata_0.load_data(var_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'dependencies'
        str_1 = {str_0: str_0}
        str_2 = [str_1, str_0]
        var_0 = {str_0: str_2}
        role_metadata_0 = module_0.RoleMetadata()
        var_1 = role_metadata_0.load_data(var_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'dependencies'
        bool_0 = False
        var_0 = {str_0: bool_0}
        role_metadata_0 = module_0.RoleMetadata()
        var_1 = role_metadata_0.load_data(var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'dependencies'
        str_1 = 're'
        str_2 = {str_1: str_1}
        str_3 = [str_2, str_0]
        role_metadata_0 = module_0.RoleMetadata()
        dict_0 = {str_0: str_3}
        float_0 = 2746.54289
        bytes_0 = None
        role_metadata_1 = module_0.RoleMetadata()
        var_0 = role_metadata_1.load(dict_0, float_0, bytes_0)
    except BaseException:
        pass