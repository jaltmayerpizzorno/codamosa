# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2
import builtins as module_3

def test_case_0():
    pass

def test_case_1():
    str_0 = 'i4/5)`\x0bwW9$a]+'
    list_0 = []
    path_0 = module_0.Path(*list_0)
    str_1 = 'zQN:c|ZT\\]\\x%'
    session_0 = module_1.get_httpie_session(path_0, str_1, str_1, str_1)
    var_0 = session_0.remove_cookies(str_0)

def test_case_2():
    str_0 = '/tmp/foo.txt'
    session_0 = module_1.Session(str_0)
    str_1 = 'e o'
    path_0 = module_0.Path()
    str_2 = ';|"lt$v2:y*'
    session_1 = module_1.get_httpie_session(path_0, str_0, str_0, str_2)
    str_3 = 'bar'
    var_0 = session_0.remove_cookies(str_3)
    var_1 = len(str_1)
    var_2 = session_0.remove_cookies(str_1)
    var_3 = session_0.cookies
    var_4 = len(var_3)

def test_case_3():
    str_0 = "RM\no~VR{%6'6[I5{"
    session_0 = module_1.Session(str_0)

def test_case_4():
    str_0 = '/tmp/foo.txt'
    session_0 = module_1.Session(str_0)
    var_0 = session_0.remove_cookies(str_0)
    var_1 = session_0.cookies
    var_2 = session_0.remove_cookies(str_0)
    var_3 = session_0.cookies
    request_headers_dict_0 = None
    request_headers_dict_1 = module_2.RequestHeadersDict(request_headers_dict_0)
    var_4 = session_0.update_headers(request_headers_dict_1)
    var_5 = len(var_3)

def test_case_5():
    str_0 = '/tmp_fGo.tKV'
    session_0 = module_1.Session(str_0)
    var_0 = session_0.remove_cookies(str_0)

def test_case_6():
    str_0 = '\t8a.~?@mg[2]0f>jH(c\x0b'
    bytes_0 = b'J*\xbe\'\xeb"a\xea'
    session_0 = module_1.Session(str_0)
    str_1 = 'https://httpie.org/doc#sessions'
    dict_0 = {str_0: str_0, str_0: bytes_0, str_1: str_1}
    request_headers_dict_0 = module_2.RequestHeadersDict()
    var_0 = session_0.update_headers(request_headers_dict_0)
    var_1 = session_0.update_headers(request_headers_dict_0)
    path_0 = module_0.Path(**dict_0)
    session_1 = module_1.get_httpie_session(path_0, str_0, str_1, str_0)
    str_2 = 'tH\\-9'
    session_2 = module_1.get_httpie_session(path_0, str_0, str_0, str_2)
    dict_1 = {str_2: str_2}
    path_1 = module_0.Path(**dict_1)
    str_3 = '4'
    session_3 = module_1.get_httpie_session(path_1, str_3, str_2, str_2)
    request_headers_dict_1 = module_2.RequestHeadersDict(**dict_1)
    path_2 = module_0.Path()
    str_4 = '&LMLTMg!@4%%\n3\tVbd'
    str_5 = '0,~oV'
    session_4 = module_1.get_httpie_session(path_2, str_5, str_4, str_2)
    none_type_0 = None
    str_6 = 's4T[1i+b'
    session_5 = module_1.get_httpie_session(path_2, str_5, none_type_0, str_6)
    list_0 = module_3.list()
    path_3 = module_0.Path(*list_0)
    session_6 = module_1.Session(path_0)
    var_2 = session_1.update_headers(request_headers_dict_1)
    session_7 = module_1.Session(str_2)
    session_8 = module_1.Session(str_0)
    var_3 = session_3.update_headers(request_headers_dict_1)

def test_case_7():
    str_0 = 't4Pv4Ir'
    session_0 = module_1.Session(str_0)
    str_1 = 'H\n'
    str_2 = 'Content-Type'
    str_3 = 'If-Modified-Since'
    str_4 = '123'
    var_0 = None
    str_5 = '1234'
    var_1 = {str_1: str_4, str_2: var_0, str_3: str_5}
    var_2 = session_0.update_headers(var_1)
    var_3 = session_0.headers
    var_4 = print(var_3)

def test_case_8():
    str_0 = '/tmp/foo.txt'
    session_0 = module_1.Session(str_0)
    var_0 = session_0.cookies