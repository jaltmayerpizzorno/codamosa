# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2

def test_case_0():
    pass

def test_case_1():
    path_0 = module_0.Path()
    str_0 = '--verbose'
    session_0 = module_1.get_httpie_session(path_0, str_0, str_0, str_0)
    var_0 = session_0.remove_cookies(str_0)

def test_case_2():
    path_0 = module_0.Path()
    str_0 = "Return processed `content`.\n\n        :param mime: E.g., 'application/atom+xml'.\n        :param content: The body cotent as text\n\n        "
    session_0 = module_1.get_httpie_session(path_0, str_0, str_0, str_0)
    str_1 = '.8DprilF\nn}kz'
    dict_0 = {str_1: path_0, str_1: str_0}
    request_headers_dict_0 = module_2.RequestHeadersDict(**dict_0)
    var_0 = session_0.update_headers(request_headers_dict_0)

def test_case_3():
    str_0 = 'output_file'
    session_0 = module_1.Session(str_0)

def test_case_4():
    str_0 = './test.json'
    session_0 = module_1.Session(str_0)
    str_1 = 'user-agent'
    str_2 = {str_1: str_0, str_0: str_0, str_0: str_0}
    var_0 = session_0.update_headers(str_2)

def test_case_5():
    str_0 = 'http://httpbin.org/put'
    session_0 = module_1.Session(str_0)
    str_1 = 'Content-Type'
    str_2 = 'application/json'
    str_3 = {str_1: str_2}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_3)
    var_0 = session_0.update_headers(request_headers_dict_0)