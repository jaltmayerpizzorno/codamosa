# Automatically generated by Pynguin.
import ansible.parsing.ajson as module_0

def test_case_0():
    try:
        str_0 = 'Ale\x0bT\tr/>lg>)'
        ansible_j_s_o_n_decoder_0 = module_0.AnsibleJSONDecoder()
        var_0 = ansible_j_s_o_n_decoder_0.object_hook(str_0)
    except BaseException:
        pass