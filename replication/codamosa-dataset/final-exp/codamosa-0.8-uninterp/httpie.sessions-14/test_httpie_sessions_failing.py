# Automatically generated by Pynguin.
import httpie.sessions as module_0
import httpie.cli.dicts as module_1
import pathlib as module_2

def test_case_0():
    try:
        iterable_0 = None
        str_0 = "xMKc,;.'6V\\$&d|t"
        session_0 = module_0.Session(str_0)
        request_headers_dict_0 = module_1.RequestHeadersDict()
        var_0 = session_0.update_headers(request_headers_dict_0)
        var_1 = session_0.remove_cookies(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        path_0 = module_2.Path()
        str_0 = ''
        str_1 = 'v'
        dict_0 = {str_0: str_0, str_1: path_0}
        request_headers_dict_0 = module_1.RequestHeadersDict(**dict_0)
        session_0 = module_0.Session(path_0)
        var_0 = session_0.update_headers(request_headers_dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        iterable_0 = None
        str_0 = ':\t9EeU;'
        str_1 = 'data'
        str_2 = 'o=%/j(!5'
        dict_0 = {str_0: iterable_0, str_1: iterable_0, str_2: str_0, str_2: iterable_0}
        request_headers_dict_0 = module_1.RequestHeadersDict(**dict_0)
        str_3 = '+aC>\\Fino,-|o\x0c]o'
        session_0 = module_0.Session(str_3)
        var_0 = session_0.update_headers(request_headers_dict_0)
        str_4 = "uR_WHcIzm2~'uf"
        str_5 = 'y]8c\r:<MboGD\x0cv6e'
        dict_1 = {str_4: str_4, str_5: str_4, str_5: str_4, str_5: str_5}
        path_0 = module_2.Path(**dict_1)
        str_6 = '\nD0Un6`E*w$Lj'
        str_7 = 'p1?'
        session_1 = module_0.get_httpie_session(path_0, str_6, str_6, str_7)
        var_1 = session_1.remove_cookies(iterable_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'X-test'
        str_1 = 'Cookie'
        str_2 = 'old'
        str_3 = 'Cookies'
        str_4 = 'new'
        str_5 = 'foo=bar'
        str_6 = {str_0: str_4, str_3: str_2, str_1: str_5}
        session_0 = module_0.Session(str_2)
        var_0 = session_0.update_headers(str_6)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '/test'
        session_0 = module_0.Session(str_0)
        str_1 = 'test1'
        str_2 = 'test2'
        str_3 = [str_1, str_2]
        var_0 = session_0.remove_cookies(str_3)
        var_1 = session_0.cookies
        var_2 = len(var_1)
        int_0 = 0
        var_3 = session_0.cookies
        var_4 = list(var_3)[int_0]
    except BaseException:
        pass