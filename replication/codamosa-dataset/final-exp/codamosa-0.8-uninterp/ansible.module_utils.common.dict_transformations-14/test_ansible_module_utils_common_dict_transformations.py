# Automatically generated by Pynguin.
import ansible.module_utils.common.dict_transformations as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'L{zN|'
    var_0 = module_0.snake_dict_to_camel_dict(str_0)

def test_case_2():
    bytes_0 = None
    str_0 = "sshpass: invalid option -- 'P'"
    var_0 = module_0.dict_merge(bytes_0, str_0)
    set_0 = {str_0, str_0, str_0, bytes_0}
    dict_0 = {var_0: set_0}
    var_1 = module_0.snake_dict_to_camel_dict(dict_0)
    var_2 = module_0.camel_dict_to_snake_dict(dict_0)

def test_case_3():
    bytes_0 = None
    str_0 = '4Entr PIN\\f_Wr'
    var_0 = module_0.dict_merge(bytes_0, str_0)
    set_0 = {str_0, str_0, str_0, bytes_0}
    dict_0 = {var_0: set_0}
    var_1 = module_0.camel_dict_to_snake_dict(dict_0)
    int_0 = -587
    var_2 = module_0.snake_dict_to_camel_dict(dict_0, int_0)
    var_3 = module_0.recursive_diff(dict_0, dict_0)

def test_case_4():
    tuple_0 = None
    var_0 = module_0.dict_merge(tuple_0, tuple_0)

def test_case_5():
    str_0 = 'Name'
    var_0 = {str_0: str_0, str_0: str_0}
    bool_0 = True
    var_1 = module_0.camel_dict_to_snake_dict(var_0, bool_0, str_0)

def test_case_6():
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = {str_0: str_0, str_1: str_1}
    str_4 = {str_0: str_0, str_1: str_1, str_2: str_3}
    str_5 = {str_0: str_0, str_1: str_1}
    str_6 = {str_0: str_0, str_1: str_1, str_2: str_5}
    var_0 = module_0.recursive_diff(str_4, str_6)

def test_case_7():
    bytes_0 = None
    str_0 = '4Entr PIN\\f_Wr'
    var_0 = module_0.dict_merge(bytes_0, str_0)
    set_0 = {str_0, str_0, str_0, bytes_0}
    dict_0 = {var_0: set_0}
    var_1 = module_0.snake_dict_to_camel_dict(dict_0)
    var_2 = module_0.camel_dict_to_snake_dict(dict_0)
    int_0 = -587
    var_3 = module_0.snake_dict_to_camel_dict(dict_0, int_0)
    var_4 = module_0.recursive_diff(dict_0, dict_0)

def test_case_8():
    str_0 = 'Unit tests for recursive_diff'
    str_1 = 'value1_1_1'
    var_0 = dict(key1_1_1=str_1)
    str_2 = 'value1_2'
    var_1 = dict(key1_1=var_0, key1_2=str_2)
    str_3 = 'value2'
    var_2 = dict(key1=var_1, key2=str_3)
    str_4 = 'value1_3'
    var_3 = dict(key1_1=str_0, key1_3=str_4)
    var_4 = dict(key1=var_3, key2=str_3)
    var_5 = module_0.recursive_diff(var_2, var_4)

def test_case_9():
    str_0 = 'value1_1_1'
    var_0 = dict(key1_1_1=str_0)
    str_1 = 'value1_2'
    var_1 = dict(key1_1=var_0, key1_2=str_1)
    str_2 = 'value2'
    var_2 = dict(key1=var_1, key2=str_2)
    str_3 = 'value1_1_2'
    var_3 = dict(key1_1_1=str_0, key1_1_2=str_3)
    str_4 = 'value1_3'
    var_4 = dict(key1_1=var_3, key1_3=str_4)
    var_5 = dict(key1=var_4, key2=str_2)
    var_6 = module_0.recursive_diff(var_2, var_5)

def test_case_10():
    str_0 = 'prop2'
    str_1 = '{ags'
    str_2 = 'val1'
    str_3 = 'val2'
    str_4 = {str_1: str_2, str_0: str_3}
    str_5 = {str_1: str_2, str_0: str_3, str_1: str_4}
    var_0 = module_0.camel_dict_to_snake_dict(str_5)

