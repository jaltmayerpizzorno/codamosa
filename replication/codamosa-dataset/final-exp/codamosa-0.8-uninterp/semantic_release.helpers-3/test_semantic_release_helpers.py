# Automatically generated by Pynguin.
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = 815
    var_0 = module_0.format_arg(int_0)

def test_case_2():
    str_0 = '"AO]9e.\tkPk.9\\aLq[8e'
    str_1 = '\n/V2'
    int_0 = 1
    logged_function_0 = module_0.LoggedFunction(int_0)
    set_0 = {str_1, str_1, str_1, int_0}
    list_0 = []
    logged_function_1 = module_0.LoggedFunction(list_0)
    float_0 = -1109.0
    dict_0 = {float_0: str_1, str_1: str_0, float_0: logged_function_0, str_0: int_0}
    var_0 = logged_function_0.__call__(dict_0)
    logged_function_2 = module_0.LoggedFunction(set_0)
    var_1 = logged_function_0.__call__(str_1)
    var_2 = module_0.format_arg(str_0)
    float_1 = -3851.0
    var_3 = module_0.format_arg(float_1)
    str_2 = '|z9\x0cRFP'
    logged_function_3 = module_0.LoggedFunction(str_2)
    int_1 = -639
    session_0 = module_0.build_requests_session(int_1)
    session_1 = module_0.build_requests_session(int_1)

def test_case_3():
    session_0 = module_0.build_requests_session()

def test_case_4():
    int_0 = 1
    bytes_0 = b'\xd20\xfe6\xc8u\xc1\x90\xfd\xe46\x00\x8es"\x129'
    session_0 = module_0.build_requests_session(bytes_0, int_0)

def test_case_5():
    str_0 = 'response'
    float_0 = 1804.6
    dict_0 = {str_0: str_0, str_0: float_0}
    logged_function_0 = module_0.LoggedFunction(dict_0)

def test_case_6():
    tuple_0 = None
    logged_function_0 = module_0.LoggedFunction(tuple_0)
    bytes_0 = b'D\x9d<\xf4'
    session_0 = module_0.build_requests_session(bytes_0)
    logged_function_1 = module_0.LoggedFunction(session_0)
    var_0 = logged_function_1.__call__(logged_function_0)

def test_case_7():
    str_0 = 'http://google.com'
    str_1 = 'key'
    str_2 = 'value'
    str_3 = {str_1: str_2}
    bool_0 = True
    session_0 = module_0.build_requests_session(bool_0)
    var_0 = session_0.get(str_0)
    bool_1 = False
    bool_2 = True
    session_1 = module_0.build_requests_session(bool_1, bool_2)
    session_2 = module_0.build_requests_session(bool_1, bool_1)

def test_case_8():
    bytes_0 = b'\x18\xe4\xe6\x03\xae'
    logged_function_0 = module_0.LoggedFunction(bytes_0)
    float_0 = 1144.0
    set_0 = set()
    retry_0 = module_1.Retry(bytes_0, logged_function_0, logged_function_0, float_0)
    session_0 = module_0.build_requests_session(set_0, retry_0)
    var_0 = logged_function_0.__call__(bytes_0)