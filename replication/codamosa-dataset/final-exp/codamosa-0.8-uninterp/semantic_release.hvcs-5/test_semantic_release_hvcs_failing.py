# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0
import urllib3.util.retry as module_1

def test_case_0():
    try:
        list_0 = []
        gitlab_0 = module_0.Gitlab(*list_0)
        optional_0 = gitlab_0.token()
        base_0 = module_0.Base()
        str_0 = base_0.domain()
    except BaseException:
        pass

def test_case_1():
    try:
        base_0 = module_0.Base()
        str_0 = base_0.api_url()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'b(3U_Q$v^UXg\r'
        str_1 = 'aSo!*u:p|#~*V'
        bool_0 = module_0.post_changelog(str_0, str_1, str_0, str_1)
        base_0 = module_0.Base()
        optional_0 = base_0.token()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 's+'
        base_0 = module_0.get_hvcs()
        bool_0 = True
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: bool_0}
        token_auth_0 = module_0.TokenAuth(dict_0)
        var_0 = token_auth_0.__eq__(base_0)
        str_1 = ')}rNGmGj@g~}kX|'
        base_1 = module_0.Base()
        bool_1 = base_1.check_build_status(str_0, str_1, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        github_0 = module_0.Github()
        optional_0 = github_0.auth()
        base_0 = module_0.get_hvcs()
        int_0 = 5498
        str_0 = '==`]w=p3GW-`s'
        retry_0 = module_1.Retry(base_0, int_0, github_0, str_0)
        token_auth_0 = module_0.TokenAuth(github_0)
        session_0 = github_0.session()
        var_0 = token_auth_0.__ne__(session_0)
        list_0 = [int_0, var_0, token_auth_0, github_0]
        var_1 = retry_0.is_retry(list_0, token_auth_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ';\r;Z:B5B2[`='
        str_1 = '$k7'
        bool_0 = module_0.post_changelog(str_0, str_0, str_1, str_0)
        base_0 = module_0.get_hvcs()
        dict_0 = None
        list_0 = None
        list_1 = [dict_0, list_0, list_0, str_1]
        bytes_0 = b';\\\r\xe6\x93\xafmh\x98j^\x8fq\x1b\x95Q\x91'
        tuple_0 = None
        retry_0 = module_1.Retry(dict_0, list_1, bytes_0, tuple_0)
        dict_1 = {}
        token_auth_0 = module_0.TokenAuth(dict_1)
        var_0 = token_auth_0.__call__(retry_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = "21Au<'"
        github_0 = module_0.Github()
        gitlab_0 = module_0.Gitlab()
        int_0 = 282
        session_0 = github_0.session(int_0)
        str_1 = None
        str_2 = '/releases/tags/'
        str_3 = '_|n@Qy_Iu?C1/t'
        token_auth_0 = module_0.TokenAuth(str_3)
        var_0 = token_auth_0.__eq__(str_2)
        str_4 = 'U#<g~\\ .g\x0cm\nuBK#N'
        str_5 = '))'
        str_6 = github_0.api_url()
        bool_0 = module_0.upload_to_release(str_1, str_4, str_0, str_5)
        bool_1 = gitlab_0.check_build_status(str_0, str_0, str_0)
    except BaseException:
        pass