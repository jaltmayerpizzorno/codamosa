# Automatically generated by Pynguin.
import ansible.plugins.filter.encryption as module_0
import ansible.parsing.yaml.objects as module_1

def test_case_0():
    try:
        str_0 = 'This is test data from ansible'
        var_0 = module_0.do_vault(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '%s salt=%s'
        int_0 = 393
        var_0 = module_0.do_vault(str_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0, str_0, dict_0]
        bytes_0 = b'Wiu\xa8\rd\xd7\xbb9H\xc4\xba>y\x8a|3'
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        var_1 = module_0.do_vault(dict_0, bytes_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x18L\xffh\xe3;\x9a\n\x9c\xf3V\xd7^\xf2'
        list_0 = [bytes_0, bytes_0]
        var_0 = module_0.do_unvault(bytes_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        filter_module_0 = module_0.FilterModule()
        bytes_0 = b'\x8ca:1]`\xc8\xea\x06\xc2\xad\x97Z'
        var_0 = module_0.do_unvault(filter_module_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$ANSIBLE_VAULT;1.1;AES256'
        var_0 = module_0.do_unvault(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'secret'
        str_1 = 'filter_default'
        str_2 = '$ANSIBLE_VAULT;1.2;AES256;test\n123456789'
        ansible_vault_encrypted_unicode_0 = module_1.AnsibleVaultEncryptedUnicode(str_2)
        var_0 = module_0.do_unvault(ansible_vault_encrypted_unicode_0, str_0, str_1)
    except BaseException:
        pass