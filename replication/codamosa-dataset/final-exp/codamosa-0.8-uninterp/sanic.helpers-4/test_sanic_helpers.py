# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    bytes_0 = b'\x97eb\x8a\xd7<L\xca\xad\xd5\xeb\x86'
    str_0 = 'x?=K\x0b$r8Qr'
    dict_0 = {bytes_0: str_0}
    var_0 = module_0.remove_entity_headers(dict_0)

def test_case_1():
    bool_0 = False
    var_0 = module_0.has_message_body(bool_0)
    var_1 = module_0.has_message_body(bool_0)

def test_case_2():
    str_0 = 'os.path'
    var_0 = module_0.import_string(str_0)
    var_1 = module_0.import_string(str_0)

def test_case_3():
    str_0 = 'Content-Type'
    str_1 = 'application/json'
    str_2 = {str_0: str_1}
    var_0 = module_0.remove_entity_headers(str_2)
    str_3 = 'Content-Location'
    str_4 = 'http://example.com'
    str_5 = {str_0: str_1, str_3: str_4}
    str_6 = 'content-location'
    str_7 = (str_6,)
    var_1 = module_0.remove_entity_headers(str_5, str_7)