# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'content-type'
    str_1 = 'content-length'
    str_2 = '50'
    str_3 = {str_1: str_2, str_1: str_1, str_1: str_0}
    var_0 = module_0.remove_entity_headers(str_3)

def test_case_2():
    str_0 = "conten't-type"
    str_1 = 'content-length'
    str_2 = '&^.'
    str_3 = 'J>'
    str_4 = 'no-cache'
    str_5 = {str_0: str_2, str_1: str_3, str_3: str_1, str_1: str_4}
    var_0 = module_0.remove_entity_headers(str_5)

def test_case_3():
    int_0 = 261
    var_0 = module_0.has_message_body(int_0)

def test_case_4():
    str_0 = 'content-length'
    str_1 = 'Host'
    str_2 = '100'
    str_3 = '127.0.0.1'
    str_4 = {str_0: str_2, str_1: str_3}
    str_5 = (str_0, str_1)
    var_0 = module_0.remove_entity_headers(str_4, str_5)