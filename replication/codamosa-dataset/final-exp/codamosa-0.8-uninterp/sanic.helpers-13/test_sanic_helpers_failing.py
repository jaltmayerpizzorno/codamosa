# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    try:
        list_0 = []
        var_0 = module_0.has_message_body(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ' .]}B}3{j3lPv;$u'
        int_0 = None
        dict_0 = {int_0: int_0, str_0: str_0, int_0: str_0, str_0: str_0}
        var_0 = module_0.remove_entity_headers(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xd5\x11\xd0\xac'
        var_0 = module_0.remove_entity_headers(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '.Y}B}3{j3lv$u'
        int_0 = None
        dict_0 = {str_0: str_0, int_0: str_0, str_0: str_0}
        var_0 = module_0.remove_entity_headers(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        var_0 = module_0.import_string(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'tests.test_http_helpers'
        var_0 = module_0.import_string(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'os.path'
        var_0 = module_0.import_string(str_0)
        str_1 = 'os.path.abspath'
        var_1 = module_0.import_string(str_1)
    except BaseException:
        pass

def test_case_7():
    try:
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
        float_0 = 923.1412
        var_11 = module_0.import_string(float_0)
    except BaseException:
        pass