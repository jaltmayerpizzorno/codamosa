# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    token_auth_0 = module_0.TokenAuth(bool_0)

def test_case_2():
    str_0 = "b\nMf/\\Z_I'ddk\n"
    set_0 = {str_0, str_0, str_0, str_0}
    bool_0 = True
    token_auth_0 = module_0.TokenAuth(bool_0)
    var_0 = token_auth_0.__ne__(set_0)
    token_auth_1 = module_0.TokenAuth(str_0)

def test_case_3():
    optional_0 = module_0.get_domain()

def test_case_4():
    base_0 = module_0.get_hvcs()
    str_0 = base_0.api_url()

def test_case_5():
    optional_0 = module_0.get_token()

def test_case_6():
    github_0 = module_0.Github()
    session_0 = github_0.session()

def test_case_7():
    str_0 = 'icgc-argo'
    bool_0 = module_0.check_build_status(str_0, str_0, str_0)

def test_case_8():
    str_0 = '0bT^[;'
    bool_0 = module_0.post_changelog(str_0, str_0, str_0, str_0)

def test_case_9():
    str_0 = 'qP'
    str_1 = 'BITBUCKET_BUILD_NUMBER'
    str_2 = None
    bool_0 = module_0.upload_to_release(str_0, str_1, str_0, str_2)

def test_case_10():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.api_url()

def test_case_11():
    base_0 = module_0.get_hvcs()

def test_case_12():
    str_0 = ''
    str_1 = '|fbWaD]96@^UM@\x0c4DI'
    str_2 = 'j'
    bool_0 = module_0.check_token()
    bool_1 = module_0.post_changelog(str_0, str_0, str_1, str_2)