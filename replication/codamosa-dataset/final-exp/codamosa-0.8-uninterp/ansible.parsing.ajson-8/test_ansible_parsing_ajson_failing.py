# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0

def test_case_0():
    try:
        str_0 = 'fo|sO_'
        set_0 = {str_0}
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '__ansible_unsafe'
        str_1 = 'value1'
        str_2 = 'value2'
        str_3 = {str_2: str_1, str_0: str_2}
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_3)
        var_1 = var_0[str_0]
    except BaseException:
        pass