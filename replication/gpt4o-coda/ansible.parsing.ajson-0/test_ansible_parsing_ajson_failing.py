# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0

def test_case_0():
    try:
        dict_0 = None
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '"3\x0b[gY<Sf!"|u+'
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_0)
    except BaseException:
        pass