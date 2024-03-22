# Automatically generated by Pynguin.
import ansible.module_utils.common.dict_transformations as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'key1'
    int_0 = 1
    int_1 = [int_0]
    var_0 = {str_0: int_0, str_0: int_1}
    var_1 = module_0.camel_dict_to_snake_dict(var_0)

def test_case_2():
    bytes_0 = b'-\xfd\x16\x17M\xaf\xc4.2\xe4'
    var_0 = module_0.snake_dict_to_camel_dict(bytes_0)

def test_case_3():
    str_0 = 'Buz'
    var_0 = dict(Bap=str_0)
    str_1 = 'Bing'
    var_1 = dict(Baz=str_0, Boom=str_1)
    var_2 = dict(foo_bar=var_0)
    var_3 = module_0.snake_dict_to_camel_dict(var_2)

def test_case_4():
    bool_0 = None
    var_0 = module_0.snake_dict_to_camel_dict(bool_0)

def test_case_5():
    int_0 = 1
    int_1 = 2
    var_0 = dict(height=int_0, width=int_1)
    var_1 = dict(age=int_0, size=var_0)
    var_2 = dict(age=int_0, size=int_0)
    var_3 = module_0.dict_merge(var_1, var_2)

def test_case_6():
    bool_0 = True
    list_0 = [bool_0]
    tuple_0 = (list_0,)
    var_0 = module_0.dict_merge(bool_0, tuple_0)

def test_case_7():
    str_0 = 'V*v4\x0bg}0Dc}\ngF'
    dict_0 = {str_0: str_0}
    var_0 = module_0.recursive_diff(dict_0, dict_0)

def test_case_8():
    str_0 = 'V*v4\x0bg}0Dc}\ngF'
    dict_0 = {str_0: str_0}
    var_0 = module_0.snake_dict_to_camel_dict(dict_0)
    float_0 = 438.0
    var_1 = module_0.camel_dict_to_snake_dict(dict_0, float_0)

def test_case_9():
    int_0 = 1
    float_0 = -3179.0
    str_0 = 'key'
    int_1 = [int_0]
    var_0 = {str_0: float_0, str_0: int_1, str_0: int_1}
    var_1 = {str_0: int_0, str_0: var_0}
    var_2 = module_0.camel_dict_to_snake_dict(var_1)

def test_case_10():
    str_0 = 'V*v4\x0bg}0Dc}\ngF'
    dict_0 = {str_0: str_0}
    var_0 = module_0.snake_dict_to_camel_dict(dict_0)
    list_0 = [var_0]
    float_0 = 438.0
    var_1 = module_0.snake_dict_to_camel_dict(list_0, float_0)

def test_case_11():
    int_0 = 1
    int_1 = 2
    var_0 = dict(height=int_0, width=int_1)
    var_1 = dict(age=int_0, size=var_0)
    var_2 = dict(height=int_0, depth=int_1)
    var_3 = dict(age=int_0, size=var_2)
    var_4 = module_0.dict_merge(var_1, var_3)

def test_case_12():
    str_0 = 'key1'
    int_0 = 1
    str_1 = 'key2c'
    float_0 = 2.0
    str_2 = 'key'
    int_1 = {str_2: int_0}
    int_2 = [int_1]
    var_0 = {str_1: float_0, str_1: int_2, str_1: int_2}
    var_1 = {str_0: int_0, str_2: var_0}
    var_2 = module_0.camel_dict_to_snake_dict(var_1)

def test_case_13():
    str_0 = 'baz'
    str_1 = 'spam'
    str_2 = 'bar'
    str_3 = 'mux'
    str_4 = 'fiz'
    str_5 = 'bux'
    str_6 = {str_4: str_5}
    str_7 = {str_5: str_5, str_3: str_6}
    str_8 = {str_5: str_2, str_0: str_7, str_1: str_0}
    var_0 = module_0.recursive_diff(str_8, str_8)

def test_case_14():
    str_0 = 'foo'
    str_1 = 'baz'
    str_2 = 'bar'
    str_3 = 'qux'
    str_4 = 'mux'
    str_5 = 'fiz'
    str_6 = 'bux'
    str_7 = {str_5: str_6}
    str_8 = {str_3: str_0, str_4: str_7}
    str_9 = 'eggs'
    str_10 = {str_0: str_2, str_1: str_8, str_1: str_9}
    str_11 = 'sizzle'
    var_0 = None
    str_12 = {str_5: str_6}
    var_1 = {str_3: var_0, str_4: str_12}
    str_13 = 'pop'
    var_2 = {str_0: str_2, str_1: var_1, str_11: str_13}
    var_3 = module_0.recursive_diff(str_10, var_2)

def test_case_15():
    str_0 = 'foo'
    str_1 = 'baz'
    str_2 = 'spam'
    str_3 = 'bar'
    str_4 = 'mux'
    str_5 = 'fiz'
    str_6 = 'bux'
    str_7 = {str_5: str_6}
    str_8 = {str_0: str_0, str_4: str_7}
    str_9 = 'eggs'
    str_10 = {str_0: str_3, str_1: str_8, str_2: str_9}
    str_11 = 'sizzle'
    var_0 = None
    str_12 = {str_5: str_6}
    var_1 = {str_5: var_0, str_4: str_12}
    var_2 = {str_0: str_3, str_1: var_1, str_11: str_5}
    var_3 = module_0.recursive_diff(str_10, var_2)

def test_case_16():
    str_0 = '<o6'
    str_1 = 'baz'
    str_2 = 'spa\n'
    str_3 = 'bar'
    str_4 = 'u'
    str_5 = 'mux'
    str_6 = 'fiz'
    str_7 = 'bx'
    str_8 = {str_6: str_7}
    str_9 = {str_4: str_0, str_5: str_8}
    str_10 = 'eggs'
    str_11 = {str_0: str_3, str_1: str_9, str_2: str_10}
    str_12 = 'sizzle'
    var_0 = {str_5: str_2, str_1: str_6}
    str_13 = 't(N.;Fz-\tA)jXkaN[79\x0c'
    var_1 = {str_0: str_3, str_1: var_0, str_12: str_13}
    var_2 = module_0.recursive_diff(str_11, var_1)

def test_case_17():
    str_0 = 'a'
    str_1 = '_'
    str_2 = 'cD'
    str_3 = 'SubDict'
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = {str_0: int_0, str_1: int_1, str_2: int_2}
    int_4 = {str_0: int_0, str_1: int_1, str_2: int_2, str_3: int_3}
    var_0 = module_0.camel_dict_to_snake_dict(int_4)