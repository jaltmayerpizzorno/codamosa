# Automatically generated by Pynguin.
import ansible.playbook.role.metadata as module_0

def test_case_0():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        str_0 = '9L#\\'
        bool_0 = False
        var_1 = role_metadata_0.load(var_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        int_0 = 2441
        bytes_0 = b''
        role_metadata_0 = module_0.RoleMetadata()
        role_metadata_1 = module_0.RoleMetadata()
        var_0 = role_metadata_1.load(list_0, int_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xc2\xc7W\xe6\x83\x08)\xc8\x83q|\xc3r\xac'
        float_0 = 0.5
        bytes_1 = b'\xefb\xde\x8bnQ@8\x04\xbcAM\xc8\xf2"h'
        int_0 = 2247
        dict_0 = {float_0: bytes_1, float_0: bytes_1, bytes_1: bytes_1, int_0: int_0}
        role_metadata_0 = module_0.RoleMetadata(dict_0)
        var_0 = role_metadata_0.deserialize(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x19^7}\xfd\xc0r\xcc\xeb\x99\x17!$R\xf8\xe7\xd7-'
        role_metadata_0 = module_0.RoleMetadata()
        var_0 = role_metadata_0.serialize()
        var_1 = role_metadata_0.serialize()
        dict_0 = {role_metadata_0: var_1, role_metadata_0: var_1, role_metadata_0: role_metadata_0}
        var_2 = role_metadata_0.deserialize(dict_0)
        bytes_1 = b'\x1d'
        str_0 = '|\rW5\r*D%\x0c]| PXU#gS/j'
        role_metadata_1 = module_0.RoleMetadata(str_0)
        var_3 = role_metadata_0.serialize()
        var_4 = role_metadata_1.load(bytes_0, role_metadata_0, bytes_1)
    except BaseException:
        pass

def test_case_4():
    try:
        role_metadata_0 = module_0.RoleMetadata()
        str_0 = ''
        role_metadata_1 = module_0.RoleMetadata(str_0)
        var_0 = role_metadata_1.serialize()
        dict_0 = {}
        bytes_0 = b'\x14j\xd3\x95'
        var_1 = role_metadata_0.load(dict_0, bytes_0)
    except BaseException:
        pass