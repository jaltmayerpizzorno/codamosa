# Automatically generated by Pynguin.
import ansible.module_utils.common.json as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xfcd\xe62v9\x1e'
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(bytes_0)
    list_0 = None
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(list_0)

def test_case_2():
    list_0 = []
    list_1 = [list_0]
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(list_1)
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(list_0)

def test_case_3():
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()

def test_case_4():
    str_0 = None
    set_0 = set()
    str_1 = 'forks must be greater than or equal to 1'
    str_2 = 'cmdline'
    str_3 = 'w3Ds'
    dict_0 = {str_1: str_0, str_2: str_2, str_3: str_2, str_3: str_2}
    list_0 = [str_0, set_0, str_0]
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(list_0)
    var_0 = ansible_j_s_o_n_encoder_0.default(dict_0)
    ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(str_0, set_0)
    ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder()

def test_case_5():
    bytes_0 = b'\xaeT\xf4\x1c'
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(bytes_0)