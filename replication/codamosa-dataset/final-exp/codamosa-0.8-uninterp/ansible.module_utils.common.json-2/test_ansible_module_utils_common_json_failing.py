# Automatically generated by Pynguin.
import ansible.module_utils.common.json as module_0

def test_case_0():
    try:
        str_0 = None
        str_1 = 'bXN\x0b'
        str_2 = 'L)P(/AoUC'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_1}
        list_0 = [dict_0, str_2, str_2, str_1]
        int_0 = 1635
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder(int_0)
        var_0 = ansible_j_s_o_n_encoder_0.iterencode(list_0)
        str_3 = 'Fv`"M|w-x=*_TS'
        bytes_0 = b'\x88\x95w\x96R\xad\x8eI\xfb\xd5M\xcex\xd9]\xdeb'
        bool_0 = None
        bytes_1 = b'\xf1\xcb\x1a\x0fX#\x15\x01\x0c\xb6\x88\xf4\xb5\xff\xee'
        tuple_0 = (bytes_0, bool_0, bytes_1)
        bytes_2 = b'\xd6i\x147w\x7f\x8a\xa3\x81\xf9\x9b'
        ansible_j_s_o_n_encoder_1 = module_0.AnsibleJSONEncoder(bytes_2)
        var_1 = ansible_j_s_o_n_encoder_1.iterencode(tuple_0)
        var_2 = ansible_j_s_o_n_encoder_0.iterencode(str_3)
        str_4 = 'I_E'
        str_5 = '(uLb(%ewP9QI\x0cq*n-\x0c"N'
        ansible_j_s_o_n_encoder_2 = module_0.AnsibleJSONEncoder(str_5)
        str_6 = '0u<M;g}Vy~'
        dict_1 = {str_0: str_1, str_4: list_0, str_6: str_1}
        ansible_j_s_o_n_encoder_3 = module_0.AnsibleJSONEncoder(**dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        ansible_j_s_o_n_encoder_0 = module_0.AnsibleJSONEncoder()
        var_0 = ansible_j_s_o_n_encoder_0.default(tuple_0)
    except BaseException:
        pass