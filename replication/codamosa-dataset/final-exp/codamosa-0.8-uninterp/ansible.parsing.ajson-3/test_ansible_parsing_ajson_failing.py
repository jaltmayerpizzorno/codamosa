# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0

def test_case_0():
    try:
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(ansible_j_s_o_n_decoder_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        ansible_j_s_o_n_decoder_1 = module_0.AnsibleJSONDecoder()
        list_0 = [ansible_j_s_o_n_decoder_0, ansible_j_s_o_n_decoder_1, ansible_j_s_o_n_decoder_0]
        var_0 = ansible_j_s_o_n_decoder_1.object_hook(list_0)
    except BaseException:
        pass