# Automatically generated by Pynguin.
import ansible.template.native_helpers as module_0
import ansible.utils.native_jinja as module_1
import ansible.parsing.yaml.objects as module_2
import jinja2.runtime as module_3

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.ansible_native_concat(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        native_jinja_text_0 = module_1.NativeJinjaText()
        dict_0 = {native_jinja_text_0: native_jinja_text_0, native_jinja_text_0: native_jinja_text_0, native_jinja_text_0: native_jinja_text_0, native_jinja_text_0: native_jinja_text_0}
        var_0 = module_0.ansible_native_concat(dict_0)
        var_1 = module_0.ansible_native_concat(dict_0)
        list_0 = [var_1, var_0, native_jinja_text_0, var_1]
        var_2 = module_0.ansible_native_concat(list_0)
        var_3 = module_0.ansible_native_concat(dict_0)
        ansible_vault_encrypted_unicode_0 = module_2.AnsibleVaultEncryptedUnicode(native_jinja_text_0)
        var_4 = module_0.ansible_native_concat(ansible_vault_encrypted_unicode_0)
        list_1 = [native_jinja_text_0, dict_0, native_jinja_text_0, dict_0]
        var_5 = module_0.ansible_native_concat(dict_0)
        var_6 = module_0.ansible_native_concat(list_1)
        var_7 = module_0.ansible_native_concat(dict_0)
        int_0 = 1181
        var_8 = module_0.ansible_native_concat(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'foo'
        strict_undefined_0 = module_3.StrictUndefined(str_0)
        strict_undefined_1 = [strict_undefined_0]
        var_0 = module_0.ansible_native_concat(strict_undefined_1)
    except BaseException:
        pass