# Automatically generated by Pynguin.
import ansible.template.native_helpers as module_0
import ansible.parsing.yaml.objects as module_1
import jinja2.runtime as module_2

def test_case_0():
    try:
        bool_0 = True
        list_0 = [bool_0]
        tuple_0 = (list_0, list_0)
        var_0 = module_0.ansible_native_concat(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xb1\xd3\xf4>Q[\xf6s\x00'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        list_0 = []
        set_0 = set()
        tuple_0 = (set_0, dict_0, dict_0)
        var_0 = module_0.ansible_native_concat(tuple_0)
        var_1 = module_0.ansible_native_concat(set_0)
        var_2 = module_0.ansible_native_concat(list_0)
        var_3 = module_0.ansible_native_concat(tuple_0)
        var_4 = module_0.ansible_native_concat(dict_0)
        var_5 = module_0.ansible_native_concat(list_0)
        str_0 = '}9D\x0b\n^]3j9hO'
        var_6 = module_0.ansible_native_concat(str_0)
        float_0 = None
        var_7 = module_0.ansible_native_concat(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '{{ [1, 2, 3] }}'
        var_0 = module_0.ansible_native_concat(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        ansible_vault_encrypted_unicode_0 = module_1.AnsibleVaultEncryptedUnicode(list_0)
        var_0 = module_0.ansible_native_concat(ansible_vault_encrypted_unicode_0)
        str_0 = '$06'
        dict_0 = {ansible_vault_encrypted_unicode_0: str_0}
        var_1 = module_0.ansible_native_concat(dict_0)
        var_2 = module_0.ansible_native_concat(dict_0)
        str_1 = 'scutil'
        var_3 = module_0.ansible_native_concat(str_1)
        set_0 = {str_0}
        var_4 = module_0.ansible_native_concat(set_0)
        float_0 = -4010.3
        var_5 = module_0.ansible_native_concat(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'undefined_2'
        strict_undefined_0 = module_2.StrictUndefined()
        strict_undefined_1 = module_2.StrictUndefined()
        strict_undefined_2 = {str_0: strict_undefined_0, str_0: strict_undefined_1}
        str_1 = 'a'
        str_2 = 'b'
        str_3 = 'c'
        var_0 = [str_1, strict_undefined_2, str_2, str_3]
        var_1 = module_0.ansible_native_concat(var_0)
    except BaseException:
        pass