# Automatically generated by Pynguin.
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xe5\xd4\xda).M\x8aV\xc9\n\xb4 o\xe4M'
    var_0 = module_0.format_arg(bytes_0)

def test_case_2():
    bool_0 = True
    logged_function_0 = module_0.LoggedFunction(bool_0)
    str_0 = '\n    Returns the token for the current VCS\n\n    :return: The token in string form\n    '
    var_0 = module_0.format_arg(str_0)

def test_case_3():
    session_0 = module_0.build_requests_session()

def test_case_4():
    float_0 = -1247.0731
    str_0 = '_\ncw)5&?F?,a'
    logged_function_0 = module_0.LoggedFunction(float_0)
    dict_0 = {}
    retry_0 = module_1.Retry(dict_0)
    var_0 = logged_function_0.__call__(retry_0)
    int_0 = -24
    session_0 = module_0.build_requests_session(int_0)
    var_1 = logged_function_0.__call__(str_0)
    dict_1 = {float_0: session_0, str_0: session_0}
    var_2 = module_0.format_arg(dict_1)
    complex_0 = None
    logged_function_1 = module_0.LoggedFunction(session_0)
    tuple_0 = ()
    var_3 = logged_function_1.__call__(tuple_0)
    str_1 = 'TpF;%\\wgDD'
    int_1 = 230
    session_1 = module_0.build_requests_session(str_1, int_1)
    var_4 = logged_function_1.__call__(complex_0)

def test_case_5():
    int_0 = 3
    retry_0 = module_1.Retry(int_0)
    session_0 = module_0.build_requests_session(int_0, retry_0)

def test_case_6():
    float_0 = -916.8117
    logged_function_0 = module_0.LoggedFunction(float_0)

def test_case_7():
    tuple_0 = ()
    float_0 = -4984.2
    logged_function_0 = module_0.LoggedFunction(float_0)
    var_0 = logged_function_0.__call__(tuple_0)

def test_case_8():
    str_0 = None
    dict_0 = {str_0: str_0}
    str_1 = 'changelog_sections'
    var_0 = module_0.format_arg(str_1)
    var_1 = module_0.format_arg(dict_0)
    var_2 = module_0.format_arg(str_0)
    bytes_0 = b'\xc7\xbc'
    var_3 = module_0.format_arg(bytes_0)
    session_0 = module_0.build_requests_session()
    dict_1 = {var_3: bytes_0, var_3: var_0}
    var_4 = module_0.format_arg(dict_1)
    retry_0 = None
    session_1 = module_0.build_requests_session(retry_0, retry_0)

def test_case_9():
    bool_0 = False
    session_0 = module_0.build_requests_session(bool_0)