# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ''
    str_1 = module_0.xhtml_unescape(str_0)

def test_case_2():
    int_0 = 2249
    str_0 = module_0.json_encode(int_0)
    bool_0 = True
    any_0 = module_0.recursive_unicode(bool_0)
    str_1 = '8c$x}\nf\t\rg~]C@Cyu]'
    str_2 = module_0.linkify(str_1)
    str_3 = module_0.xhtml_unescape(str_1)

def test_case_3():
    str_0 = 'e'
    str_1 = module_0.squeeze(str_0)

def test_case_4():
    str_0 = 'S~[03\t#%2.zVr)f0Y%A'
    str_1 = module_0.url_escape(str_0)

def test_case_5():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    str_1 = module_0.linkify(str_0)
    str_2 = module_0.linkify(str_0, str_0)
    bool_0 = False
    str_3 = module_0.linkify(str_1, bool_0, str_2, bool_0)
    str_4 = module_0.xhtml_unescape(str_3)
    var_0 = module_0.url_unescape(str_4)

def test_case_6():
    bytes_0 = b'[o\xa7\x056^\xc4\xd4\xde\xf5.\x04*'
    bool_0 = False
    str_0 = module_0.url_escape(bytes_0, bool_0)

def test_case_7():
    str_0 = 'foo http://www.example.com bar'
    str_1 = module_0.linkify(str_0)

def test_case_8():
    bytes_0 = b'\xdf\xc0J\x83\xa6\xe4\n\xa7G\xcb\x1e\xf5\xfa\xebd3d\x94\xa6'
    bool_0 = True
    optional_0 = module_0.utf8(bytes_0)
    str_0 = module_0.url_escape(bytes_0, bool_0)
    bool_1 = False
    dict_0 = module_0.parse_qs_bytes(str_0, bool_1)
    str_1 = 'p}\tK7]Oo*p)q*(POS|'
    str_2 = module_0.url_escape(str_1)
    str_3 = module_0.json_encode(str_1)
    optional_1 = module_0.to_unicode(str_2)

def test_case_9():
    str_0 = 'Hello http://tornadoweb.rg/1?a=1&b=2!'
    str_1 = module_0.linkify(str_0)

def test_case_10():
    str_0 = '[#-Dx2hDC<#\\rya'
    str_1 = module_0.xhtml_escape(str_0)
    str_2 = '\x0b~FI,,-2^'
    str_3 = module_0.xhtml_unescape(str_2)
    str_4 = module_0.json_encode(str_2)
    var_0 = module_0.url_unescape(str_3)
    str_5 = module_0.squeeze(str_4)
    str_6 = '\n|\nvdogWhw!J.mB'
    str_7 = module_0.linkify(str_6)
    str_8 = module_0.json_encode(str_2)
    dict_0 = module_0.parse_qs_bytes(str_2)
    optional_0 = module_0.to_unicode(str_7)
    any_0 = module_0.recursive_unicode(dict_0)
    optional_1 = module_0.utf8(str_7)
    optional_2 = module_0.utf8(str_5)
    str_9 = module_0.xhtml_unescape(str_1)
    str_10 = module_0.xhtml_unescape(str_0)

def test_case_11():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    str_1 = module_0.linkify(str_0)
    any_0 = module_0.recursive_unicode(str_1)
    str_2 = 'www.facebook.com/profile?=dickbutt'
    str_3 = module_0.linkify(str_0, str_0)
    str_4 = module_0.linkify(str_3, str_2)
    str_5 = module_0.xhtml_unescape(str_4)
    bool_0 = None
    var_0 = module_0.url_unescape(str_4, str_2, bool_0)

def test_case_12():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    str_1 = module_0.url_escape(str_0)
    str_2 = 'www.facebook.com/profile?=dickutt'
    str_3 = module_0.linkify(str_2)
    list_0 = [str_2, str_2, str_3]
    str_4 = module_0.linkify(str_3, list_0)
    bool_0 = None
    str_5 = module_0.xhtml_unescape(str_3)
    var_0 = module_0.url_unescape(str_5, bool_0)

def test_case_13():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    bool_0 = True
    list_0 = []
    str_1 = module_0.linkify(str_0, bool_0, list_0)
    bool_1 = True
    str_2 = module_0.linkify(str_1, bool_1, str_1)
    str_3 = '"_|{s^(1Qq|\x0c'
    bool_2 = False
    str_4 = module_0.linkify(str_1, bool_0, str_3, bool_2)
    str_5 = module_0.xhtml_unescape(str_4)
    any_0 = module_0.recursive_unicode(list_0)
    str_6 = module_0.xhtml_escape(str_2)
    bool_3 = None
    var_0 = module_0.url_unescape(str_1, bool_3)

def test_case_14():
    str_0 = "C#}5R:|4C/DC'K#"
    str_1 = module_0.url_escape(str_0)
    str_2 = module_0.json_encode(str_0)
    str_3 = module_0.linkify(str_2)
    str_4 = module_0.xhtml_unescape(str_3)

