# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2

def test_case_0():
    pass

def test_case_1():
    path_0 = module_0.Path()
    str_0 = 'MQoDV8WHI'
    session_0 = module_1.get_httpie_session(path_0, str_0, str_0, str_0)

def test_case_2():
    str_0 = '(,]t`'
    dict_0 = {str_0: str_0}
    request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
    str_1 = 'K:sq07CCM\x0b"W^leo\x0cI'
    str_2 = ':J~lN'
    dict_1 = {str_1: str_1, str_1: str_1, str_1: str_1, str_2: str_1}
    path_0 = module_0.Path(**dict_1)
    str_3 = '\n;/?'
    session_0 = module_1.get_httpie_session(path_0, str_3, str_0, str_1)
    var_0 = session_0.update_headers(request_headers_dict_0)
    session_1 = module_1.Session(str_1)

def test_case_3():
    str_0 = "An error indicating that the body is binary and won't be written,\n     e.g., for terminal output)."
    dict_0 = {str_0: str_0}
    session_0 = module_1.Session(str_0)
    request_headers_dict_0 = module_2.RequestHeadersDict(dict_0)
    path_0 = module_0.Path()
    str_1 = ''
    str_2 = 'j!15t\x0bhiW"(zX3\'7gEFt'
    session_1 = module_1.get_httpie_session(path_0, str_1, str_1, str_2)
    var_0 = session_1.update_headers(request_headers_dict_0)

def test_case_4():
    str_0 = 'OW)OEmeqSs4YGj[\x0b+'
    session_0 = module_1.Session(str_0)

def test_case_5():
    request_headers_dict_0 = module_2.RequestHeadersDict()
    list_0 = []
    path_0 = module_0.Path(*list_0)
    str_0 = '@U#GPJgO!f_]EX,><NHj'
    session_0 = module_1.get_httpie_session(path_0, str_0, str_0, str_0)
    var_0 = session_0.update_headers(request_headers_dict_0)

def test_case_6():
    str_0 = "An error indicating that the body is binary and won't be written,\n     e.g., for terminal output)."
    dict_0 = {str_0: str_0}
    session_0 = module_1.Session(str_0)
    request_headers_dict_0 = module_2.RequestHeadersDict(dict_0)
    path_0 = module_0.Path()
    var_0 = session_0.update_headers(request_headers_dict_0)

def test_case_7():
    str_0 = 'OW)OEmeqSs4YGj[\x0b+'
    set_0 = {str_0}
    session_0 = module_1.Session(str_0)
    var_0 = session_0.remove_cookies(set_0)

def test_case_8():
    str_0 = 'test_session'
    session_0 = module_1.Session(str_0)
    str_1 = 'Header1'
    str_2 = 'Header2'
    str_3 = 'Header3'
    str_4 = 'Header5'
    str_5 = 'value1'
    str_6 = 'value2'
    var_0 = None
    str_7 = 'value4'
    var_1 = {str_1: str_5, str_2: str_6, str_3: var_0, str_0: str_7, str_4: str_6}
    var_2 = session_0.update_headers(var_1)

def test_case_9():
    str_0 = 'Host'
    str_1 = 'Connection'
    str_2 = 'User-Agent'
    str_3 = 'Length'
    str_4 = 'Content-Type'
    str_5 = 'v@*`\\6'
    str_6 = 'keep-alive'
    str_7 = 'application/json'
    str_8 = '*/*'
    str_9 = {str_0: str_4, str_1: str_6, str_2: str_1, str_3: str_1, str_4: str_7, str_5: str_8}
    str_10 = './sessions/httpbin.org/httpbin.org.json'
    session_0 = module_1.Session(str_10)
    var_0 = session_0.update_headers(str_9)

def test_case_10():
    str_0 = 'Content-Type'
    str_1 = 'Cookie'
    str_2 = 'application/json'
    str_3 = 'username=admin;password=12345'
    str_4 = {str_0: str_2, str_1: str_3}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_4)
    str_5 = ''
    session_0 = module_1.Session(str_5)
    var_0 = session_0.update_headers(request_headers_dict_0)
    str_6 = 'username'
    var_1 = session_0.remove_cookies(request_headers_dict_0)
    str_7 = 'test'
    int_0 = None
    list_0 = [int_0, str_6, str_5]
    var_2 = session_0.remove_cookies(list_0)
    var_3 = request_headers_dict_0.get(str_7)

def test_case_11():
    str_0 = 'Host'
    str_1 = 'Connection'
    str_2 = 'User-Agent'
    str_3 = 'Length'
    str_4 = 'Content-Type'
    str_5 = 'Accept'
    str_6 = 'httpbin.org'
    str_7 = 'keep-alive'
    str_8 = 'HTTPie/0.9.9'
    str_9 = '135'
    str_10 = 'application/json'
    str_11 = '*/*'
    str_12 = {str_0: str_6, str_1: str_7, str_2: str_8, str_3: str_9, str_4: str_10, str_5: str_11}
    str_13 = './sessions/httpbin.org/httpbin.org.json'
    session_0 = module_1.Session(str_13)
    var_0 = session_0.update_headers(str_12)

def test_case_12():
    str_0 = './test-session'
    session_0 = module_1.Session(str_0)
    var_0 = session_0.cookies

def test_case_13():
    str_0 = './test-session'
    session_0 = module_1.Session(str_0)
    var_0 = session_0.auth