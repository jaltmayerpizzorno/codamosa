# Automatically generated by Pynguin.
import tornado.escape as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'http://console.dvelopers.Roogle.com\\\\\\\\n'
    str_1 = module_0.linkify(str_0)

def test_case_2():
    str_0 = "*7LE:~}Oq.HS'&k\x0bEV"
    str_1 = module_0.xhtml_escape(str_0)
    str_2 = module_0.xhtml_unescape(str_1)

def test_case_3():
    str_0 = 'Google authentication using OAuth2.\n\n    In order to use, register your application with Google and copy the\n    relevant parameters to your application settings.\n\n    * Go to the Google Dev Console at http://console.developers.google.com\n    * Select a project, or create a new one.\n    * In the sidebar on the left, select APIs & Auth.\n    * In the list of APIs, find the Google+ API service and set it to ON.\n    * In the sidebar on the left, select Credentials.\n    * In the OAuth section of the page, select Create New Client ID.\n    * Set the Redirect URI to point to your auth handler\n    * Copy the "Client secret" and "Client ID" to the application settings as\n      ``{"google_oauth": {"key": CLIENT_ID, "secret": CLIENT_SECRET}}``\n\n    .. versionadded:: 3.2\n    '
    bool_0 = True
    str_1 = module_0.linkify(str_0, bool_0, str_0, bool_0)
    str_2 = module_0.json_encode(str_1)

def test_case_4():
    str_0 = 'none'
    str_1 = module_0.squeeze(str_0)

def test_case_5():
    str_0 = 'r6z2;!]X!x@93'
    var_0 = module_0.url_unescape(str_0)
    str_1 = module_0.url_escape(str_0)

def test_case_6():
    bytes_0 = b"'\x87\x9a\\\xb4L'}\xb6\x8b%\xfc"
    dict_0 = None
    bool_0 = False
    var_0 = module_0.url_unescape(bytes_0, dict_0, bool_0)

def test_case_7():
    bytes_0 = b'@\xde\xe6I\x97\x98#\xed\x86~%<5p\xfe\xcbk\xc7'
    bool_0 = False
    bool_1 = False
    dict_0 = module_0.parse_qs_bytes(bytes_0, bool_0, bool_1)

def test_case_8():
    str_0 = 'K%}La'
    dict_0 = module_0.parse_qs_bytes(str_0)
    str_1 = 'https://www.googleapiswcom/oauth20v4/token'
    bool_0 = True
    str_2 = module_0.xhtml_unescape(str_0)
    str_3 = module_0.linkify(str_1, bool_0)
    bool_1 = True
    dict_1 = module_0.parse_qs_bytes(str_2, bool_1)

def test_case_9():
    str_0 = '#'
    optional_0 = module_0.utf8(str_0)

def test_case_10():
    bytes_0 = b'\xc8I\x8e\x82\xa1\x01'
    optional_0 = module_0.utf8(bytes_0)

def test_case_11():
    str_0 = 'http://console.develpers.googlg.com\\n'
    any_0 = module_0.recursive_unicode(str_0)
    str_1 = ''
    bool_0 = True
    str_2 = module_0.linkify(str_0, bool_0)
    dict_0 = module_0.parse_qs_bytes(str_1)

def test_case_12():
    str_0 = '\'"BI)&c~=c\x0cn'
    bool_0 = False
    str_1 = module_0.linkify(str_0, bool_0, str_0)

def test_case_13():
    str_0 = "*7LE:~}Oq.HS'&k\x0bEV"
    str_1 = module_0.xhtml_escape(str_0)
    str_2 = module_0.xhtml_unescape(str_0)
    var_0 = module_0.url_unescape(str_2, str_0)
    str_3 = module_0.xhtml_unescape(str_1)
    str_4 = module_0.url_escape(str_3)
    str_5 = module_0.xhtml_escape(str_2)
    optional_0 = module_0.utf8(str_1)
    any_0 = module_0.recursive_unicode(str_1)
    str_6 = module_0.json_encode(str_2)
    str_7 = module_0.xhtml_escape(str_4)
    str_8 = module_0.xhtml_escape(str_0)
    var_1 = module_0.url_unescape(str_3, str_2)
    any_1 = module_0.recursive_unicode(str_4)
    optional_1 = module_0.utf8(str_5)
    any_2 = module_0.recursive_unicode(str_3)
    bytes_0 = b'\xc7\xde+\xfe\x82\xf6Z?"\xac\xf0z\x15u\xed:B\xfb\xfa\xb9'
    optional_2 = module_0.utf8(bytes_0)
    list_0 = [optional_0]
    any_3 = module_0.recursive_unicode(list_0)

def test_case_14():
    str_0 = 'http://console.develpers.google.com\\'
    bool_0 = False
    str_1 = module_0.linkify(str_0, str_0, bool_0)

def test_case_15():
    str_0 = 'Google authentication using OAuth2.\n\n    In order to use, register your application with Google and copy the\n    relevant parameters to your application settings.\n\n    * Go to the Google Dev Console at http://console.developers.google.com\n    * Select a project, or create a new one.\n    * In the sidebar on the left, select APIs & Auth.\n    * In the list of APIs, find the Google+ API service and set it to ON.\n    * In the sidebar on the left, select Credentials.\n    * In the OAuth section of the page, select Create New Client ID.\n    * Set the Redirect URI to point to your auth handler\n    * Copy the "Client secret" and "Client ID" to the application settings as\n      ``{"google_oauth": {"key": CLIENT_ID, "secret": CLIENT_SECRET}}``\n\n    .. versionadded:: 3.2\n    '
    bool_0 = True
    str_1 = module_0.linkify(str_0, bool_0, str_0, bool_0)

def test_case_16():
    str_0 = 'https://www.googleapiswcom/oauth20v4/token'
    bool_0 = True
    str_1 = module_0.linkify(str_0, bool_0)

def test_case_17():
    str_0 = '\'"A:'
    str_1 = module_0.xhtml_escape(str_0)
    str_2 = "http:/\x0c6_ol.~evel'rs.og.om\\\\\\"
    str_3 = module_0.xhtml_unescape(str_2)
    bool_0 = True
    str_4 = module_0.linkify(str_3, bool_0, str_3, bool_0)
    optional_0 = module_0.utf8(str_0)
    any_0 = module_0.recursive_unicode(str_3)
    str_5 = module_0.url_escape(str_0, bool_0)
    str_6 = module_0.xhtml_unescape(str_1)
    str_7 = module_0.json_encode(str_3)
    str_8 = module_0.json_encode(str_4)
    str_9 = module_0.json_encode(str_8)
    var_0 = module_0.url_unescape(str_9, str_4, bool_0)
    list_0 = []
    str_10 = module_0.linkify(str_9, bool_0, list_0)
    bool_1 = None
    optional_1 = module_0.to_unicode(str_7)
    var_1 = module_0.url_unescape(str_3, bool_1)
    str_11 = module_0.linkify(str_7, str_8)
    var_2 = module_0.url_unescape(str_0)

def test_case_18():
    str_0 = '`~5\x0cD|-&rzm6y;MAa@'
    str_1 = module_0.xhtml_unescape(str_0)
    var_0 = module_0.url_unescape(str_1)
    bool_0 = None
    var_1 = module_0.url_unescape(str_0, bool_0)
    var_2 = module_0.url_unescape(str_0)
    str_2 = 'A-mX]?fj)T~[6A(R.\t\\A'
    optional_0 = module_0.to_unicode(str_2)
    str_3 = module_0.linkify(str_1, str_1)
    any_0 = module_0.recursive_unicode(str_0)