# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    try:
        str_0 = None
        bool_0 = module_0.post_changelog(str_0, str_0, str_0, str_0)
        gitlab_0 = module_0.Gitlab()
        str_1 = gitlab_0.domain()
        base_0 = module_0.Base()
        str_2 = base_0.domain()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        bool_0 = module_0.post_changelog(str_0, str_0, str_0, str_0)
        github_0 = module_0.Github()
        gitlab_0 = module_0.Gitlab()
        str_1 = gitlab_0.domain()
        base_0 = module_0.Base()
        token_auth_0 = module_0.TokenAuth(github_0)
        str_2 = base_0.api_url()
    except BaseException:
        pass

def test_case_2():
    try:
        github_0 = module_0.Github()
        optional_0 = github_0.auth()
        github_1 = module_0.Github()
        str_0 = github_1.api_url()
        bool_0 = module_0.check_token()
        base_0 = module_0.Base()
        optional_1 = github_1.token()
        optional_2 = base_0.token()
    except BaseException:
        pass

def test_case_3():
    try:
        github_0 = module_0.Github()
        str_0 = 'mokJ}'
        str_1 = 'X/VQ}pK${p:~A}\t!.]%'
        str_2 = None
        bool_0 = github_0.check_build_status(str_0, str_1, str_2)
        base_0 = module_0.get_hvcs()
        str_3 = base_0.api_url()
        str_4 = base_0.api_url()
        session_0 = github_0.session()
        token_auth_0 = module_0.TokenAuth(session_0)
        github_1 = module_0.Github()
        str_5 = '='
        list_0 = []
        base_1 = module_0.Base(*list_0)
        bool_1 = base_1.check_build_status(str_4, str_5, str_5)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'wo>['
        token_auth_0 = None
        str_1 = 'sU3 +0X)+2N9aTow>'
        str_2 = 'Q[B!4mwLzF\x0bdUT&Y%'
        bool_0 = module_0.upload_to_release(str_0, str_1, str_2, str_0)
        str_3 = 'ncP:?zrS_2C}x@%j6t'
        dict_0 = {str_0: str_3, str_0: str_3, token_auth_0: str_3}
        var_0 = token_auth_0.__eq__(dict_0)
        token_auth_1 = module_0.TokenAuth(str_3)
        var_1 = token_auth_1.__call__(token_auth_0)
    except BaseException:
        pass

def test_case_5():
    try:
        optional_0 = module_0.get_domain()
        gitlab_0 = module_0.Gitlab()
        optional_1 = gitlab_0.token()
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        str_0 = 'QPw;hp'
        str_1 = '\n    Performs necessary checks to ensure that the travis build is one\n    that should create releases.\n\n    :param branch: The branch the environment should be running against.\n    '
        gitlab_0 = module_0.Gitlab(*list_0)
        bool_0 = module_0.post_changelog(str_0, str_0, str_0, str_1)
        base_0 = module_0.get_hvcs()
        github_0 = module_0.Github()
        bool_1 = module_0.check_token()
        optional_0 = gitlab_0.token()
        str_2 = 'kmG'
        str_3 = 'rNT'
        bool_2 = gitlab_0.check_build_status(str_2, str_0, str_3)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = module_0.check_token()
        github_0 = module_0.Github()
        gitlab_0 = module_0.Gitlab()
        session_0 = github_0.session()
        dict_0 = {gitlab_0: github_0}
        token_auth_0 = module_0.TokenAuth(dict_0)
        var_0 = token_auth_0.__call__(session_0)
        optional_0 = module_0.get_domain()
        token_auth_1 = module_0.TokenAuth(gitlab_0)
        optional_1 = github_0.auth()
        list_0 = []
        var_1 = token_auth_1.__eq__(list_0)
        gitlab_1 = module_0.Gitlab()
        optional_2 = gitlab_1.token()
        int_0 = -341
        var_2 = token_auth_1.__eq__(int_0)
        github_1 = module_0.Github()
        optional_3 = github_0.auth()
        optional_4 = module_0.get_token()
        base_0 = module_0.get_hvcs()
        base_1 = module_0.Base()
        token_auth_2 = module_0.TokenAuth(base_0)
        base_2 = module_0.Base()
        str_0 = base_2.domain()
    except BaseException:
        pass