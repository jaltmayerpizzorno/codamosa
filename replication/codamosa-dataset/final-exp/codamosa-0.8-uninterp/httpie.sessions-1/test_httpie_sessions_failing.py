# Automatically generated by Pynguin.
import httpie.cli.dicts as module_0
import pathlib as module_1
import httpie.sessions as module_2

def test_case_0():
    try:
        request_headers_dict_0 = module_0.RequestHeadersDict()
        path_0 = module_1.Path()
        str_0 = "u'mH"
        session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_0)
        str_1 = '$D4Mo;1V,~rc@bkd42h?'
        iterable_0 = None
        session_1 = module_2.Session(str_1)
        var_0 = session_1.remove_cookies(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        path_0 = module_1.Path(**dict_0)
        request_headers_dict_0 = module_0.RequestHeadersDict()
        str_0 = ''
        str_1 = 'Luj\n,m:6-h.?&'
        session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_1)
        var_0 = session_0.update_headers(request_headers_dict_0)
        session_1 = module_2.Session(path_0)
        list_0 = [session_1, str_0, str_0, request_headers_dict_0]
        session_2 = module_2.Session(path_0)
        var_1 = session_1.remove_cookies(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '<'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        path_0 = module_1.Path(**dict_0)
        str_1 = '+:r'
        request_headers_dict_0 = module_0.RequestHeadersDict()
        session_0 = module_2.Session(str_1)
        var_0 = session_0.remove_cookies(session_0)
        str_2 = '\tr9NV _tWZ'
        session_1 = module_2.get_httpie_session(path_0, str_2, str_2, str_2)
        session_2 = module_2.Session(path_0)
        request_headers_dict_1 = module_0.RequestHeadersDict(session_2)
        session_3 = module_2.Session(str_0)
        var_1 = session_1.update_headers(request_headers_dict_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        session_0 = module_2.Session(str_0)
        str_1 = 'User-Agent'
        str_2 = 'Accept'
        str_3 = 'Cookie'
        str_4 = 'Content-Type'
        str_5 = 'If-Match'
        str_6 = 'If-Modified-Since'
        str_7 = 'If-None-Match'
        str_8 = 'HTTPie/0.13.0'
        str_9 = 'jsession=xxx; wcs_bt=s_xxx:xxx'
        str_10 = 'xxx'
        str_11 = {str_1: str_8, str_2: str_3, str_3: str_9, str_4: str_3, str_5: str_10, str_6: str_10, str_7: str_10}
        var_0 = session_0.update_headers(str_11)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '/non-existing-path'
        session_0 = module_2.Session(str_0)
        str_1 = 'Content-Type'
        str_2 = 'User-Agent'
        str_3 = 'If-Modified-Since'
        str_4 = 'Cookie'
        str_5 = 'Host'
        str_6 = 'application/json'
        str_7 = '0'
        str_8 = 'foo=bar; baz=qux'
        str_9 = 'localhost:5000'
        str_10 = {str_1: str_6, str_1: str_6, str_2: str_4, str_3: str_7, str_4: str_8, str_5: str_9}
        var_0 = session_0.update_headers(str_10)
    except BaseException:
        pass