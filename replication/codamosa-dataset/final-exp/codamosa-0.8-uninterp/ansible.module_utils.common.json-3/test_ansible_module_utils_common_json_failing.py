# Automatically generated by Pynguin.
import ansible.module_utils.common.json as module_0

def test_case_0():
    try:
        str_0 = 'gMxI*\n%!F}-IS<55B/'
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        dict_0 = {}
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(ansible_j_s_o_n_encoder_0, **dict_0)
        dict_1 = {str_0: str_0}
        ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder(dict_1, dict_1)
        var_0 = ansible_j_s_o_n_encoder_2.iterencode(dict_0)
        var_1 = ansible_j_s_o_n_encoder_2.default(ansible_j_s_o_n_encoder_1)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 2474
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.default(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        bytes_0 = b''
        var_0 = ansible_j_s_o_n_encoder_0.encode(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'show_per_host_start'
        dict_0 = {str_0: str_0}
        float_0 = -12.988
        bytes_0 = b'G\x94\x8fg\ti)Tc\x1eH\xcaM-Zf\x1f\xce\xc1'
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(bytes_0)
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(float_0)
        bool_0 = True
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(bool_0)
        var_1 = ansible_j_s_o_n_encoder_1.iterencode(dict_0, **dict_0)
    except BaseException:
        pass