def test_case_15():
    str_0 = 'ar_AR}'
    any_0 = module_0.recursive_unicode(str_0)
    str_1 = module_0.squeeze(str_0)
    optional_0 = module_0.utf8(str_0)
    str_2 = '}wSpyi4oksM1'
    bool_0 = True
    dict_0 = module_0.parse_qs_bytes(str_1, bool_0)
    str_3 = "a,];'+ic]APBdX-/}=e"
    bool_1 = True
    str_4 = module_0.linkify(str_3, bool_1)
    bool_2 = False
    bool_3 = None
    bool_4 = None
    dict_1 = module_0.parse_qs_bytes(str_4, bool_3, bool_4)
    optional_1 = module_0.utf8(str_4)
    str_5 = module_0.squeeze(str_0)
    optional_2 = module_0.utf8(str_2)
    optional_3 = module_0.to_unicode(str_1)
    var_0 = module_0.url_unescape(str_1)
    optional_4 = module_0.to_unicode(str_1)
    any_1 = module_0.recursive_unicode(bool_2)
    str_6 = module_0.squeeze(str_5)
    any_2 = module_0.recursive_unicode(dict_0)

def test_case_16():
    str_0 = 'http://wwtfacebook.com/profilX?=ikt'
    str_1 = module_0.linkify(str_0, str_0)

def test_case_17():
    str_0 = 'www.facebook.com/profile?=dickbutt'
    str_1 = module_0.linkify(str_0)
    bool_0 = None
    str_2 = module_0.linkify(str_1, bool_0, str_0, bool_0)

def test_case_18():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    str_1 = module_0.linkify(str_0)
    str_2 = 'www.facebook.com/profile?=dickbutt'
    str_3 = module_0.linkify(str_2)
    bool_0 = True
    str_4 = module_0.linkify(str_2, bool_0)

def test_case_19():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    str_1 = module_0.linkify(str_0)
    str_2 = 'www.facebook.com/profile?=dickbutt'
    bool_0 = True
    str_3 = module_0.linkify(str_0, bool_0)
    bool_1 = True
    str_4 = module_0.linkify(str_2, bool_1, str_1, bool_1)

def test_case_20():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    str_1 = module_0.linkify(str_0)
    str_2 = 'Hello http://www.facebook.com'
    str_3 = module_0.linkify(str_2, str_0)
    bool_0 = False
    bool_1 = False
    list_0 = [str_3]
    str_4 = module_0.linkify(str_2, bool_0, bool_1, list_0)

def test_case_21():
    str_0 = 'http://example.com'
    str_1 = module_0.linkify(str_0, str_0)

def test_case_22():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    str_1 = module_0.linkify(str_0)
    bool_0 = True
    bool_1 = False
    str_2 = module_0.linkify(str_1, bool_0, str_1, bool_1)
    str_3 = 'http://tornadoweb.org'
    str_4 = module_0.linkify(str_2, str_3)

def test_case_23():
    str_0 = 'www.facebook.com/profile'
    str_1 = module_0.linkify(str_0)
    str_2 = module_0.json_encode(str_0)
    bool_0 = None
    str_3 = module_0.linkify(str_2, bool_0, bool_0)
    list_0 = []
    str_4 = module_0.linkify(str_3, str_3, list_0)
    str_5 = module_0.xhtml_unescape(str_0)
    bool_1 = False
    var_0 = module_0.url_unescape(str_1, bool_1)

def test_case_24():
    str_0 = 'http://www.facubook.comiprof[le?=dickbutt'
    bool_0 = True
    list_0 = []
    str_1 = module_0.linkify(str_0, bool_0, list_0)
    bool_1 = False
    str_2 = module_0.linkify(str_1, bool_1, str_1)
    str_3 = '"_|{s^(1Qq|\x0c'
    bool_2 = True
    str_4 = module_0.linkify(str_1, bool_0, str_3, bool_2)
    str_5 = module_0.xhtml_unescape(str_4)
    bool_3 = None
    var_0 = module_0.url_unescape(str_3, bool_3)

def test_case_25():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    bool_0 = True
    list_0 = []
    str_1 = module_0.linkify(str_0, bool_0, list_0)
    str_2 = module_0.xhtml_unescape(str_1)
    bool_1 = False
    str_3 = module_0.json_encode(str_2)
    str_4 = module_0.linkify(str_1, bool_1, str_1)
    str_5 = module_0.linkify(str_2)
    str_6 = module_0.xhtml_unescape(str_2)
    any_0 = module_0.recursive_unicode(str_5)
    bool_2 = None
    none_type_0 = None
    var_0 = module_0.url_unescape(str_5, none_type_0, bool_2)
    str_7 = module_0.xhtml_escape(str_5)

def test_case_26():
    str_0 = 'http://www.facebook.com/profile?=dickbutt'
    str_1 = module_0.url_escape(str_0)
    bool_0 = True
    list_0 = []
    str_2 = module_0.xhtml_escape(str_0)
    str_3 = module_0.linkify(str_0, bool_0, list_0)
    str_4 = module_0.linkify(str_3, bool_0, str_3)
    str_5 = '"|is2(1Qq|'
    str_6 = 'http://www.facebookbcom/profiX?kt'
    bool_1 = False
    optional_0 = module_0.utf8(str_5)
    str_7 = module_0.url_escape(str_3, bool_1)
    str_8 = module_0.linkify(str_6, list_0)
    str_9 = module_0.xhtml_unescape(str_4)
    var_0 = module_0.url_unescape(str_3, str_6)
    var_1 = module_0.url_unescape(str_9, bool_0)