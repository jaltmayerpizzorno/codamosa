# Automatically generated by Pynguin.
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'k\\)X\tPtxU7Ab_SXsqx'
    str_1 = 'O<ujWC#KH&'
    dict_0 = {str_0: str_0, str_1: str_1}
    var_0 = module_0.format_arg(dict_0)

def test_case_2():
    str_0 = 'bia5x`dG\x0c\tG=&1Hy_"'
    str_1 = ':r/BYc|'
    str_2 = "\ni'KKCY\x0boEtHZ\rng(2<G"
    str_3 = '~\x0cl+MCn.'
    dict_0 = {str_0: str_1, str_2: str_1, str_3: str_0, str_3: str_2}
    var_0 = module_0.format_arg(dict_0)
    list_0 = None
    session_0 = module_0.build_requests_session()
    session_1 = module_0.build_requests_session()
    str_4 = "]/.F bbp'P"
    var_1 = module_0.format_arg(str_4)
    list_1 = [list_0]
    var_2 = module_0.format_arg(list_1)

def test_case_3():
    session_0 = module_0.build_requests_session()

def test_case_4():
    retry_0 = module_1.Retry()
    session_0 = module_0.build_requests_session()
    session_1 = module_0.build_requests_session(session_0, retry_0)

def test_case_5():
    int_0 = 456
    logged_function_0 = module_0.LoggedFunction(int_0)

def test_case_6():
    int_0 = -183
    session_0 = module_0.build_requests_session()
    logged_function_0 = module_0.LoggedFunction(session_0)
    var_0 = logged_function_0.__call__(int_0)

def test_case_7():
    dict_0 = {}
    str_0 = ''
    retry_0 = module_1.Retry(dict_0, dict_0, str_0, str_0)
    session_0 = module_0.build_requests_session(str_0, retry_0)