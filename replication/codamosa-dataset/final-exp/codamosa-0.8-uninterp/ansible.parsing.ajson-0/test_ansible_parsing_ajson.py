# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0

def test_case_0():
    pass

def test_case_1():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()

def test_case_2():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    str_0 = '{"__ansible_vault": "xxxx"}'
    var_0 = ansible_j_s_o_n_decoder_0.decode(str_0)

def test_case_3():
    str_0 = None
    float_0 = 2572.131
    list_0 = [str_0, str_0, float_0]
    dict_0 = {str_0: list_0, str_0: str_0}
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(dict_0)

def test_case_4():
    ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
    str_0 = 'test_key'
    str_1 = 'test_value'
    str_2 = {str_0: str_1}
    var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_2)
    str_3 = '__ansible_vault'
    str_4 = 'ansible_vault_encrypted_string'
    str_5 = {str_3: str_4}
    var_1 = ansible_j_s_o_n_decoder_0.object_hook(str_5)
    str_6 = '__ansible_unsafe'
    str_7 = 'ansible_unsafe_string'
    str_8 = {str_6: str_7}
    var_2 = ansible_j_s_o_n_decoder_0.object_hook(str_8)