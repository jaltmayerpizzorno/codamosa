# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    try:
        bytes_0 = b'\xee\r\xe9\x99\xe4kb\xd3\x9a\xc45'
        var_0 = module_0.has_message_body(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        var_0 = module_0.remove_entity_headers(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "' U\rSe8U m~]YRJ]2#,L"
        float_0 = 2812.71
        set_0 = {str_0, float_0, str_0}
        dict_0 = {str_0: str_0, float_0: str_0, str_0: set_0}
        var_0 = module_0.remove_entity_headers(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        var_0 = module_0.has_message_body(bool_0)
        bool_1 = None
        var_1 = module_0.is_hop_by_hop_header(bool_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'inspect.ismodule'
        str_1 = 'importlib'
        var_0 = module_0.import_string(str_0, str_1)
    except BaseException:
        pass