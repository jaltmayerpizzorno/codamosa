# Automatically generated by Pynguin.
import ansible.utils.helpers as module_0

def test_case_0():
    bytes_0 = b'\xbc)\x822\xa1\xe1\xa5/+\xa0H*\x1eq'
    var_0 = module_0.object_to_dict(bytes_0)

def test_case_1():
    str_0 = '50%'
    int_0 = 2888
    float_0 = 744.23
    list_0 = [str_0, str_0, str_0, str_0, int_0]
    var_0 = module_0.object_to_dict(float_0, list_0)

def test_case_2():
    str_0 = 'O'
    var_0 = module_0.deduplicate_list(str_0)

def test_case_3():
    str_0 = 'A~3\\o\x0baWJ\x0b'
    var_0 = module_0.deduplicate_list(str_0)

def test_case_4():
    str_0 = '50%'
    int_0 = 209
    var_0 = module_0.pct_to_int(str_0, int_0)

def test_case_5():
    str_0 = '-0%'
    int_0 = 183
    var_0 = module_0.pct_to_int(str_0, int_0)

def test_case_6():
    str_0 = '!l_+HEyplqlf7n6$'
    var_0 = module_0.deduplicate_list(str_0)
    str_1 = 'hex'
    int_0 = 2902
    float_0 = 3477.64
    float_1 = -4257.82402
    var_1 = module_0.object_to_dict(float_1, str_0)
    str_2 = 'ui\x0c\x0brC)'
    list_0 = [str_2, str_1, int_0]
    var_2 = module_0.object_to_dict(float_0, list_0)