# Automatically generated by Pynguin.
import ansible.module_utils.common.dict_transformations as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'sr.~#fQ'
    var_0 = module_0.snake_dict_to_camel_dict(str_0)

def test_case_2():
    str_0 = 'my_first_key'
    str_1 = 'my_first_value'
    str_2 = {str_0: str_1}
    str_3 = 'h_t_t_p_endpoint'
    bytes_0 = b'\x14\x19x'
    list_0 = [bytes_0, str_1, str_0, str_2]
    list_1 = [bytes_0, str_3, str_3]
    var_0 = module_0.snake_dict_to_camel_dict(list_0, list_1)

def test_case_3():
    str_0 = 'my_http_endpoint'
    str_1 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.camel_dict_to_snake_dict(str_1)
    bool_0 = True
    var_1 = module_0.camel_dict_to_snake_dict(str_1, bool_0)
    var_2 = module_0.snake_dict_to_camel_dict(var_1)

def test_case_4():
    bool_0 = True
    str_0 = 'Tar\x0bgetGroupARNs'
    str_1 = 'test'
    str_2 = {str_0: str_1}
    var_0 = module_0.camel_dict_to_snake_dict(str_2, bool_0)

def test_case_5():
    float_0 = None
    bool_0 = True
    var_0 = module_0.dict_merge(float_0, bool_0)

def test_case_6():
    int_0 = -13
    str_0 = 'd'
    int_1 = {str_0: int_0, str_0: int_0, str_0: int_0}
    var_0 = module_0.recursive_diff(int_1, int_1)

def test_case_7():
    float_0 = 916.1069340262536
    str_0 = 'ANSIBLE_HTTPAPI_PLUGINS'
    dict_0 = {}
    var_0 = module_0.camel_dict_to_snake_dict(dict_0)
    var_1 = module_0.dict_merge(str_0, dict_0)
    var_2 = module_0.snake_dict_to_camel_dict(float_0)

def test_case_8():
    str_0 = 'b'
    str_1 = 'c'
    str_2 = '1'
    str_3 = 'd'
    str_4 = 'e'
    str_5 = '2'
    str_6 = 'f'
    str_7 = 'g'
    str_8 = '3'
    str_9 = '4'
    str_10 = {str_6: str_8, str_7: str_9}
    str_11 = {str_3: str_5, str_4: str_10}
    str_12 = {str_0: str_2, str_1: str_11}
    str_13 = 'h'
    str_14 = 'i'
    str_15 = '5'
    str_16 = '6'
    str_17 = {str_6: str_15, str_14: str_16}
    str_18 = {str_4: str_17}
    str_19 = '7'
    str_20 = {str_1: str_18, str_13: str_19}
    var_0 = module_0.dict_merge(str_12, str_20)

def test_case_9():
    str_0 = 'my_first_key'
    str_1 = {str_0: str_0}
    str_2 = {str_0: str_0, str_0: str_1}
    var_0 = module_0.camel_dict_to_snake_dict(str_2)

def test_case_10():
    int_0 = -13
    str_0 = 'd'
    int_1 = {str_0: int_0, str_0: int_0}
    int_2 = {str_0: int_0, str_0: int_0, str_0: int_1}
    var_0 = module_0.recursive_diff(int_2, int_2)

def test_case_11():
    int_0 = -10
    int_1 = 2
    str_0 = 'd'
    str_1 = '?K'
    int_2 = -7
    int_3 = {str_0: int_1, str_1: int_2}
    int_4 = {str_0: int_0, str_1: int_3, str_1: int_3}
    var_0 = module_0.recursive_diff(int_4, int_3)

def test_case_12():
    int_0 = -10
    str_0 = 'd'
    str_1 = 'iK'
    int_1 = 3
    int_2 = {str_0: int_1, str_1: int_1}
    int_3 = {str_0: int_0, str_1: int_1, str_1: int_2}
    int_4 = {str_1: int_0, str_1: int_1, str_1: int_2}
    var_0 = module_0.recursive_diff(int_3, int_4)

def test_case_13():
    str_0 = '\n#1'
    str_1 = 'c'
    int_0 = 1
    int_1 = 2
    str_2 = 'd'
    str_3 = 'e'
    int_2 = 3
    int_3 = 4
    int_4 = {str_2: int_2, str_3: int_3}
    int_5 = {str_0: int_0, str_3: int_1, str_1: int_4}
    int_6 = 5
    int_7 = {str_2: int_2, str_3: int_6}
    int_8 = {str_0: int_0, str_3: int_1, str_1: int_7}
    var_0 = module_0.recursive_diff(int_5, int_8)

def test_case_14():
    int_0 = 1
    int_1 = 2
    str_0 = 'd'
    str_1 = 'e'
    int_2 = 3
    int_3 = 4
    int_4 = {str_0: int_2, str_1: int_3}
    int_5 = {str_0: int_0, str_0: int_2, str_0: int_4}
    int_6 = {str_1: int_0, str_0: int_1, str_0: int_4}
    var_0 = module_0.recursive_diff(int_5, int_6)

