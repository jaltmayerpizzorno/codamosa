# Automatically generated by Pynguin.
import ansible.playbook.role.metadata as module_0

def test_case_0():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        set_0 = {role_metadata_0, role_metadata_0, role_metadata_0, role_metadata_0}
        var_0 = role_metadata_0.load(role_metadata_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -197.42
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.deserialize(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\nqkIjFcHQN1~R\x0cwU_L{H'
        bytes_0 = b''
        role_metadata_0 = module_0.RoleMetadata()
        dict_0 = {bytes_0: str_0, bytes_0: role_metadata_0}
        var_0 = role_metadata_0.deserialize(dict_0)
        var_1 = role_metadata_0.load(str_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        float_0 = -771.8649777337735
        var_1 = role_metadata_0.load(var_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        role_metadata_1 = module_0.RoleMetadata()
        var_0 = role_metadata_1.serialize()
        role_metadata_2 = module_0.RoleMetadata()
        bool_0 = True
        role_metadata_3 = module_0.RoleMetadata(bool_0)
        dict_0 = {}
        float_0 = -1046.51619
        int_0 = 1067
        var_1 = role_metadata_2.load(dict_0, float_0, int_0)
        role_metadata_4 = module_0.RoleMetadata()
        tuple_0 = ()
        var_2 = role_metadata_2.deserialize(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'f@p'
        var_0 = [str_0, str_0, str_0]
        var_1 = dict(allow_duplicates=str_0, dependencies=var_0, argument_specs=str_0)
        role_metadata_0 = module_0.RoleMetadata()
        var_2 = role_metadata_0.load_data(var_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        var_0 = dict(allow_duplicates=str_0, dependencies=str_0, argument_specs=str_0)
        role_metadata_0 = module_0.RoleMetadata()
        var_1 = role_metadata_0.load_data(var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'solaris'
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = dict(src=role_metadata_0)
        var_1 = [str_0, var_0, str_0, var_0]
        var_2 = dict(allow_duplicates=var_1, dependencies=var_1, argument_specs=str_0)
        var_3 = role_metadata_0.load_data(var_2)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'foo'
        var_0 = dict(src=str_0)
        var_1 = [str_0, str_0, var_0]
        str_1 = 'str'
        var_2 = dict(allow_duplicates=str_1, dependencies=var_1, argument_specs=str_1)
        role_metadata_0 = module_0.RoleMetadata()
        var_3 = role_metadata_0.load_data(var_2)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'galaxy_info'
        str_1 = 'allow_duplicates'
        str_2 = 'dependencies'
        str_3 = 'junk'
        str_4 = 'role'
        str_5 = 'test.dependency'
        str_6 = {str_4: str_5}
        str_7 = 'test.dependency2'
        str_8 = {str_4: str_7}
        str_9 = [str_6, str_8]
        str_10 = {str_0: str_3, str_1: str_3, str_2: str_9}
        role_metadata_0 = module_0.RoleMetadata(str_4)
        var_0 = None
        var_1 = role_metadata_0.load(str_10, var_0, var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'solaris'
        str_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = dict(src=str_1)
        var_1 = [str_1, var_0, str_0, var_0]
        var_2 = dict(allow_duplicates=var_1, dependencies=var_1, argument_specs=str_0)
        var_3 = role_metadata_0.load_data(var_2)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = True
        str_0 = 'role'
        str_1 = 'q3"\x0cBGh@<p|.3!oaE&'
        str_2 = 'mysql'
        str_3 = '1.0'
        str_4 = 'foo'
        str_5 = {str_0: str_2, str_3: str_3, str_1: str_4}
        str_6 = 'xyz'
        var_0 = dict(role=str_6)
        str_7 = 'https://example.com/repo/roles/foo'
        var_1 = dict(src=str_7)
        dict_0 = {str_7: str_1}
        role_metadata_0 = module_0.RoleMetadata(dict_0)
        var_2 = [str_5, var_0, var_1]
        str_8 = 'bar'
        var_3 = dict(type=str_2, default=str_8)
        var_4 = {role_metadata_0: str_3, str_4: str_1}
        var_5 = dict(allow_duplicates=bool_0, dependencies=var_2, argument_specs=var_4)
        var_6 = role_metadata_0.load_data(var_5)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'solaris'
        str_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = dict(src=role_metadata_0)
        var_1 = [str_1, var_0, str_0, var_0]
        var_2 = dict(allow_duplicates=var_1, dependencies=var_1, argument_specs=str_0)
        var_3 = role_metadata_0.load_data(var_2)
    except BaseException:
        pass