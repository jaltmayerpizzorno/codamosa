# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0

def test_case_0():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()

def test_case_1():
    list_0 = []
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(list_0)

def test_case_2():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    str_0 = '{"__ansible_vault": "$ANSIBLE_VAULT;1.1;AES256\\n...encrypted_data..."}'
    var_0 = ansible_j_s_o_n_decoder_0.decode(str_0)

def test_case_3():
    list_0 = []
    str_0 = 'i4*K'
    dict_0 = {str_0: list_0}
    dict_1 = {}
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder(**dict_1)
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(dict_0)