def test_case_15():
    bool_0 = True
    str_0 = 'Tar\x0bgetGroupARNs'
    str_1 = 'test'
    str_2 = [str_0, str_1]
    str_3 = {str_0: str_2}
    var_0 = module_0.camel_dict_to_snake_dict(str_3, bool_0)

def test_case_16():
    str_0 = 'InstanceName'
    str_1 = 'SystemDisk'
    str_2 = 'Tags'
    str_3 = 'DiskSize'
    int_0 = 40
    str_4 = 'Key'
    str_5 = 'Value'
    str_6 = 'TestKey1'
    str_7 = {str_4: str_6, str_5: str_3}
    str_8 = [str_7]
    var_0 = {str_0: str_8, str_1: int_0, str_2: str_5}
    bool_0 = True
    var_1 = module_0.camel_dict_to_snake_dict(var_0, bool_0)

def test_case_17():
    str_0 = 'testCamelCaseTag'
    str_1 = 'testDict'
    str_2 = 'Tags'
    var_0 = [str_1]
    var_1 = {str_0: var_0}
    var_2 = [var_1]
    str_3 = "-<ng'"
    str_4 = [str_3, str_1]
    str_5 = 'tag1'
    str_6 = 'tag2'
    str_7 = [str_5, str_6]
    str_8 = 'string'
    str_9 = {str_6: str_8}
    str_10 = {str_5: str_9}
    str_11 = 'Key'
    str_12 = 'Value'
    str_13 = 'A'
    str_14 = {str_11: str_13, str_12: str_2}
    str_15 = 'D'
    str_16 = {str_11: str_5, str_8: var_2, str_13: str_3, str_12: str_15}
    str_17 = [str_4, str_14, str_16]
    var_3 = {str_13: var_2, str_8: str_4, str_0: str_7, str_1: str_10, str_2: str_17, str_8: str_8}
    bool_0 = True
    var_4 = module_0.camel_dict_to_snake_dict(var_3, bool_0)

def test_case_18():
    str_0 = 'testDict'
    str_1 = 'Tags'
    var_0 = [str_0]
    str_2 = "-<ng'"
    str_3 = [str_2, str_0]
    str_4 = 'tag1'
    str_5 = 'tag2'
    str_6 = [str_4, str_5]
    str_7 = 'string'
    str_8 = {str_5: str_7}
    str_9 = {str_4: str_8}
    str_10 = '_\x0b'
    str_11 = 'Value'
    str_12 = 'H'
    str_13 = {str_10: str_12, str_11: str_1}
    str_14 = 'D'
    str_15 = {str_10: str_4, str_7: var_0, str_12: str_2, str_11: str_14}
    list_0 = [str_8, str_6]
    bytes_0 = b''
    int_0 = None
    dict_0 = {str_7: bytes_0, int_0: str_5, str_4: str_8, str_5: str_4}
    var_1 = module_0.snake_dict_to_camel_dict(list_0, dict_0)
    str_16 = [str_3, str_13, str_15]
    set_0 = set()
    tuple_0 = (list_0, bytes_0, int_0)
    var_2 = module_0.dict_merge(set_0, tuple_0)
    var_3 = {str_12: var_0, str_7: str_3, str_7: str_6, str_0: str_9, str_1: str_16, str_7: str_7}
    bool_0 = True
    var_4 = module_0.camel_dict_to_snake_dict(var_3, bool_0)

def test_case_19():
    str_0 = 'testCamelCaseTag'
    str_1 = 'testDict'
    str_2 = 'Tags'
    var_0 = {str_0: str_1}
    var_1 = [var_0]
    str_3 = "-<ng'"
    str_4 = [str_3, str_1]
    str_5 = 'tag1'
    str_6 = ''
    str_7 = [str_5, str_6]
    str_8 = 'HTTPEndpoint'
    str_9 = {str_6: str_8}
    str_10 = {str_5: str_9}
    str_11 = 'Key'
    float_0 = 3059.342
    var_2 = module_0.snake_dict_to_camel_dict(float_0)
    str_12 = 'Value'
    str_13 = 'a>?*p_g'
    str_14 = {str_11: str_13, str_12: str_2}
    str_15 = 'D'
    str_16 = {str_11: str_5, str_8: var_1, str_13: str_3, str_12: str_15}
    list_0 = [str_9, str_7]
    bytes_0 = b''
    int_0 = None
    dict_0 = {str_8: bytes_0, int_0: str_6, str_5: str_9, str_6: str_5}
    var_3 = module_0.snake_dict_to_camel_dict(list_0, dict_0)
    str_17 = [str_4, str_14, str_16]
    set_0 = set()
    tuple_0 = (list_0, bytes_0, int_0)
    var_4 = module_0.dict_merge(set_0, tuple_0)
    var_5 = {str_13: var_1, str_8: str_4, str_0: str_7, str_1: str_10, str_2: str_17, str_8: str_8}
    bool_0 = True
    var_6 = module_0.camel_dict_to_snake_dict(var_5, bool_0)