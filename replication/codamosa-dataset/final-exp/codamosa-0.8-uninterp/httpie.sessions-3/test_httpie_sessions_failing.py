# Automatically generated by Pynguin.
import httpie.sessions as module_0
import httpie.cli.dicts as module_1

def test_case_0():
    try:
        str_0 = "$NdHu0w\r'2#$"
        str_1 = '8'
        list_0 = [str_0, str_0, str_1, str_1]
        session_0 = module_0.Session(str_0)
        var_0 = session_0.remove_cookies(list_0)
        session_1 = module_0.Session(str_0)
        dict_0 = {str_0: session_1}
        request_headers_dict_0 = module_1.RequestHeadersDict(**dict_0)
        var_1 = session_1.update_headers(request_headers_dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '__cfduid=d8f6e5cd638fd9df85c4d7f8c25aa80e71568485094'
        str_1 = 'Content-Type'
        str_2 = 'Cookie'
        str_3 = 'application/json; charset=utf-8'
        str_4 = {str_1: str_3, str_2: str_0}
        str_5 = 'sessions/session1.json'
        session_0 = module_0.Session(str_5)
        var_0 = session_0.update_headers(str_4)
    except BaseException:
        pass