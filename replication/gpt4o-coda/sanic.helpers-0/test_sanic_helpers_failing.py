# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    try:
        float_0 = 0.001
        var_0 = module_0.is_hop_by_hop_header(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = None
        var_0 = module_0.remove_entity_headers(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        var_0 = module_0.import_string(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1I{2\\,_h/}Sk^'
        bytes_0 = b'w\xa8\xb5=\x18\xce\xe1\xe8o\x1f`\xfc\x9f'
        dict_0 = {str_0: bytes_0}
        var_0 = module_0.remove_entity_headers(dict_0)
        bool_0 = True
        int_0 = 204
        var_1 = module_0.has_message_body(int_0)
        float_0 = 400.716155
        var_2 = module_0.remove_entity_headers(float_0, bool_0)
    except BaseException:
        pass