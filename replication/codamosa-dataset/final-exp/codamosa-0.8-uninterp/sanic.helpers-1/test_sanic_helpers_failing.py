# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    try:
        bytes_0 = b'\xc8'
        var_0 = module_0.remove_entity_headers(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        var_0 = module_0.has_message_body(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        var_0 = module_0.is_entity_header(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\\fj)t(GP^'
        var_0 = module_0.import_string(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'http.client'
        var_0 = module_0.import_string(str_0)
        str_1 = 'http.client.error'
        var_1 = module_0.import_string(str_1)
        str_2 = 'http.client.HTTPConnection'
        var_2 = module_0.import_string(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        complex_0 = None
        dict_0 = {complex_0: complex_0, complex_0: complex_0, complex_0: complex_0, complex_0: complex_0}
        var_0 = module_0.remove_entity_headers(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 304
        var_0 = module_0.has_message_body(int_0)
        set_0 = None
        dict_0 = {}
        var_1 = module_0.remove_entity_headers(dict_0)
        bool_0 = False
        var_2 = module_0.has_message_body(bool_0)
        var_3 = module_0.is_hop_by_hop_header(set_0)
    except BaseException:
        pass