# Automatically generated by Pynguin.
import ansible.utils.helpers as module_0

def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    int_0 = 1270
    var_0 = module_0.object_to_dict(dict_0, int_0)

def test_case_1():
    str_0 = 'zjl'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.object_to_dict(str_0, list_0)

def test_case_2():
    int_0 = -795
    set_0 = {int_0}
    list_0 = [set_0, set_0]
    var_0 = module_0.object_to_dict(list_0)

def test_case_3():
    bytes_0 = b'j\xee];\xed?Wy7r\xe5\xf3\xcd\x85\xd0\xdb\\\x16\xba\x0c'
    var_0 = module_0.deduplicate_list(bytes_0)

def test_case_4():
    str_0 = ':kT\x0csG;(?%^L12%U1-:B'
    var_0 = module_0.deduplicate_list(str_0)

def test_case_5():
    str_0 = '20%'
    int_0 = 100
    var_0 = module_0.pct_to_int(str_0, int_0)
    str_1 = '20'
    var_1 = module_0.pct_to_int(str_1, int_0)
    int_1 = 21
    var_2 = module_0.pct_to_int(int_1, int_0)
    str_2 = '100%'
    var_3 = module_0.pct_to_int(str_2, int_0)
    str_3 = '0%'
    var_4 = module_0.pct_to_int(str_3, int_0)
    int_2 = 0
    var_5 = module_0.pct_to_int(int_2, int_0)
    int_3 = 1
    var_6 = module_0.pct_to_int(int_3, int_0)
    int_4 = 5
    var_7 = module_0.pct_to_int(str_2, int_0, int_4)
    var_8 = module_0.pct_to_int(str_3, int_0, int_4)
    var_9 = module_0.pct_to_int(int_2, int_0, int_4)