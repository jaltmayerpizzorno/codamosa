# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    try:
        bytes_0 = b'\xc7\x05\xd0\x01\t*'
        str_0 = module_0.xhtml_unescape(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'%U'
        bool_0 = True
        str_0 = module_0.linkify(bytes_0, bool_0)
        any_0 = module_0.json_decode(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        tuple_0 = ()
        any_0 = module_0.recursive_unicode(tuple_0)
        str_0 = 'A\\1m^At]'
        dict_0 = module_0.parse_qs_bytes(str_0)
        str_1 = module_0.xhtml_escape(str_0)
        bytes_0 = b'\xd5?\x1b\x88:\xb7\x80Y\xb6K\xfeba\xca'
        str_2 = None
        var_0 = module_0.url_unescape(str_0, str_2, bool_0)
        bool_1 = True
        str_3 = module_0.linkify(bytes_0, bool_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b's\x15\xf4A\x1d\xe2\x9d*\x1a)\n\xfbTQ\x04\xa1qE'
        bool_0 = True
        dict_0 = module_0.parse_qs_bytes(bytes_0, bool_0)
        str_0 = 'http://www.facebook.com/tornadoweb'
        bool_1 = True
        str_1 = module_0.linkify(str_0, str_0)
        str_2 = module_0.linkify(str_0, bool_1, bool_1)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 893.21098
        list_0 = [float_0, float_0, float_0, float_0]
        optional_0 = module_0.utf8(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        none_type_0 = None
        float_0 = 866.21
        str_0 = '.nzXPKeK"T@'
        bool_0 = True
        var_0 = module_0.url_unescape(str_0, bool_0)
        any_0 = module_0.recursive_unicode(float_0)
        optional_0 = module_0.to_unicode(none_type_0)
        dict_0 = {}
        optional_1 = module_0.to_unicode(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'A message with a url (http://www.example.com/) and an email\n    address (user@example.com).'
        bool_0 = True
        str_1 = module_0.linkify(str_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\\2DUJ?gw3kp@xqFl7#\t['
        str_1 = module_0.url_escape(str_0)
        str_2 = module_0.squeeze(str_0)
        var_0 = module_0.url_unescape(str_0, str_0)
        any_0 = module_0.recursive_unicode(str_0)
        bytes_0 = b'\x13\x9em`W\xa3\xda\x13\xcc\xca\x95R\xf0Y3\xff\x84-\xe2'
        bool_0 = False
        var_1 = module_0.url_unescape(bytes_0, str_2, bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'expires_in'
        str_1 = module_0.xhtml_escape(str_0)
        optional_0 = module_0.to_unicode(str_1)
        str_2 = module_0.xhtml_escape(str_0)
        str_3 = module_0.linkify(str_0)
        optional_1 = module_0.to_unicode(str_0)
        bytes_0 = None
        any_0 = module_0.recursive_unicode(str_1)
        bool_0 = False
        optional_2 = module_0.to_unicode(str_1)
        str_4 = module_0.url_escape(str_2, bool_0)
        str_5 = module_0.xhtml_escape(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = False
        tuple_0 = ()
        any_0 = module_0.recursive_unicode(tuple_0)
        str_0 = 'A\\1m^At]'
        dict_0 = module_0.parse_qs_bytes(str_0)
        str_1 = module_0.xhtml_escape(str_0)
        bytes_0 = b'\xd5?\x1b\x88:\xb7\x80Y\xb6K\xfeba\xca'
        str_2 = None
        var_0 = module_0.url_unescape(str_0, str_2, bool_0)
        bool_1 = True
        str_3 = module_0.linkify(bytes_0, bool_1)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'yx'
        str_0 = module_0.xhtml_escape(bytes_0)
        var_0 = module_0.url_unescape(bytes_0, str_0)
        bytes_1 = b'\x1e\xc5=\xd1Z\xf1\xd0'
        tuple_0 = (bytes_1, bytes_0)
        any_0 = module_0.recursive_unicode(tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'http://www.example.cm'
        str_1 = module_0.linkify(str_0)
        bool_0 = True
        str_2 = module_0.xhtml_escape(str_1)
        str_3 = module_0.xhtml_unescape(str_2)
        any_0 = module_0.recursive_unicode(bool_0)
        optional_0 = module_0.utf8(str_0)
        optional_1 = module_0.to_unicode(str_3)
        bool_1 = False
        str_4 = module_0.xhtml_unescape(str_1)
        dict_0 = module_0.parse_qs_bytes(str_4)
        str_5 = module_0.xhtml_escape(str_3)
        str_6 = 'A\\1m^At]'
        dict_1 = module_0.parse_qs_bytes(str_0, bool_0, bool_1)
        optional_2 = module_0.to_unicode(str_6)
        str_7 = module_0.json_encode(str_6)
        str_8 = module_0.xhtml_unescape(str_5)
        str_9 = ' l/g!CT)k>VV}'
        dict_2 = module_0.parse_qs_bytes(str_0)
        str_10 = module_0.xhtml_escape(str_1)
        var_0 = module_0.url_unescape(str_2, str_9)
        list_0 = [str_9, str_10, str_1]
        str_11 = module_0.linkify(str_10, str_8, bool_1, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'aNi\x16'
        var_0 = module_0.url_unescape(bytes_0)
        str_0 = module_0.json_encode(var_0)
        var_1 = module_0.url_unescape(bytes_0, str_0)
        str_1 = 'en1VrH&uH;R'
        str_2 = module_0.xhtml_unescape(str_1)
        str_3 = module_0.xhtml_escape(str_1)
        bytes_1 = b'2\rvlvq\x10b\x0f\xeeI'
        str_4 = module_0.xhtml_escape(bytes_1)
    except BaseException:
        pass