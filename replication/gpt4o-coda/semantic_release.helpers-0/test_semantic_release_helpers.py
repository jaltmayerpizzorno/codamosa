# Automatically generated by Pynguin.
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

def test_case_0():
    pass

def test_case_1():
    dict_0 = None
    var_0 = module_0.format_arg(dict_0)

def test_case_2():
    str_0 = '-Zc,.EU'
    var_0 = module_0.format_arg(str_0)

def test_case_3():
    session_0 = module_0.build_requests_session()

def test_case_4():
    int_0 = 1404
    bytes_0 = None
    logged_function_0 = module_0.LoggedFunction(bytes_0)
    bool_0 = True
    session_0 = module_0.build_requests_session(int_0, int_0)
    var_0 = module_0.format_arg(session_0)
    session_1 = module_0.build_requests_session(bool_0)
    float_0 = 149.0
    logged_function_1 = module_0.LoggedFunction(float_0)

def test_case_5():
    retry_0 = module_1.Retry()
    session_0 = module_0.build_requests_session(retry_0, retry_0)

def test_case_6():
    bool_0 = True
    logged_function_0 = module_0.LoggedFunction(bool_0)

def test_case_7():
    bool_0 = True
    float_0 = -5715.0
    logged_function_0 = module_0.LoggedFunction(float_0)
    var_0 = logged_function_0.__call__(bool_0)

def test_case_8():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    session_0 = module_0.build_requests_session(list_0, bool_0)
    complex_0 = None
    logged_function_0 = module_0.LoggedFunction(complex_0)
    bytes_0 = b'U\xaf\x1c\x93\xa0\xfd\x80cz\xc7q\xfcX'
    var_0 = module_0.format_arg(bytes_0)
    str_0 = 'y\tA"aC'
    dict_0 = None
    logged_function_1 = module_0.LoggedFunction(dict_0)
    float_0 = -1275.6795
    list_1 = [complex_0]
    tuple_0 = (float_0, list_1)
    var_1 = logged_function_0.__call__(tuple_0)
    str_1 = 'response'
    bytes_1 = b'\xcc'
    session_1 = module_0.build_requests_session(bytes_1)
    dict_1 = {str_0: str_0, str_1: str_0}
    session_2 = module_0.build_requests_session()
    logged_function_2 = module_0.LoggedFunction(dict_0)
    var_2 = module_0.format_arg(session_2)
    session_3 = module_0.build_requests_session(dict_1)
    var_3 = module_0.format_arg(logged_function_1)

def test_case_9():
    str_0 = ''
    bytes_0 = b'l'
    bool_0 = True
    retry_0 = module_1.Retry(bool_0, bytes_0, bytes_0, bool_0, str_0)
    session_0 = module_0.build_requests_session(str_0, retry_0)