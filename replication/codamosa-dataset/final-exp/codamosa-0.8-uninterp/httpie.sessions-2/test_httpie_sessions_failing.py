# Automatically generated by Pynguin.
import httpie.sessions as module_0
import pathlib as module_1
import httpie.cli.dicts as module_2
import requests.cookies as module_3

def test_case_0():
    try:
        path_0 = None
        str_0 = '%{fq?kwd\txupt'
        session_0 = module_0.get_httpie_session(path_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        iterable_0 = None
        path_0 = module_1.Path()
        str_0 = "\x0b8`/'y\npOW!wD7 "
        str_1 = 'gb0{72({;1r=,f7'
        str_2 = '8@=L'
        session_0 = module_0.get_httpie_session(path_0, str_0, str_1, str_2)
        var_0 = session_0.remove_cookies(iterable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'test'
        session_0 = module_0.Session(str_0)
        str_1 = 'ab'
        str_2 = [str_1, str_0]
        var_0 = session_0.remove_cookies(str_2)
        var_1 = session_0.cookies
        str_3 = 'M'
        dict_0 = {str_3: session_0}
        request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
        var_2 = session_0.update_headers(request_headers_dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        path_0 = module_1.Path()
        bytes_0 = b'd\x12\xfaYg\xef\x83\xa8n'
        var_0 = path_0.glob(bytes_0)
        var_1 = path_0.lstat()
        var_2 = path_0.exists()
        str_0 = 'u'
        str_1 = 'Output Processing'
        session_0 = module_0.get_httpie_session(path_0, str_0, str_0, str_1)
        bytes_1 = b''
        request_headers_dict_0 = module_2.RequestHeadersDict(bytes_1)
        str_2 = None
        str_3 = None
        session_1 = module_0.get_httpie_session(path_0, str_0, str_2, str_3)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '[\rV~=px:|`{@,'
        session_0 = module_0.Session(str_0)
        request_headers_dict_0 = module_2.RequestHeadersDict()
        var_0 = session_0.update_headers(request_headers_dict_0)
        path_0 = module_1.Path()
        str_1 = '=@A/x>R#&P&Zs,e+'
        session_1 = module_0.get_httpie_session(path_0, str_1, str_0, str_1)
        var_1 = session_0.update_headers(request_headers_dict_0)
        var_2 = session_0.update_headers(request_headers_dict_0)
        var_3 = session_0.update_headers(request_headers_dict_0)
        str_2 = ''
        str_3 = '02I|am!\x0bm~>cS.zy'
        session_2 = module_0.get_httpie_session(path_0, str_2, str_2, str_3)
        str_4 = 'kI'
        var_4 = session_0.remove_cookies(str_4)
        int_0 = 130
        var_5 = session_1.remove_cookies(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'test'
        session_0 = module_0.Session(str_0)
        var_0 = session_0.cookies
        var_1 = print(str_0)
        str_1 = 'abc'
        int_0 = 2
        var_2 = session_0.cookies
        requests_cookie_jar_0 = module_3.RequestsCookieJar()
        str_2 = '6AROS)vY_\x0c'
        list_0 = [str_1, int_0]
        str_3 = '1~wVG3rj0spgpa'
        str_4 = ''
        dict_0 = {str_0: var_1, str_2: list_0, str_3: list_0, str_4: str_3}
        request_headers_dict_0 = module_2.RequestHeadersDict(requests_cookie_jar_0, **dict_0)
        var_3 = session_0.update_headers(request_headers_dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = './test'
        session_0 = module_0.Session(str_0)
        str_1 = 'If-Modified-Since'
        str_2 = 'Accept-Language'
        str_3 = 'User-Agent'
        str_4 = 'Accept-Encoding'
        str_5 = 'Cookie'
        str_6 = 'Connection'
        str_7 = 'Host'
        str_8 = 'Sat, 29 Oct 1994 19:43:31 GMT'
        str_9 = 'pl-pl,pl;q=0.8,en;q=0.5,en-us;q=0.3'
        str_10 = 'HTTPie/0.9.3'
        str_11 = 'gzip, deflate'
        str_12 = 'some_cookie=some_value'
        str_13 = '*/*'
        str_14 = 'keep-alive'
        str_15 = '1'
        str_16 = 'httpie.org'
        str_17 = {str_1: str_8, str_2: str_9, str_3: str_10, str_4: str_11, str_5: str_12, str_11: str_13, str_6: str_14, str_6: str_15, str_7: str_16}
        var_0 = session_0.update_headers(str_17)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '~/.config/httpie/sessions/bbc.json'
        session_0 = module_0.Session(str_0)
        str_1 = 'HOST'
        str_2 = 'Cookie'
        str_3 = 'bbc.co.uk'
        str_4 = 'BBC-UID=1234567; expires=Fri'
        str_5 = {str_1: str_3, str_2: str_4}
        var_0 = session_0.update_headers(str_5)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = './test'
        session_0 = module_0.Session(str_0)
        str_1 = 'If-Modified-Since'
        str_2 = 'Accept-Language'
        str_3 = 'User-Agent'
        str_4 = 'Accept-Encoding'
        str_5 = 'Cookie'
        str_6 = 'AcaCpt'
        str_7 = 'Connection'
        str_8 = 'DNT'
        str_9 = 'Host'
        str_10 = 'Sat, 29 Oct 1994 19:43:31 GMT'
        str_11 = 'pl-pl,pl;q=0.8,en;q=0.5,en-us;q=0.3'
        str_12 = 'gzip, deflate'
        str_13 = 'some_cookie=some_value'
        str_14 = '*/*'
        str_15 = 'keep-alive'
        str_16 = '1O'
        str_17 = 'httpie.org'
        str_18 = {str_1: str_10, str_2: str_11, str_3: str_5, str_4: str_12, str_5: str_13, str_6: str_14, str_7: str_15, str_8: str_16, str_9: str_17}
        var_0 = session_0.update_headers(str_18)
    except BaseException:
        pass