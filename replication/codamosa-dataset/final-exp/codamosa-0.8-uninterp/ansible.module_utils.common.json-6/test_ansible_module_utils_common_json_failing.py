# Automatically generated by Pynguin.
import ansible.module_utils.common.json as module_0

def test_case_0():
    try:
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.default(ansible_j_s_o_n_encoder_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 2525.73
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(float_0)
        list_0 = []
        bytes_0 = b'K\x81\xbdD7\xc6\xba'
        dict_0 = {ansible_j_s_o_n_encoder_0: var_0, bytes_0: bytes_0}
        bytes_1 = b'9)'
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(bytes_1)
        var_1 = ansible_j_s_o_n_encoder_1.iterencode(dict_0)
        var_2 = ansible_j_s_o_n_encoder_0.default(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(ansible_j_s_o_n_encoder_0)
        list_0 = []
        bytes_0 = b'K\x81\xbdD7\xc6\xba'
        dict_0 = {ansible_j_s_o_n_encoder_0: list_0, bytes_0: bytes_0}
        bytes_1 = b'9)'
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(bytes_1)
        var_1 = ansible_j_s_o_n_encoder_1.iterencode(dict_0)
        ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder(bytes_0)
        var_2 = ansible_j_s_o_n_encoder_2.default(list_0)
    except BaseException:
        pass