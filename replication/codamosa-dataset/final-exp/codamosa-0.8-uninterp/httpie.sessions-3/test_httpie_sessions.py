# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2

def test_case_0():
    pass

def test_case_1():
    path_0 = module_0.Path()
    str_0 = 'tCp{[#"m\'+zMq8"'
    str_1 = 'Invalid item "%s" (to specify an empty header use `Header;`)'
    session_0 = module_1.get_httpie_session(path_0, str_0, str_1, str_1)
    session_1 = module_1.get_httpie_session(path_0, str_0, str_0, str_0)

def test_case_2():
    str_0 = 'aJ8HP'
    dict_0 = {str_0: str_0}
    request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
    path_0 = module_0.Path()
    session_0 = module_1.Session(str_0)
    var_0 = session_0.update_headers(request_headers_dict_0)
    str_1 = '1)!+`n/0\\'
    session_1 = module_1.get_httpie_session(path_0, str_1, str_0, str_0)
    session_2 = module_1.get_httpie_session(path_0, str_1, str_0, str_0)

def test_case_3():
    request_headers_dict_0 = module_2.RequestHeadersDict()
    path_0 = module_0.Path()
    var_0 = path_0.is_fifo()
    str_0 = 'Y(.f{H{?+\x0bl*vo'
    str_1 = ''
    str_2 = 'E3?M)W'
    session_0 = module_1.get_httpie_session(path_0, str_1, str_1, str_2)
    var_1 = session_0.update_headers(request_headers_dict_0)
    session_1 = module_1.get_httpie_session(path_0, str_0, str_0, str_0)
    var_2 = session_1.update_headers(request_headers_dict_0)

def test_case_4():
    str_0 = 'Xv'
    session_0 = module_1.Session(str_0)

def test_case_5():
    str_0 = './default.json'
    session_0 = module_1.Session(str_0)
    str_1 = 'User-Agent'
    str_2 = {str_0: str_0, str_1: str_0, str_0: str_0, str_0: str_1}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_2)
    var_0 = session_0.update_headers(request_headers_dict_0)

def test_case_6():
    str_0 = 'dH3>Vx!;x3:5Q@FWsD'
    session_0 = module_1.Session(str_0)
    var_0 = session_0.remove_cookies(str_0)

def test_case_7():
    str_0 = './default.json'
    session_0 = module_1.Session(str_0)
    str_1 = 'User-Agent'
    str_2 = 'Cookie'
    str_3 = {str_0: str_0, str_1: str_2, str_0: str_0, str_2: str_1}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_3)
    var_0 = session_0.update_headers(request_headers_dict_0)

def test_case_8():
    str_0 = 'temp.json'
    session_0 = module_1.Session(str_0)
    str_1 = 'key'
    str_2 = 'value'
    str_3 = {str_1: str_2}
    var_0 = session_0.update_headers(str_3)
    str_4 = 'value2'
    str_5 = {str_1: str_4}
    var_1 = session_0.update_headers(str_5)
    var_2 = None
    var_3 = {str_1: var_2}
    var_4 = session_0.update_headers(var_3)
    str_6 = {str_1: str_2}
    var_5 = session_0.update_headers(str_6)
    str_7 = {str_1: str_2}
    var_6 = session_0.update_headers(str_7)
    str_8 = {str_1: str_2}
    var_7 = session_0.update_headers(str_8)
    str_9 = {str_1: str_4}
    var_8 = session_0.update_headers(str_9)

def test_case_9():
    str_0 = './default.json'
    session_0 = module_1.Session(str_0)
    str_1 = '\noOt'
    str_2 = 'User-Agent'
    str_3 = 'Cookie'
    str_4 = '*/*'
    str_5 = {str_1: str_1, str_2: str_3, str_1: str_4, str_3: str_0}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_5)
    var_0 = session_0.update_headers(request_headers_dict_0)
    var_1 = session_0.cookies
    var_2 = print(var_1)

def test_case_10():
    str_0 = './default.json'
    session_0 = module_1.Session(str_0)
    str_1 = 'Host'
    str_2 = 'User-Agent'
    str_3 = 'Cookie'
    str_4 = '*/*'
    str_5 = 'PHPSESSID=ajkv124k5jnr0e67pb44ktbe50'
    str_6 = {str_1: str_1, str_2: str_3, str_1: str_4, str_3: str_5}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_6)
    var_0 = session_0.update_headers(request_headers_dict_0)
    var_1 = session_0.cookies
    var_2 = print(var_1)