# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    str_0 = '='
    var_0 = module_0.is_hop_by_hop_header(str_0)

def test_case_1():
    int_0 = 407
    var_0 = module_0.has_message_body(int_0)

def test_case_2():
    bool_0 = False
    var_0 = module_0.has_message_body(bool_0)
    int_0 = 407
    var_1 = module_0.has_message_body(int_0)

def test_case_3():
    str_0 = '.'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.remove_entity_headers(dict_0)
    str_1 = 'geQX@NiD'
    var_1 = module_0.is_entity_header(str_1)

def test_case_4():
    str_0 = 'content-location'
    str_1 = 'expires'
    str_2 = 'Content-Type'
    str_3 = 'None'
    str_4 = 'Sat, 01 Jan 2020 00:00:00 GMT'
    str_5 = 'application/json'
    str_6 = {str_0: str_3, str_1: str_4, str_2: str_5}
    str_7 = 'Content-Location'
    str_8 = 'Expires'
    str_9 = 'content-type'
    str_10 = {str_7: str_3, str_8: str_4, str_9: str_5}
    var_0 = module_0.remove_entity_headers(str_6)
    var_1 = module_0.remove_entity_headers(str_10)