# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    try:
        bytes_0 = b'\xc29'
        str_0 = module_0.xhtml_unescape(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xc1\xc5yXX\xcc\x14\xe6\xd7\xa4\xdd}\xb4'
        any_0 = module_0.json_decode(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'N%5=q]%oPsM;%lLi'
        optional_0 = module_0.to_unicode(str_0)
        optional_1 = module_0.to_unicode(str_0)
        bool_0 = False
        str_1 = 'ASYNC_TEST_TIMEOUT'
        str_2 = 'nH=KiO^'
        list_0 = [str_2, str_1, str_2, str_2]
        str_3 = module_0.linkify(str_0, bool_0, str_2, list_0)
        bytes_0 = b'_\x9cz77\xb7SK}X\xdb\x8a\x1e'
        optional_2 = None
        dict_0 = module_0.parse_qs_bytes(bytes_0)
        bool_1 = True
        var_0 = module_0.url_unescape(bytes_0, optional_2, bool_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "R'XLn"
        bool_0 = False
        optional_0 = module_0.to_unicode(str_0)
        str_1 = module_0.linkify(str_0, bool_0, bool_0)
        bool_1 = False
        str_2 = 'nH=KiO^'
        list_0 = [str_1, str_1, str_2, str_2]
        str_3 = module_0.linkify(str_0, bool_1, str_0, list_0)
        bytes_0 = b'_\x9cz77\xb7SK}X\xdb\x8a\x1e'
        optional_1 = None
        dict_0 = module_0.parse_qs_bytes(bytes_0)
        var_0 = module_0.url_unescape(bytes_0, optional_1, bool_1)
        str_4 = module_0.linkify(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        optional_0 = module_0.utf8(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xc1\xc5yXX\xcc\x14\x08\xe6\xd7\xa4\xdd}\xb4'
        any_0 = module_0.recursive_unicode(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Q>\\XTp"{w|3y"a\npnnv'
        bool_0 = True
        bool_1 = True
        str_1 = module_0.squeeze(str_0)
        dict_0 = module_0.parse_qs_bytes(str_0, bool_1)
        str_2 = module_0.linkify(str_0, bool_0)
        str_3 = 'G_-&_b%\r:|\x0b7n'
        any_0 = module_0.recursive_unicode(bool_0)
        str_4 = module_0.squeeze(str_3)
        str_5 = 'LC_MESSAGES'
        var_0 = module_0.url_unescape(str_0)
        set_0 = None
        tuple_0 = (str_5, set_0)
        str_6 = "Cannot load translation for '%s': %s"
        str_7 = module_0.linkify(str_5, str_6)
        any_1 = module_0.recursive_unicode(tuple_0)
        str_8 = module_0.squeeze(str_5)
        bool_2 = True
        bytes_0 = b'\xda\xe7K\xd8\x08\x89\x9bt\xcd\xc0\xb4\xb2\xae\xf9\x90'
        str_9 = module_0.linkify(str_5, bool_2)
        any_2 = module_0.recursive_unicode(tuple_0)
        str_10 = module_0.xhtml_unescape(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        any_0 = module_0.recursive_unicode(list_0)
        str_0 = 'li1,,=53P'
        bool_0 = True
        dict_0 = module_0.parse_qs_bytes(str_0, bool_0)
        str_1 = 'LG'
        str_2 = module_0.url_escape(str_1)
        bytes_0 = b'pK\x15\xc4\xe1\xb9\xa1J\xf3\xf9\x84+\x98[y\x17\x81'
        str_3 = 'SlH=U:tMd8~>E'
        any_1 = module_0.recursive_unicode(str_2)
        str_4 = 'V\tW'
        list_1 = [str_3, str_3, str_4, str_3]
        str_5 = module_0.linkify(bytes_0, list_1)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\xb8\x98\xca\xd0\xc9$P\xf14Y&W\xa8'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        list_0 = [bytes_0, bytes_0]
        bool_0 = True
        tuple_0 = (set_0, list_0, bool_0, set_0)
        optional_0 = module_0.to_unicode(tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'Hello http://tornadoweb.org!'
        str_1 = module_0.linkify(str_0)
        str_2 = module_0.xhtml_escape(str_1)
        str_3 = module_0.xhtml_unescape(str_2)
        optional_0 = module_0.utf8(str_0)
        bool_0 = True
        str_4 = module_0.linkify(str_2, bool_0)
        str_5 = 'ZTRr'
        str_6 = module_0.url_escape(str_1)
        bool_1 = False
        list_0 = [str_4, str_5, str_5, str_0]
        str_7 = module_0.linkify(str_4, bool_1, list_0)
    except BaseException:
        pass