# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0
import ansible.utils.unsafe_proxy as module_1

def test_case_0():
    pass

def test_case_1():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()

def test_case_2():
    str_0 = '{"__ansible_vault": "id"}'
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    var_0 = ansible_j_s_o_n_decoder_0.decode(str_0)

def test_case_3():
    str_0 = '`;IwR)F1`lO{&?+wvc9Y'
    str_1 = 'node'
    dict_0 = {str_1: str_0, str_0: str_0, str_0: str_0, str_0: str_1}
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(dict_0)
    ansible_j_s_o_n_decoder_1 = module_0.AnsibleJSONDecoder()

def test_case_4():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    str_0 = '__ansible_unsafe'
    str_1 = '$ANSIBLE_UNSAFE'
    str_2 = {str_0: str_1}
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_2)
    var_1 = module_1.wrap_var(str_1)