# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0

def test_case_0():
    pass

def test_case_1():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()

def test_case_2():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    str_0 = '__ansible_vault'
    str_1 = {str_0: str_0}
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_1)

def test_case_3():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    str_0 = '__ansible_vault'
    str_1 = {ansible_j_s_o_n_decoder_0: str_0, ansible_j_s_o_n_decoder_0: ansible_j_s_o_n_decoder_0, str_0: ansible_j_s_o_n_decoder_0}
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_1)

def test_case_4():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    str_0 = 'Vault-1'
    str_1 = '__ansible_vault'
    str_2 = '__ANSIBLE_VAULT__'
    str_3 = 'b'
    str_4 = {str_1: str_2, str_3: str_3}
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_4)
    str_5 = '__ansible_unsafe'
    str_6 = {str_5: str_0}
    var_1 = ansible_j_s_o_n_decoder_0.object_hook(str_6)