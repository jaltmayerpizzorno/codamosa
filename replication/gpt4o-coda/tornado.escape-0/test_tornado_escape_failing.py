# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    try:
        bytes_0 = b'.\xa4q\xfe\xeb\xd1\x9d\xc6e\x83\xf2dp\x81\xd6'
        str_0 = module_0.xhtml_unescape(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '9UR,P!"j'
        any_0 = module_0.json_decode(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'R\xd1\xdf~\x04\x95\xf5\x13\xf33'
        none_type_0 = None
        bool_0 = True
        var_0 = module_0.url_unescape(bytes_0, none_type_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'Y\x1d_\xda~\xea\xa0/\xf3R\xaa\x06`\xd3\xc0@\x0b\xedh\xc5'
        var_0 = module_0.url_unescape(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'R\xd1\xdf~\x04\x95\xf5\x13\xf33'
        none_type_0 = None
        bool_0 = False
        var_0 = module_0.url_unescape(bytes_0, none_type_0, bool_0)
        optional_0 = module_0.to_unicode(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '|44FY6]\t/6t4!Y'
        bool_0 = True
        bool_1 = False
        dict_0 = module_0.parse_qs_bytes(str_0, bool_0, bool_1)
        bytes_0 = b'|\x8ex\xb1\x18P\x80'
        any_0 = module_0.json_decode(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 300.9
        optional_0 = module_0.to_unicode(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\xf0\x80\xd8\x0e\xca\x1a\xf9'
        any_0 = module_0.recursive_unicode(bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '#}*ea0,$(U$:`9]zjw&c'
        str_1 = module_0.xhtml_unescape(str_0)
        optional_0 = module_0.utf8(str_0)
        str_2 = module_0.url_escape(str_0)
        bool_0 = False
        str_3 = 'CHWa$@'
        bool_1 = True
        dict_0 = module_0.parse_qs_bytes(str_3, bool_1)
        str_4 = module_0.url_escape(str_2, bool_0)
        bytes_0 = None
        str_5 = module_0.url_escape(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -852
        str_0 = module_0.json_encode(int_0)
        bool_0 = False
        var_0 = module_0.url_unescape(str_0, str_0, bool_0)
        bytes_0 = b'\xd1\x0e\x94!\xaaL\n\x82?'
        optional_0 = module_0.utf8(bytes_0)
        str_1 = 'J1](;b|'
        dict_0 = module_0.parse_qs_bytes(str_1)
        str_2 = module_0.json_encode(dict_0)
        dict_1 = module_0.parse_qs_bytes(str_1)
        bool_1 = False
        str_3 = module_0.linkify(str_1, str_1, bool_1)
        bool_2 = False
        var_1 = module_0.url_unescape(bytes_0, bool_2)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '[aIkN90e+AMtNUn\n'
        any_0 = module_0.recursive_unicode(str_0)
        str_1 = module_0.xhtml_escape(str_0)
        str_2 = 'rr6m?Za\\*vs!'
        str_3 = module_0.xhtml_escape(str_2)
        str_4 = module_0.squeeze(str_1)
        str_5 = module_0.json_encode(str_1)
        bytes_0 = None
        bytes_1 = b'\xe9'
        bytes_2 = b'\x8b.3'
        list_0 = [bytes_0, bytes_1, bytes_2]
        str_6 = None
        dict_0 = {str_2: list_0, str_6: list_0, str_4: list_0, str_4: list_0}
        tuple_0 = (str_2, dict_0)
        any_1 = module_0.recursive_unicode(tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        dict_0 = {}
        optional_0 = module_0.utf8(dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = None
        bool_0 = True
        str_0 = 'l~{vIoN!vYB{|'
        tuple_0 = (bytes_0, bool_0, str_0)
        optional_0 = module_0.utf8(str_0)
        any_0 = module_0.recursive_unicode(tuple_0)
        str_1 = 'J~p-U3fJ-k)-5c"g9w6'
        str_2 = module_0.xhtml_unescape(str_1)
        bytes_1 = b''
        dict_0 = module_0.parse_qs_bytes(bytes_1)
        bool_1 = None
        str_3 = None
        list_0 = [str_3, str_3, str_3, str_3]
        str_4 = module_0.linkify(bytes_1, bool_1, list_0)
    except BaseException:
        pass