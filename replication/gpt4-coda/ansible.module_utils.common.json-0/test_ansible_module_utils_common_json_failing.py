# Automatically generated by Pynguin.
import ansible.module_utils.common.json as module_0

def test_case_0():
    try:
        str_0 = '15y{2sW#* CxR,r4]43'
        dict_0 = {}
        bytes_0 = b'\x80\x1cz?\xb1\xc6\x0b\x98\x8f\xcfF\x83~/\xce\xb2'
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(dict_0, bytes_0)
        list_0 = [bytes_0, dict_0, bytes_0, str_0]
        list_1 = [ansible_j_s_o_n_encoder_0, list_0, dict_0]
        float_0 = -688.1508
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(float_0, **dict_0)
        var_0 = ansible_j_s_o_n_encoder_1.iterencode(list_1)
        ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder(**dict_0)
        var_1 = ansible_j_s_o_n_encoder_0.default(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.default(ansible_j_s_o_n_encoder_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(dict_0, **dict_0)
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder()
        float_0 = None
        var_1 = ansible_j_s_o_n_encoder_1.default(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = None
        int_1 = 5
        float_0 = 1955.59
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(float_0)
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(int_1)
        str_0 = '7?{r5$/E'
        str_1 = 'QP")R`w+JB=K\\\x0c'
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder()
        var_1 = ansible_j_s_o_n_encoder_1.iterencode(str_1)
        list_0 = None
        list_1 = [list_0]
        str_2 = 'Oxsk^m&s//3Rjv\x0c'
        dict_0 = {str_2: float_0}
        var_2 = ansible_j_s_o_n_encoder_0.iterencode(dict_0)
        ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder(str_0, list_1)
        dict_1 = {}
        var_3 = ansible_j_s_o_n_encoder_2.default(dict_1)
        dict_2 = {int_0: int_0, int_0: int_0}
        var_4 = ansible_j_s_o_n_encoder_2.iterencode(dict_2)
        list_2 = [dict_2]
        var_5 = ansible_j_s_o_n_encoder_2.iterencode(int_0)
        ansible_j_s_o_n_encoder_3 = module_0.AnsibleJSONEncoder()
        var_6 = ansible_j_s_o_n_encoder_3.default(list_2)
    except BaseException:
        pass