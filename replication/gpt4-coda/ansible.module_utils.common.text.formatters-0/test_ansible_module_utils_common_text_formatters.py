# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    var_0 = module_0.lenient_lowercase(dict_0)

def test_case_2():
    bytes_0 = b'lH\xc74\xd2\x18ID\x0c'
    var_0 = module_0.lenient_lowercase(bytes_0)

def test_case_3():
    float_0 = 4933.74
    var_0 = module_0.human_to_bytes(float_0)

def test_case_4():
    bytes_0 = b'\xb5\xf1\x1cPmv\xeb\x92h\xa6\x99p\x92x\x02\xef'
    int_0 = -2120
    str_0 = '_ZF_,"W(\rA(NZ-KQB'
    var_0 = module_0.bytes_to_human(int_0, str_0)
    var_1 = module_0.lenient_lowercase(bytes_0)
    var_2 = module_0.lenient_lowercase(bytes_0)

def test_case_5():
    int_0 = -1862
    var_0 = module_0.bytes_to_human(int_0)
    str_0 = '5'
    str_1 = 'mBK\t7FB%|`Y*?&wsnco'
    var_1 = module_0.human_to_bytes(str_0, str_1)