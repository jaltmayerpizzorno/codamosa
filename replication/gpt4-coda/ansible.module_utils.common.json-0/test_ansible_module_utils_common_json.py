# Automatically generated by Pynguin.
import ansible.module_utils.common.json as module_0

def test_case_0():
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()

def test_case_1():
    bytes_0 = None
    int_0 = -1219
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(int_0)
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(bytes_0)

def test_case_2():
    str_0 = 'PYP\nc'
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(str_0)
    list_0 = [str_0, ansible_j_s_o_n_encoder_0, ansible_j_s_o_n_encoder_0, ansible_j_s_o_n_encoder_0]
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(list_0)

def test_case_3():
    ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
    str_0 = 'string'
    bytes_0 = b'+3\xe2z\xdeU\xd8\x86\x1a\xf4\xab\xee'
    bool_0 = True
    list_0 = [ansible_j_s_o_n_encoder_0]
    tuple_0 = (ansible_j_s_o_n_encoder_0, bytes_0, bool_0, list_0)
    var_0 = ansible_j_s_o_n_encoder_0.iterencode(tuple_0)
    str_1 = 'yFDVW~:vK#G)}6IM<'
    dict_0 = {}
    var_1 = ansible_j_s_o_n_encoder_0.iterencode(str_1, **dict_0)
    var_2 = ansible_j_s_o_n_encoder_0.iterencode(str_0)
    var_3 = ansible_j_s_o_n_encoder_0.default(dict_0)
    ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(dict_0)