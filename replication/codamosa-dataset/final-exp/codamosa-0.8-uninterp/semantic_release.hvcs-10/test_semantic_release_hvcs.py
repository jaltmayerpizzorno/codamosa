# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    int_0 = -612
    github_0 = module_0.Github()
    session_0 = github_0.session(int_0, int_0)
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    token_auth_0 = module_0.TokenAuth(dict_0)

def test_case_2():
    float_0 = 1471.8071
    str_0 = 'kp|%'
    token_auth_0 = module_0.TokenAuth(str_0)
    var_0 = token_auth_0.__ne__(float_0)
    gitlab_0 = module_0.Gitlab()
    str_1 = gitlab_0.api_url()
    optional_0 = gitlab_0.token()
    optional_1 = gitlab_0.token()
    optional_2 = gitlab_0.token()

def test_case_3():
    optional_0 = module_0.get_domain()

def test_case_4():
    base_0 = module_0.get_hvcs()
    str_0 = base_0.api_url()

def test_case_5():
    bool_0 = module_0.check_token()

def test_case_6():
    github_0 = module_0.Github()
    session_0 = github_0.session()

def test_case_7():
    str_0 = 'indy-sdk'
    bool_0 = module_0.check_build_status(str_0, str_0, str_0)

def test_case_8():
    str_0 = 'M\x0cJ;\tY]YV%r5a'
    bool_0 = module_0.post_changelog(str_0, str_0, str_0, str_0)

def test_case_9():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.api_url()
    str_1 = None
    str_2 = gitlab_0.api_url()
    bool_0 = module_0.upload_to_release(str_0, str_0, str_0, str_1)

def test_case_10():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.domain()

def test_case_11():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.api_url()

def test_case_12():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.api_url()
    optional_0 = gitlab_0.token()

def test_case_13():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.api_url()
    optional_0 = module_0.get_token()
    optional_1 = module_0.get_domain()

def test_case_14():
    str_0 = ''
    str_1 = "Zuh#/J3F\nCv-E'@9"
    bool_0 = module_0.post_changelog(str_0, str_1, str_1, str_1)
    github_0 = module_0.Github()
    optional_0 = github_0.auth()
    str_2 = '5_\rNvK\x0c7qjbfp'
    str_3 = 'changelog_file'
    str_4 = None
    github_1 = module_0.Github()
    bool_1 = github_1.check_build_status(str_1, str_4, str_2)
    bool_2 = module_0.upload_to_release(str_2, str_0, str_3, str_4)
    int_0 = None
    int_1 = -1834
    token_auth_0 = module_0.TokenAuth(int_1)
    session_0 = github_1.session(int_0)
    var_0 = token_auth_0.__call__(session_0)
    var_1 = token_auth_0.__eq__(int_0)
    list_0 = []
    gitlab_0 = module_0.Gitlab(*list_0)
    str_5 = gitlab_0.api_url()
    github_2 = module_0.Github()
    github_3 = module_0.Github()