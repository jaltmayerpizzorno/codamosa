# Automatically generated by Pynguin.
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    var_0 = module_0.format_arg(bool_0)

def test_case_2():
    session_0 = module_0.build_requests_session()
    str_0 = "P=7Oc8aw'gZW2AMalL"
    var_0 = module_0.format_arg(str_0)
    str_1 = 'D^h}@)`\x0c=aWLay!'
    list_0 = [session_0, str_1]
    dict_0 = {}
    bytes_0 = b'.\x911\xe7\xdbX=\xc8${\\>x9z'
    bytes_1 = b'\x82\xee\x9e\xb3\x8e\xf2\xc7'
    bool_0 = None
    retry_0 = module_1.Retry(dict_0, str_1, bytes_0, bytes_1, dict_0, bool_0)
    session_1 = module_0.build_requests_session(list_0, retry_0)
    set_0 = {str_1, session_0}
    session_2 = module_0.build_requests_session()
    int_0 = -1229
    session_3 = module_0.build_requests_session(set_0, int_0)
    str_2 = ' to '
    dict_1 = {str_1: session_0, str_1: session_0, str_1: session_0, str_2: str_1}
    var_1 = module_0.format_arg(dict_1)

def test_case_3():
    session_0 = module_0.build_requests_session()

def test_case_4():
    int_0 = -401
    str_0 = 'sIU<Y72`'
    bool_0 = False
    logged_function_0 = module_0.LoggedFunction(bool_0)
    var_0 = logged_function_0.__call__(str_0)
    session_0 = module_0.build_requests_session()
    tuple_0 = None
    bool_1 = True
    tuple_1 = (session_0, tuple_0, bool_1)
    session_1 = module_0.build_requests_session(tuple_1, int_0)
    session_2 = module_0.build_requests_session(int_0)
    str_1 = '\x0c\x0bFn~adjZ~w,\x0b'
    str_2 = None
    dict_0 = {str_1: tuple_1, str_2: logged_function_0}
    var_1 = logged_function_0.__call__(dict_0)
    session_3 = module_0.build_requests_session()
    bool_2 = True
    session_4 = module_0.build_requests_session(bool_2)

def test_case_5():
    retry_0 = module_1.Retry()
    session_0 = module_0.build_requests_session(retry_0, retry_0)

def test_case_6():
    bytes_0 = b'\xfeg`<nU#\xe7t\xac?\xa8'
    int_0 = 404
    logged_function_0 = module_0.LoggedFunction(int_0)
    var_0 = logged_function_0.__call__(bytes_0)

def test_case_7():
    bool_0 = False
    session_0 = module_0.build_requests_session(bool_0, bool_0)
    retry_0 = module_1.Retry()
    session_1 = module_0.build_requests_session(bool_0, retry_0)

def test_case_8():
    bool_0 = False
    retry_0 = module_1.Retry()
    session_0 = module_0.build_requests_session(bool_0, retry_0)