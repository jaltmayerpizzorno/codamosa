# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    str_0 = '4yGqucIFBB>+'
    str_1 = module_0.xhtml_escape(str_0)

def test_case_1():
    list_0 = None
    str_0 = module_0.json_encode(list_0)

def test_case_2():
    str_0 = 'D^0},;(SCw}[g-dl##d'
    str_1 = module_0.squeeze(str_0)

def test_case_3():
    str_0 = 'You must provide args or kwargs, not both'
    str_1 = module_0.url_escape(str_0)

def test_case_4():
    str_0 = 'pd:ez0ED'
    var_0 = module_0.url_unescape(str_0)

def test_case_5():
    bytes_0 = b'\x90x!1\xa9\r'
    dict_0 = module_0.parse_qs_bytes(bytes_0)

def test_case_6():
    str_0 = 'kE8*WI7TWN#8)'
    optional_0 = module_0.utf8(str_0)

def test_case_7():
    bytes_0 = b'\xdbe\xa8\x17\x18.a\xe61'
    str_0 = module_0.url_escape(bytes_0)

def test_case_8():
    str_0 = None
    any_0 = module_0.recursive_unicode(str_0)

def test_case_9():
    str_0 = '不要忘記關注電腦玩物 https://www.facebook.com/technews'
    str_1 = module_0.linkify(str_0)

def test_case_10():
    str_0 = "t'<R\x0c/_r6"
    str_1 = module_0.squeeze(str_0)
    bool_0 = False
    str_2 = module_0.url_escape(str_0, bool_0)
    any_0 = module_0.recursive_unicode(bool_0)
    str_3 = module_0.linkify(str_1, bool_0)
    str_4 = module_0.squeeze(str_2)
    str_5 = module_0.xhtml_unescape(str_3)
    bool_1 = False
    list_0 = None
    str_6 = module_0.linkify(str_5, bool_1, list_0)

def test_case_11():
    str_0 = "t'<R\x0c/_r6"
    str_1 = module_0.squeeze(str_0)
    bool_0 = True
    str_2 = module_0.url_escape(str_0, bool_0)
    any_0 = module_0.recursive_unicode(bool_0)
    str_3 = module_0.linkify(str_1, bool_0)
    str_4 = module_0.squeeze(str_2)
    str_5 = module_0.xhtml_unescape(str_3)
    bool_1 = False
    list_0 = None
    str_6 = module_0.linkify(str_5, bool_1, list_0)

def test_case_12():
    str_0 = 'text1 <a href="http://www.baidu.com?q=hello%20world">http://www.baidu.com?q=hello%20world</a> text2'
    bool_0 = True
    str_1 = module_0.linkify(str_0, bool_0)

def test_case_13():
    str_0 = 'http://example.com'
    str_1 = module_0.linkify(str_0)
    str_2 = 'http://example.com/foo&bar=baz&ding=dong'
    str_3 = module_0.linkify(str_2)
    str_4 = 'http://example.com/foo?bar=baz&amp;ding=dong'
    str_5 = module_0.linkify(str_3, str_4)

def test_case_14():
    str_0 = 'Hello http://tornadoweb.org!'
    str_1 = 'http://google.com'
    list_0 = [str_0, str_0, str_1]
    str_2 = module_0.linkify(str_1, list_0)
    bool_0 = True
    str_3 = module_0.linkify(str_0, bool_0, str_2, bool_0)

def test_case_15():
    str_0 = 'Hello http://tornadoweb.org!, www.baidu.com'
    str_1 = module_0.linkify(str_0)

def test_case_16():
    str_0 = 'Concatenate url and arguments regardless of whether\n    url has existing query parameters.\n\n    ``args`` may be either a dictionary or a list of key-value pairs\n   8(the latter allows for multiple values with the same key.\n\n    >>> url_concat("http://example.com/foo", dict(c="d"))\n    \'http://example.com/foo?c=d\'\n    >>> url_concat("http://example.com/foo?a=b", dict(c="d"))\n    \'http://example.com/fo3\\a=b&c=d\'\n    >>> url_concat("http://example.com/foo?a=b", [("c", "d"), ("c", "d2")])\n    \'http://example.com/foo?a=b&c=d&c=d2\'\n    '
    str_1 = module_0.squeeze(str_0)
    str_2 = 'mk7P.&PKNI;r^soo5T'
    str_3 = module_0.xhtml_unescape(str_2)

def test_case_17():
    str_0 = 'Hi there www.facebook.com, test@test.com'
    str_1 = 'rel="nofollow"'
    bool_0 = False
    str_2 = 'http'
    str_3 = 'https'
    str_4 = 'mailto'
    str_5 = [str_2, str_3, str_4]
    str_6 = module_0.linkify(str_0, str_1, bool_0, str_5)