# Automatically generated by Pynguin.
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

def test_case_0():
    pass

def test_case_1():
    list_0 = None
    float_0 = 649.7679
    var_0 = module_0.format_arg(float_0)
    bytes_0 = b'p\xcd\xb58\x95\x1fl#&\xf7\x9e\x18\x86'
    logged_function_0 = module_0.LoggedFunction(bytes_0)
    var_1 = logged_function_0.__call__(list_0)
    dict_0 = {}
    var_2 = logged_function_0.__call__(dict_0)

def test_case_2():
    bytes_0 = b'\x01\xb4\xcb\xf3'
    str_0 = 'Attempting to create release for '
    var_0 = module_0.format_arg(str_0)
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_1 = module_0.format_arg(list_0)
    dict_0 = None
    logged_function_0 = module_0.LoggedFunction(dict_0)
    session_0 = module_0.build_requests_session()
    logged_function_1 = module_0.LoggedFunction(bytes_0)
    logged_function_2 = module_0.LoggedFunction(dict_0)
    list_1 = [logged_function_1, bytes_0, bytes_0, bytes_0]
    var_2 = logged_function_1.__call__(list_1)

def test_case_3():
    session_0 = module_0.build_requests_session()

def test_case_4():
    str_0 = 'B,;p\n3:68=L667N&>d\t'
    str_1 = 'YxGJ|\r+cp9'
    dict_0 = {str_0: str_0, str_1: str_0}
    int_0 = 1611
    session_0 = module_0.build_requests_session(dict_0, int_0)
    set_0 = {session_0, int_0}
    str_2 = 'C^^,$ZHq$WJ"{'
    dict_1 = {str_2: str_2}
    logged_function_0 = module_0.LoggedFunction(dict_1)
    var_0 = logged_function_0.__call__(set_0)

def test_case_5():
    bool_0 = True
    retry_0 = module_1.Retry()
    session_0 = module_0.build_requests_session(bool_0, retry_0)

def test_case_6():
    complex_0 = None
    logged_function_0 = module_0.LoggedFunction(complex_0)

def test_case_7():
    str_0 = 'n?'
    bytes_0 = b'\x8aJ\xb4J'
    logged_function_0 = module_0.LoggedFunction(bytes_0)
    var_0 = logged_function_0.__call__(str_0)

def test_case_8():
    bool_0 = False
    session_0 = module_0.build_requests_session(bool_0, bool_0)
    retry_0 = module_1.Retry()
    session_1 = module_0.build_requests_session(bool_0, retry_0)

def test_case_9():
    bool_0 = False
    retry_0 = module_1.Retry()
    session_0 = module_0.build_requests_session(bool_0, retry_0)