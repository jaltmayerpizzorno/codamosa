# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    try:
        github_0 = module_0.Github()
        base_0 = module_0.get_hvcs()
        optional_0 = module_0.get_domain()
        str_0 = base_0.api_url()
        session_0 = github_0.session()
        str_1 = base_0.domain()
        github_1 = module_0.Github()
        optional_1 = module_0.get_domain()
        str_2 = None
        bool_0 = module_0.check_build_status(str_2, str_2, str_2)
        base_1 = module_0.Base()
        dict_0 = {}
        base_2 = module_0.Base(**dict_0)
        optional_2 = module_0.get_token()
        optional_3 = github_1.auth()
        str_3 = base_1.domain()
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
        base_0 = module_0.Base()
        optional_0 = base_0.token()
    except BaseException:
        pass

def test_case_3():
    try:
        gitlab_0 = module_0.Gitlab()
        github_0 = module_0.Github()
        str_0 = '* '
        str_1 = '`KW'
        bool_0 = module_0.post_changelog(str_0, str_1, str_1, str_1)
        bool_1 = github_0.check_build_status(str_1, str_0, str_0)
        session_0 = github_0.session()
        optional_0 = gitlab_0.token()
        optional_1 = gitlab_0.token()
        optional_2 = gitlab_0.token()
        str_2 = '\niKf^dbA~Vktv#"O]GO.'
        str_3 = '[G2`sX|`x`'
        str_4 = 'l_^j~MI~XCZ}vhab>u'
        base_0 = module_0.Base()
        bool_2 = base_0.check_build_status(str_2, str_3, str_4)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        str_1 = None
        str_2 = ' '
        bool_0 = module_0.upload_to_release(str_0, str_1, str_1, str_2)
        list_0 = []
        token_auth_0 = module_0.TokenAuth(str_1)
        token_auth_1 = module_0.TokenAuth(token_auth_0)
        var_0 = token_auth_1.__call__(list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'M1 FXg:\x0cywTTzxu'
        gitlab_0 = module_0.Gitlab()
        bool_0 = gitlab_0.check_build_status(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        optional_0 = module_0.get_token()
        list_0 = [optional_0, optional_0]
        str_0 = 'Checking build status...'
        str_1 = 'print-'
        str_2 = '0S|IzYoGXAB'
        int_0 = -3066
        dict_0 = {str_0: list_0, str_1: list_0, str_2: int_0, str_1: str_0}
        github_0 = module_0.Github(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        base_0 = module_0.get_hvcs()
        tuple_0 = ()
        token_auth_0 = module_0.TokenAuth(tuple_0)
        var_0 = token_auth_0.__ne__(base_0)
        base_1 = module_0.get_hvcs()
        base_2 = module_0.Base()
        str_0 = 'I>\nvc{U;y8tU\r3F6\x0cq'
        str_1 = 'RZIfc7\\:%xqI\\OviTz&B'
        bool_0 = base_1.check_build_status(str_0, str_1, str_1)
        str_2 = base_1.api_url()
        dict_0 = {}
        optional_0 = base_0.token()
        list_0 = [str_2, var_0]
        github_0 = module_0.Github()
        session_0 = github_0.session()
        var_1 = token_auth_0.__call__(session_0)
        var_2 = token_auth_0.__ne__(list_0)
        str_3 = base_0.domain()
        gitlab_0 = module_0.Gitlab()
        github_1 = module_0.Github(**dict_0)
        str_4 = base_2.api_url()
    except BaseException:
        pass