# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'www.google.com'
    str_1 = module_0.linkify(str_0)

def test_case_2():
    float_0 = 2401.233
    str_0 = module_0.json_encode(float_0)

def test_case_3():
    str_0 = "w6K'#Vc(9\x0cb~Hsxc3"
    str_1 = module_0.squeeze(str_0)
    str_2 = '. Lists not accepted for security reasons; see '
    var_0 = module_0.url_unescape(str_2)
    str_3 = module_0.json_encode(str_2)
    any_0 = module_0.recursive_unicode(str_1)
    str_4 = module_0.squeeze(str_3)
    any_1 = module_0.recursive_unicode(str_2)

def test_case_4():
    str_0 = '4f^S^'
    str_1 = module_0.url_escape(str_0)

def test_case_5():
    str_0 = ' _'
    var_0 = module_0.url_unescape(str_0, str_0)

def test_case_6():
    bytes_0 = b'\xa9\x084\x16\xfd\x90\xba`\x05n'
    dict_0 = module_0.parse_qs_bytes(bytes_0)

def test_case_7():
    bytes_0 = b'\x1d3'
    var_0 = module_0.url_unescape(bytes_0)
    bool_0 = True
    dict_0 = module_0.parse_qs_bytes(bytes_0, bool_0)
    str_0 = 'Hello http://www.facebook.com/tarekziade tarek@ziade.org'
    bool_1 = True
    bool_2 = False
    str_1 = module_0.linkify(str_0, bool_1, bool_2)

def test_case_8():
    bytes_0 = b'\xa9\x084\x16\xfd\x90\xba`\x05n'
    str_0 = module_0.url_escape(bytes_0)

def test_case_9():
    str_0 = 'Hello http://tornadoweb.org !'
    bool_0 = True
    str_1 = module_0.linkify(str_0, bool_0, str_0)

def test_case_10():
    str_0 = 'H=llo http://tornadoweb.org!'
    bool_0 = False
    str_1 = module_0.linkify(str_0, bool_0)
    str_2 = 'b\x0b'
    str_3 = module_0.url_escape(str_2, bool_0)
    bool_1 = False
    str_4 = '\\'
    list_0 = [str_0, str_4]
    str_5 = module_0.linkify(str_1, str_1, bool_1, list_0)
    str_6 = module_0.xhtml_escape(str_5)
    str_7 = module_0.linkify(str_6, str_5)

def test_case_11():
    str_0 = 'lbuu_X`[aX*|'
    dict_0 = module_0.parse_qs_bytes(str_0)
    optional_0 = module_0.to_unicode(str_0)
    optional_1 = module_0.to_unicode(str_0)
    any_0 = module_0.recursive_unicode(str_0)
    str_1 = module_0.url_escape(str_0)
    optional_2 = module_0.to_unicode(str_0)
    any_1 = module_0.recursive_unicode(dict_0)

def test_case_12():
    str_0 = '<foo http://tornadoweb.org>'
    str_1 = module_0.linkify(str_0)

def test_case_13():
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
    str_6 = "Cannot lad trnslation fr '%s': %"
    str_7 = module_0.linkify(str_5, str_6)
    any_1 = module_0.recursive_unicode(tuple_0)
    str_8 = module_0.squeeze(str_5)
    bool_2 = True
    str_9 = module_0.linkify(str_5, bool_2)
    any_2 = module_0.recursive_unicode(bool_2)
    any_3 = module_0.recursive_unicode(dict_0)
    str_10 = module_0.json_encode(str_3)
    optional_0 = module_0.to_unicode(str_6)

def test_case_14():
    str_0 = 'Hello http://tornadoweb.org!'
    str_1 = module_0.linkify(str_0)
    str_2 = module_0.xhtml_escape(str_1)
    str_3 = module_0.xhtml_unescape(str_2)
    optional_0 = module_0.utf8(str_0)
    str_4 = 'Hello http://www.amazon.com/ASIN/1245'
    bool_0 = True
    str_5 = module_0.linkify(str_4, bool_0)
    str_6 = "title='Test'"
    str_7 = module_0.linkify(str_6)

def test_case_15():
    str_0 = "pT\\,NdJ'w"
    str_1 = module_0.xhtml_escape(str_0)
    str_2 = module_0.json_encode(str_0)
    str_3 = module_0.xhtml_escape(str_0)
    str_4 = module_0.linkify(str_1, str_1)
    str_5 = module_0.xhtml_unescape(str_1)
    str_6 = module_0.json_encode(str_2)
    str_7 = module_0.json_encode(str_3)
    str_8 = 'http://www.google.com/search'
    optional_0 = module_0.to_unicode(str_0)
    str_9 = module_0.squeeze(str_8)
    str_10 = module_0.url_escape(str_5)