def test_case_11():
    str_0 = 'Name'
    str_1 = 'Values'
    str_2 = 'va3w$.Hkf>?-`o'
    str_3 = "s'nd"
    int_0 = 1
    var_0 = {str_3: str_3, str_1: int_0}
    var_1 = [str_2, var_0]
    var_2 = {str_0: str_0, str_1: var_1}
    str_4 = 'values'
    bool_0 = True
    str_5 = [str_4]
    var_3 = module_0.camel_dict_to_snake_dict(var_2, bool_0, str_5)

def test_case_12():
    str_0 = 'Test'
    str_1 = 'dromedaryCase'
    str_2 = 'Value'
    str_3 = 'SubValue'
    str_4 = 'test'
    int_0 = 1
    str_5 = '4'
    str_6 = '|'
    str_7 = [str_5, str_6]
    var_0 = [int_0, int_0, str_1, str_7]
    var_1 = {str_3: str_4, str_5: var_0}
    var_2 = {str_0: str_2, str_1: var_1}
    var_3 = module_0.camel_dict_to_snake_dict(var_2)

def test_case_13():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = 4
    int_4 = 5
    int_5 = 6
    int_6 = 7
    var_0 = dict(G=int_4, H=int_5, I=int_6)
    var_1 = dict(D=int_2, E=int_3, F=var_0)
    var_2 = dict(A=int_0, B=int_1, C=var_1)
    int_7 = 10
    int_8 = 20
    int_9 = 30
    int_10 = 70
    var_3 = dict(I=int_10)
    var_4 = dict(D=int_9, F=var_3)
    var_5 = dict(A=int_7, B=int_8, C=var_4)
    var_6 = module_0.dict_merge(var_2, var_5)
    var_7 = dict(G=int_4, H=int_5, I=int_10)
    var_8 = dict(D=int_9, E=int_3, F=var_7)
    var_9 = dict(A=int_7, B=int_8, C=var_8)
    var_10 = module_0.dict_merge(var_5, var_2)

def test_case_14():
    str_0 = ''
    str_1 = 'b|#&]hp"'
    str_2 = 'Valu\r'
    str_3 = 'SubValue'
    int_0 = 2
    str_4 = 'cs@noORZu*}mHLAz?u_'
    str_5 = '5'
    float_0 = None
    dict_0 = {str_3: str_1, str_4: float_0, str_4: str_1, float_0: str_4}
    tuple_0 = (str_3, dict_0, int_0)
    int_1 = 3766
    var_0 = module_0.dict_merge(tuple_0, int_1)
    tuple_1 = (tuple_0,)
    var_1 = module_0.dict_merge(float_0, tuple_1)
    var_2 = [int_0, int_0, str_5, str_0]
    var_3 = {str_3: str_5, str_2: var_2}
    var_4 = {str_0: str_2, str_1: var_3}
    dict_1 = {str_0: int_0, str_1: str_4}
    var_5 = module_0.snake_dict_to_camel_dict(dict_1)
    str_6 = 'sub_list'
    bytes_0 = b'\xfa\x98\xd0\x10\x1cZ\xa8\x01\xf1\xf1F\xbe\x05\x8e'
    var_6 = module_0.snake_dict_to_camel_dict(dict_1, bytes_0)
    set_0 = {int_0}
    bool_0 = True
    var_7 = module_0.dict_merge(bool_0, set_0)
    dict_2 = {str_6: var_4}
    bytes_1 = b'9r\xe3\x07'
    var_8 = module_0.camel_dict_to_snake_dict(dict_2, bytes_1)

def test_case_15():
    str_0 = 'Values'
    str_1 = 'name'
    str_2 = 'value'
    str_3 = 'string'
    str_4 = {str_1: str_2, str_2: str_3}
    str_5 = 'second'
    int_0 = 1
    var_0 = {str_1: str_5, str_2: int_0}
    var_1 = [str_4, var_0]
    var_2 = {str_0: var_1}
    bool_0 = True
    var_3 = module_0.camel_dict_to_snake_dict(var_2, bool_0, str_0)

def test_case_16():
    str_0 = 'Name'
    str_1 = 'Values'
    str_2 = 'name'
    str_3 = 'value'
    str_4 = {str_2: str_3, str_3: str_2}
    var_0 = {str_0: str_0, str_1: str_4}
    bool_0 = True
    bytes_0 = b'\xac\xf0>v'
    var_1 = module_0.dict_merge(str_2, bytes_0)
    var_2 = module_0.camel_dict_to_snake_dict(var_0, bool_0, str_1)

def test_case_17():
    str_0 = "_'Vj[\nC?p;i:;i"
    var_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    bool_0 = True
    var_1 = module_0.camel_dict_to_snake_dict(var_0, bool_0, str_0)