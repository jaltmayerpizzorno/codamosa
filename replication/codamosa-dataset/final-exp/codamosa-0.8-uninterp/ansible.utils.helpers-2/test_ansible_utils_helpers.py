# Automatically generated by Pynguin.
import ansible.utils.helpers as module_0

def test_case_0():
    bytes_0 = b'\x18\xcb%\xdf\xf3\x9a\x14x\xea'
    var_0 = module_0.object_to_dict(bytes_0)

def test_case_1():
    int_0 = -186
    str_0 = "-d';=#&MTWXw"
    var_0 = module_0.pct_to_int(int_0, int_0, str_0)
    str_1 = 'vI4e*'
    var_1 = module_0.object_to_dict(str_1)

def test_case_2():
    set_0 = set()
    var_0 = module_0.deduplicate_list(set_0)

def test_case_3():
    int_0 = 1435
    list_0 = [int_0, int_0, int_0]
    bool_0 = True
    var_0 = module_0.object_to_dict(list_0, bool_0)

def test_case_4():
    str_0 = '9'
    var_0 = module_0.deduplicate_list(str_0)

def test_case_5():
    str_0 = 'L-;#\tef?Xf'
    var_0 = module_0.deduplicate_list(str_0)

def test_case_6():
    str_0 = 'attr1'
    str_1 = 'attr2'
    str_2 = 'attr3'
    str_3 = 'a'
    str_4 = 'b'
    str_5 = 'c'
    str_6 = {str_0: str_3, str_1: str_4, str_2: str_5}
    var_0 = module_0.object_to_dict(str_6)
    str_7 = [str_1]
    var_1 = module_0.object_to_dict(str_6, str_7)

def test_case_7():
    int_0 = 75
    int_1 = 100
    var_0 = module_0.pct_to_int(int_0, int_1)
    var_1 = module_0.pct_to_int(int_1, int_1)
    str_0 = '15%'
    var_2 = module_0.pct_to_int(str_0, int_1)

def test_case_8():
    str_0 = '100%'
    int_0 = 100
    var_0 = module_0.pct_to_int(str_0, int_0)
    str_1 = '50%'
    var_1 = module_0.pct_to_int(str_1, int_0)
    str_2 = '0%'
    var_2 = module_0.pct_to_int(str_2, int_0)
    var_3 = module_0.pct_to_int(str_1, int_0)
    float_0 = -1232.0
    float_1 = 0.2
    var_4 = module_0.pct_to_int(float_0, float_1)