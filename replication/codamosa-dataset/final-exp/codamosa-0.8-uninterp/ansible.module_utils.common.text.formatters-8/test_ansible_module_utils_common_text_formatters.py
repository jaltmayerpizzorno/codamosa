# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'CollectionModuleUtilLocator can only locate from ansible_collections, got {0}'
    var_0 = module_0.lenient_lowercase(str_0)

def test_case_2():
    bytes_0 = b"=\xb9\xca\xe1\xdd'\x02\x9b2"
    var_0 = module_0.lenient_lowercase(bytes_0)

def test_case_3():
    str_0 = '10M'
    var_0 = module_0.human_to_bytes(str_0)

def test_case_4():
    str_0 = '0'
    var_0 = module_0.human_to_bytes(str_0)

def test_case_5():
    bool_0 = False
    var_0 = module_0.bytes_to_human(bool_0)

def test_case_6():
    int_0 = -1305
    var_0 = module_0.bytes_to_human(int_0, int_0)

def test_case_7():
    int_0 = 1024
    float_0 = 384.7
    var_0 = module_0.bytes_to_human(int_0, float_0)

def test_case_8():
    bool_0 = True
    var_0 = module_0.bytes_to_human(bool_0)

def test_case_9():
    bytes_0 = b'\xa4\x95\xa0\xe3{l\\\xbd\xbb\xe0.\xc2\xbf\x16\x06)<'
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    str_0 = '4Tb'
    bool_0 = True
    var_0 = module_0.human_to_bytes(str_0, bool_0, set_0)
    var_1 = module_0.lenient_lowercase(bytes_0)