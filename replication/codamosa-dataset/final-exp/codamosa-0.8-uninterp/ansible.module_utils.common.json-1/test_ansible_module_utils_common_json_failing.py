# Automatically generated by Pynguin.
import ansible.module_utils.common.json as module_0

def test_case_0():
    try:
        dict_0 = {}
        float_0 = -1496.17031
        str_0 = 'R9\\(U5P'
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(str_0, **dict_0)
        dict_1 = {}
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(dict_1)
        var_1 = ansible_j_s_o_n_encoder_0.default(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1230
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.default(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -998.1972
        list_0 = [float_0, float_0]
        int_0 = -3045
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(int_0)
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(list_0)
        var_1 = ansible_j_s_o_n_encoder_0.default(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.default(dict_0)
        var_1 = ansible_j_s_o_n_encoder_0.iterencode(ansible_j_s_o_n_encoder_0)
        str_0 = 'R9\\(U5P'
        ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder(str_0, **dict_0)
        dict_1 = {ansible_j_s_o_n_encoder_2: ansible_j_s_o_n_encoder_1}
        var_2 = ansible_j_s_o_n_encoder_2.iterencode(dict_1)
        var_3 = ansible_j_s_o_n_encoder_2.default(str_0)
    except BaseException:
        pass