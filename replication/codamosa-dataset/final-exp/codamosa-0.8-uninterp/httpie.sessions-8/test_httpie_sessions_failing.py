# Automatically generated by Pynguin.
import httpie.cli.dicts as module_0
import pathlib as module_1
import httpie.sessions as module_2

def test_case_0():
    try:
        dict_0 = {}
        request_headers_dict_0 = module_0.RequestHeadersDict(**dict_0)
        dict_1 = {}
        path_0 = module_1.Path(**dict_1)
        str_0 = ''
        session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_0)
        var_0 = session_0.update_headers(request_headers_dict_0)
        iterable_0 = None
        path_1 = module_1.Path()
        session_1 = module_2.Session(path_1)
        var_1 = session_1.remove_cookies(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        path_0 = module_1.Path()
        request_headers_dict_0 = module_0.RequestHeadersDict()
        str_0 = "$':hzJcm"
        session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_0)
        str_1 = '.8NDp\trilF\nn}kz'
        dict_0 = {str_0: str_0, str_0: request_headers_dict_0, str_1: session_0}
        request_headers_dict_1 = module_0.RequestHeadersDict(**dict_0)
        var_0 = session_0.update_headers(request_headers_dict_1)
    except BaseException:
        pass

def test_case_2():
    try:
        path_0 = module_1.Path()
        str_0 = 'P'
        session_0 = module_2.Session(str_0)
        request_headers_dict_0 = module_0.RequestHeadersDict()
        var_0 = session_0.remove_cookies(request_headers_dict_0)
        str_1 = '?IGgS>RSR'
        str_2 = '--continue only works with --download'
        dict_0 = {str_0: str_0, str_2: str_1, str_0: str_2, str_1: request_headers_dict_0, str_2: var_0}
        request_headers_dict_1 = module_0.RequestHeadersDict(**dict_0)
        session_1 = module_2.get_httpie_session(path_0, str_2, str_0, str_0)
        var_1 = session_1.update_headers(request_headers_dict_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = './test.json'
        session_0 = module_2.Session(str_0)
        str_1 = 'user-agent'
        str_2 = 'connect-type'
        str_3 = 'cookie'
        str_4 = 'test2'
        str_5 = 'test3'
        str_6 = {str_1: str_4, str_2: str_4, str_3: str_5}
        var_0 = session_0.update_headers(str_6)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Session1'
        session_0 = module_2.Session(str_0)
        str_1 = 'Accept-Encoding'
        str_2 = 'Cookie'
        str_3 = 'something=the-value'
        str_4 = {str_1: str_0, str_2: str_3}
        var_0 = session_0.update_headers(str_4)
    except BaseException:
        pass