# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'~\x07\xc2\x1d\xcf\xce\xd5Cu\xe7[K\xd5W#'
    var_0 = module_0.is_entity_header(bytes_0)

def test_case_2():
    int_0 = 198
    str_0 = '\t7u%p5hC'
    var_0 = module_0.has_message_body(int_0)
    var_1 = module_0.is_entity_header(str_0)

def test_case_3():
    str_0 = '0GG#\nnfe<o'
    dict_0 = {str_0: str_0}
    var_0 = module_0.remove_entity_headers(dict_0)

def test_case_4():
    int_0 = 100
    var_0 = module_0.has_message_body(int_0)
    int_1 = 101
    var_1 = module_0.has_message_body(int_1)
    int_2 = 102
    var_2 = module_0.has_message_body(int_2)
    int_3 = 103
    var_3 = module_0.has_message_body(int_3)
    int_4 = 200
    var_4 = module_0.has_message_body(int_4)
    int_5 = 201
    var_5 = module_0.has_message_body(int_5)
    int_6 = 202
    var_6 = module_0.has_message_body(int_6)
    int_7 = 203
    var_7 = module_0.has_message_body(int_7)
    int_8 = 204
    var_8 = module_0.has_message_body(int_8)
    int_9 = 205
    var_9 = module_0.has_message_body(int_9)
    int_10 = 206
    var_10 = module_0.has_message_body(int_10)
    int_11 = 207
    var_11 = module_0.has_message_body(int_11)
    int_12 = 208
    var_12 = module_0.has_message_body(int_12)
    int_13 = 226
    var_13 = module_0.has_message_body(int_13)
    int_14 = 300
    var_14 = module_0.has_message_body(int_14)

def test_case_5():
    str_0 = 'content-location'
    str_1 = 'expires'
    str_2 = 'hre'
    str_3 = 'soon'
    str_4 = {str_0: str_2, str_1: str_3}
    var_0 = module_0.remove_entity_headers(str_4)
    str_5 = 'other'
    str_6 = 'value'
    str_7 = {str_0: str_2, str_1: str_3, str_5: str_6}
    str_8 = (str_5,)
    var_1 = module_0.remove_entity_headers(str_7, str_8)