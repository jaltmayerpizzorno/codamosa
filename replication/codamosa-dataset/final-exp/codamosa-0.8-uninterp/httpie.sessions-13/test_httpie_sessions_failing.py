# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.cli.dicts as module_1
import httpie.sessions as module_2

def test_case_0():
    try:
        path_0 = module_0.Path()
        int_0 = -2708
        request_headers_dict_0 = module_1.RequestHeadersDict()
        str_0 = "yZo^3ui'=ZC;I6Nc#HGu"
        session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_0)
        path_1 = module_0.Path()
        str_1 = '=BhWV(@96*g8z u'
        str_2 = ':]+'
        session_1 = module_2.get_httpie_session(path_1, str_1, str_1, str_2)
        var_0 = session_1.update_headers(request_headers_dict_0)
        var_1 = session_1.update_headers(request_headers_dict_0)
        var_2 = path_0.rglob(int_0)
        session_2 = module_2.Session(path_0)
        str_3 = None
        str_4 = '{N-<'
        session_3 = module_2.get_httpie_session(path_1, str_4, str_3, str_2)
        session_4 = module_2.Session(str_3)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'v5u ?F <_(BH'
        list_0 = [str_0]
        dict_0 = {str_0: list_0}
        request_headers_dict_0 = module_1.RequestHeadersDict(**dict_0)
        str_1 = 'Hp.y<:$aLq'
        dict_1 = {str_1: list_0, str_1: str_1, str_0: str_1}
        path_0 = module_0.Path(**dict_1)
        str_2 = '-x'
        str_3 = 'user-agent'
        session_0 = module_2.get_httpie_session(path_0, str_2, str_3, str_2)
        var_0 = session_0.update_headers(request_headers_dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'a/b'
        session_0 = module_2.Session(str_0)
        str_1 = 'User-Agent'
        str_2 = 'Cookie'
        str_3 = 'Content-Type'
        str_4 = 'HTTPie/0.9.9'
        str_5 = 'foo1=bar1; foo2=bar2'
        str_6 = 'application/json'
        str_7 = {str_1: str_4, str_2: str_5, str_3: str_6}
        var_0 = session_0.update_headers(str_7)
    except BaseException:
        pass