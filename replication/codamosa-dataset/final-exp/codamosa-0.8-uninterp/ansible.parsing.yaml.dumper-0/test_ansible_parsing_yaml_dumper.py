# Automatically generated by Pynguin.
import ansible.parsing.yaml.dumper as module_0
import ansible.parsing.yaml.objects as module_1
import ansible.template as module_2

def test_case_0():
    pass

def test_case_1():
    var_0 = None
    ansible_dumper_0 = module_0.AnsibleDumper(var_0)
    bool_0 = False
    ansible_unicode_0 = module_1.AnsibleUnicode()
    str_0 = ',\t3b{0mS'
    list_0 = []
    ansible_undefined_0 = module_2.AnsibleUndefined(str_0)
    async_iterator_0 = ansible_undefined_0.__aiter__()
    str_1 = 'EM'
    ansible_vault_encrypted_unicode_0 = module_1.AnsibleVaultEncryptedUnicode(str_1)
    tuple_0 = (str_1, ansible_vault_encrypted_unicode_0)
    dict_0 = {str_1: bool_0, bool_0: str_1}
    ansible_dumper_1 = module_0.AnsibleDumper(async_iterator_0, ansible_undefined_0, tuple_0, dict_0)
    float_0 = -716.32357
    tuple_1 = (list_0, float_0, ansible_unicode_0, float_0)
    var_1 = ansible_dumper_0.represent_data(tuple_1)