def test_case_16():
    str_0 = 'H=llo http://tornadoweb.org!'
    bool_0 = False
    str_1 = module_0.linkify(str_0, bool_0)
    str_2 = 'Hello http://www.amazon.com/ASIN/12345'
    bool_1 = False
    str_3 = '\\'
    var_0 = module_0.url_unescape(str_2, str_0, bool_0)
    list_0 = [str_0, str_3]
    str_4 = module_0.linkify(str_1, str_1, bool_1, list_0)
    str_5 = module_0.xhtml_escape(str_4)
    str_6 = module_0.linkify(str_5, str_4)

def test_case_17():
    str_0 = 'http://www.google.com/search?client=ubuntu&channel=fs&q=php+str_split&ie=utf-8&oe=utf-8'
    str_1 = module_0.linkify(str_0, str_0)

def test_case_18():
    str_0 = 'Hello httF://toYnadoweb.org!'
    str_1 = module_0.linkify(str_0)

def test_case_19():
    str_0 = '\n    hello http://tornadoweb.org/\n    blah blah blah http://www.tornadoweb.org/en/stable/index.html\n    http://www.tornadoweb.org/en/stable/index.html#something\n    blah blah blah\n    '
    str_1 = module_0.linkify(str_0)

def test_case_20():
    str_0 = 'http://tornadoweb.org'
    str_1 = module_0.linkify(str_0)
    bool_0 = True
    str_2 = ''
    str_3 = 'K@{?2XKS4`'
    list_0 = [str_2, str_2, str_2, str_3]
    str_4 = module_0.linkify(str_1, bool_0, str_0, bool_0, list_0)

def test_case_21():
    str_0 = '\n    hello http://tornadoweb.org/\n    blah blah blah http://www.tornadoweb.org/en/stable/index.html\n    http://www.tornadoweb.org/en/stable/index.html#something\n    blah blah blah\n    '
    bool_0 = True
    str_1 = module_0.linkify(str_0, bool_0)

def test_case_22():
    str_0 = '\n    hello http://tornadoweb.org/\n    blah blah blah http://www.tornadoweb.org/en/stable/index.html\n    http://www.tornadoweb.org/en/stable/index.html#something\n    blah blah blah\n    '
    str_1 = module_0.url_escape(str_0)
    str_2 = 'www.example.com'
    bool_0 = True
    str_3 = module_0.linkify(str_0, bool_0)
    str_4 = 'http://www.example.com'
    str_5 = module_0.linkify(str_3)
    bool_1 = False
    str_6 = "sT#BiPb.'!ZZKFA"
    list_0 = [str_6, str_4]
    str_7 = module_0.linkify(str_0, bool_1, str_2, list_0)
    bool_2 = True
    str_8 = module_0.linkify(str_7, bool_2, str_7, bool_2, list_0)

def test_case_23():
    str_0 = 'H=llo http://tornadoweb.org!'
    bool_0 = False
    str_1 = module_0.linkify(str_0, bool_0)
    bool_1 = False
    str_2 = '3'
    list_0 = [str_0, str_2]
    str_3 = module_0.linkify(str_1, str_1, bool_1, list_0)
    str_4 = module_0.xhtml_escape(str_3)
    str_5 = module_0.linkify(str_4, str_3)

def test_case_24():
    str_0 = 'Hello http://www.facebook.com/tarekziade tarek@ziade.org'
    bool_0 = True
    bool_1 = False
    str_1 = module_0.linkify(str_0, bool_0, bool_1)

def test_case_25():
    str_0 = '^,2S<TV^,vu'
    str_1 = module_0.xhtml_unescape(str_0)
    dict_0 = module_0.parse_qs_bytes(str_0)
    optional_0 = module_0.utf8(str_0)
    str_2 = 'http://www.facebook.com/tarekzia'
    bool_0 = True
    str_3 = module_0.linkify(str_2, bool_0)

def test_case_26():
    str_0 = 'Hello http://tornad=web.org!'
    str_1 = module_0.linkify(str_0)
    str_2 = module_0.xhtml_escape(str_1)
    str_3 = module_0.linkify(str_1)
    str_4 = module_0.xhtml_unescape(str_2)
    any_0 = module_0.recursive_unicode(str_2)
    any_1 = module_0.recursive_unicode(str_0)
    optional_0 = module_0.utf8(str_2)
    bool_0 = True
    str_5 = module_0.linkify(str_2, bool_0)
    bool_1 = True
    list_0 = None
    str_6 = module_0.linkify(str_5, bool_1, str_1, list_0)
    bool_2 = True
    str_7 = module_0.linkify(str_0, bool_2)