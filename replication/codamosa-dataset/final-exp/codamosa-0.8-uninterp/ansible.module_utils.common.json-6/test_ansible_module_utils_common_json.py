# Automatically generated by Pynguin.
import ansible.module_utils.common.json as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = None
    bytes_0 = b'\xc2\x8a'
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(bytes_0)
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(list_0)

def test_case_2():
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()

def test_case_3():
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
    dict_0 = {ansible_j_s_o_n_encoder_0: ansible_j_s_o_n_encoder_0, ansible_j_s_o_n_encoder_0: ansible_j_s_o_n_encoder_0, ansible_j_s_o_n_encoder_0: ansible_j_s_o_n_encoder_0, ansible_j_s_o_n_encoder_0: ansible_j_s_o_n_encoder_0}
    var_0 = ansible_j_s_o_n_encoder_0.default(dict_0)

def test_case_4():
    int_0 = -1245
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(int_0)

def test_case_5():
    dict_0 = {}
    str_0 = '\n        Returns the correct action plugin to handle the requestion task action\n        '
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(str_0)
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(dict_0)

def test_case_6():
    float_0 = 2526.0
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(float_0)
    list_0 = [float_0, ansible_j_s_o_n_encoder_0, var_0, var_0]
    bytes_0 = b'9)'
    ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(bytes_0)
    var_1 = ansible_j_s_o_n_encoder_1.iterencode(list_0)
    ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder()
    dict_0 = {}
    var_2 = ansible_j_s_o_n_encoder_0.default(dict_0)