# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    try:
        list_0 = None
        var_0 = module_0.is_entity_header(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'j\\'
        var_0 = module_0.has_message_body(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -506
        set_0 = set()
        list_0 = [int_0, int_0, set_0]
        var_0 = module_0.is_hop_by_hop_header(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n        Close the connection if a request is not being sent or received\n\n        :return: boolean - True if closed, false if staying open\n        '
        var_0 = module_0.remove_entity_headers(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '1ndM"6'
        var_0 = module_0.import_string(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 335
        var_0 = module_0.has_message_body(int_0)
        str_0 = '4N)fWU~v5EC.'
        var_1 = module_0.import_string(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'http.server.SimpleHTTPRequestHandler'
        var_0 = module_0.import_string(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x97eb\x8a\xd7<L\xad\xd5\xeb\x86'
        int_0 = 304
        var_0 = module_0.has_message_body(int_0)
        str_0 = 'x?=\x0br8Qr'
        float_0 = -322.9178697999598
        var_1 = module_0.has_message_body(float_0)
        dict_0 = {bytes_0: bytes_0, str_0: float_0}
        var_2 = module_0.remove_entity_headers(dict_0)
        str_1 = 'Response already started'
        var_3 = module_0.is_hop_by_hop_header(str_1)
        int_1 = None
        var_4 = module_0.import_string(int_1)
    except BaseException:
        pass