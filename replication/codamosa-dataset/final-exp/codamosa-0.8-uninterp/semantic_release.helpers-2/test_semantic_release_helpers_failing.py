# Automatically generated by Pynguin.
import semantic_release.helpers as module_0

def test_case_0():
    try:
        int_0 = 2593
        logged_function_0 = module_0.LoggedFunction(int_0)
        bytes_0 = b'Df\xa0\xc8:\xfc\xe0^\r\xe1\xff<\xb8\x84\x9c\xe5\x0f\xb97)'
        list_0 = []
        logged_function_1 = module_0.LoggedFunction(list_0)
        session_0 = module_0.build_requests_session(logged_function_1)
        int_1 = 2544
        dict_0 = {}
        logged_function_2 = module_0.LoggedFunction(dict_0)
        session_1 = module_0.build_requests_session(bytes_0, int_1)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        str_0 = 'bNM!:WafI,7p*79g7'
        list_1 = [str_0, str_0]
        logged_function_0 = module_0.LoggedFunction(list_1)
        var_0 = logged_function_0.__call__(list_0)
        str_1 = 'Not in a valid git repository'
        bytes_0 = b'\xd4N8T\xc0r\xa7'
        var_1 = module_0.format_arg(bytes_0)
        bool_0 = False
        session_0 = module_0.build_requests_session(str_1, bool_0)
        session_1 = module_0.build_requests_session()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        session_0 = module_0.build_requests_session(bool_0, bool_0)
        str_0 = 'https://httpbin.org/anything?q=abc'
        var_0 = session_0.get(str_0)
        str_1 = 'q'
        str_2 = 'args'
        var_1 = resp.json()[str_2][str_1]
    except BaseException:
        pass