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
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.encode(ansible_j_s_o_n_encoder_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        bool_0 = False
        bytes_0 = b'\x13'
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(bytes_0)
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(ansible_j_s_o_n_encoder_0)
        ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder()
        ansible_j_s_o_n_encoder_3 = module_0.AnsibleJSONEncoder()
        dict_1 = {ansible_j_s_o_n_encoder_2: dict_0, ansible_j_s_o_n_encoder_1: ansible_j_s_o_n_encoder_3, ansible_j_s_o_n_encoder_2: bytes_0, bool_0: ansible_j_s_o_n_encoder_3}
        var_0 = ansible_j_s_o_n_encoder_2.default(dict_1)
        bool_1 = True
        ansible_j_s_o_n_encoder_4 = module_0.AnsibleJSONEncoder(bool_1, **dict_0)
        ansible_j_s_o_n_encoder_5 = module_0.AnsibleJSONEncoder()
        var_1 = ansible_j_s_o_n_encoder_3.iterencode(dict_0)
        str_0 = 'W{)7=r\\I^Rro4'
        str_1 = 'l\rh)_{|*ziU8O"\\{|a'
        str_2 = 'i:?;U\nXhqFkQnf~p-_'
        dict_2 = {str_1: str_1, str_0: bool_1, str_2: bool_0, str_1: ansible_j_s_o_n_encoder_1}
        var_2 = ansible_j_s_o_n_encoder_4.iterencode(dict_0, **dict_2)
    except BaseException:
        pass