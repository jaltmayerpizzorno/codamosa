# Automatically generated by Pynguin.
import ansible.module_utils.common.text.converters as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -793
    var_0 = module_0.to_bytes(int_0)

def test_case_2():
    bytes_0 = b'M\xa7M\xff\xed\xed\xfc\xd1\x08{\x87\xf3\xa6<\xd1\xe8'
    var_0 = module_0.to_bytes(bytes_0)

def test_case_3():
    int_0 = 210
    var_0 = module_0.to_text(int_0)

def test_case_4():
    tuple_0 = ()
    var_0 = module_0.jsonify(tuple_0)

def test_case_5():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.container_to_bytes(dict_0)

def test_case_6():
    str_0 = 'A-'
    var_0 = module_0.container_to_bytes(str_0)

def test_case_7():
    int_0 = None
    var_0 = module_0.container_to_text(int_0)

def test_case_8():
    str_0 = 'r3vW+A\raDR;8-dLi]{\x0c('
    str_1 = '  value ? true_val : false_val '
    dict_0 = {}
    str_2 = 'D2'
    list_0 = [str_2]
    tuple_0 = (dict_0, str_2, list_0, dict_0)
    bytes_0 = b'\xd2\x99\xbd\xd2\x8a\xe2\xc9\xd4\xd7(\xe4\xdaaE\xc1\x81\xef'
    var_0 = module_0.to_text(str_0, str_1, tuple_0, bytes_0)
    dict_1 = {}
    var_1 = module_0.jsonify(dict_1, **dict_1)
    bytes_1 = b'\x1a'
    var_2 = module_0.jsonify(bytes_1)

def test_case_9():
    str_0 = 'n4}TV'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.jsonify(dict_0)

def test_case_10():
    str_0 = 'modules'
    dict_0 = {str_0: str_0, str_0: str_0}
    list_0 = [dict_0, str_0]
    var_0 = module_0.jsonify(list_0)
    str_1 = 'yearly'
    dict_1 = {str_1: str_1, str_1: str_1, str_1: str_1}
    var_1 = module_0.container_to_bytes(dict_1)