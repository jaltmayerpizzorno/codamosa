# Automatically generated by Pynguin.
import ansible.plugins.filter.encryption as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        str_0 = 'W1\tHPHS_d#7B`ax~\tjR'
        var_0 = module_0.do_vault(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 255
        bytes_0 = None
        list_0 = []
        list_1 = [int_0, list_0, list_0, list_0]
        var_0 = module_0.do_vault(int_0, bytes_0, list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        bytes_0 = b'2u\xffQ\x00\x10\xf3)D\xab-\x12|2`'
        list_0 = [bytes_0, bool_0, bytes_0]
        var_0 = module_0.do_vault(bool_0, bytes_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -1384
        list_0 = []
        var_0 = module_0.do_unvault(int_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = None
        str_0 = '*b#Ww<'
        bool_0 = False
        var_0 = module_0.do_unvault(float_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$ANSIBLE_VAULT;1.1;AES256;my;33511665611736306536303361356533373763306138633163646637356530333635383637393935613536633035373766393134626535306166613862330a6465666163696c696f6e3d6263636b636f6465206664316136636537653162336166663264383962643436306438626362613231333234303730343830643232620a'
        str_1 = 'verysecret'
        var_0 = module_0.do_unvault(str_0, str_1, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        ansible_vault_encrypted_unicode_0 = module_1.AnsibleVaultEncryptedUnicode(bool_0)
        bytes_0 = b'\xb69\xa4\x8d\xaa\xf7\xce\x83Z4\xf58\xcb'
        var_0 = module_0.do_unvault(ansible_vault_encrypted_unicode_0, bytes_0)
    except BaseException:
        pass