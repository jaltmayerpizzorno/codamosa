# Automatically generated by Pynguin.
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

def test_case_0():
    try:
        set_0 = set()
        logged_function_0 = module_0.LoggedFunction(set_0)
        list_0 = [logged_function_0]
        list_1 = [set_0, list_0, list_0]
        var_0 = logged_function_0.__call__(list_1)
        int_0 = 1586
        logged_function_1 = module_0.LoggedFunction(int_0)
        str_0 = "RRGu)7,D9'T@tv"
        float_0 = -1421.56
        var_1 = logged_function_0.__call__(float_0)
        logged_function_2 = module_0.LoggedFunction(str_0)
        float_1 = 2030.8
        var_2 = module_0.format_arg(float_1)
        bool_0 = None
        session_0 = module_0.build_requests_session(bool_0, bool_0)
        var_3 = logged_function_2.__call__(logged_function_0)
    except BaseException:
        pass

def test_case_1():
    try:
        session_0 = module_0.build_requests_session()
        str_0 = 'https://httpbin.org/get'
        var_0 = session_0.get(str_0)
        bool_0 = False
        session_1 = module_0.build_requests_session(bool_0)
        var_1 = session_1.get(str_0)
        int_0 = 1
        retry_0 = module_1.Retry(int_0)
        session_2 = module_0.build_requests_session(retry_0)
        str_1 = 'https://httpbin.org/status/503'
        var_2 = session_2.get(str_1)
    except BaseException:
        pass