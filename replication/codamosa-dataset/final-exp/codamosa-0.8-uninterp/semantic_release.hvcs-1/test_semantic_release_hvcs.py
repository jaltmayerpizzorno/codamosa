# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    pass

def test_case_1():
    github_0 = None
    list_0 = [github_0, github_0, github_0]
    base_0 = module_0.get_hvcs()
    list_1 = [base_0, base_0, base_0]
    bytes_0 = None
    tuple_0 = (base_0, list_1, bytes_0)
    tuple_1 = (tuple_0,)
    token_auth_0 = module_0.TokenAuth(tuple_1)
    token_auth_1 = module_0.TokenAuth(token_auth_0)
    var_0 = token_auth_1.__eq__(list_0)

def test_case_2():
    dict_0 = {}
    gitlab_0 = module_0.Gitlab(**dict_0)
    str_0 = '\tn>>q'
    str_1 = 'wQ'
    base_0 = module_0.get_hvcs()
    bool_0 = base_0.check_build_status(str_0, str_1, str_1)
    str_2 = 'retry'
    str_3 = ''
    bool_1 = base_0.check_build_status(str_2, str_1, str_3)
    str_4 = 'label'
    list_0 = []
    str_5 = 'soG\\)Ac?'
    dict_1 = {}
    token_auth_0 = module_0.TokenAuth(dict_1)
    var_0 = token_auth_0.__eq__(str_5)
    str_6 = 'I)uqLn\t'
    token_auth_1 = module_0.TokenAuth(str_6)
    var_1 = token_auth_1.__ne__(list_0)
    base_1 = module_0.get_hvcs()
    bool_2 = base_1.check_build_status(str_4, str_4, str_4)
    optional_0 = gitlab_0.token()

def test_case_3():
    github_0 = module_0.Github()
    str_0 = github_0.domain()

def test_case_4():
    str_0 = 'airflow'
    bool_0 = module_0.check_build_status(str_0, str_0, str_0)

def test_case_5():
    str_0 = '_C\x0bqYRpM(:\x0cj'
    str_1 = None
    bool_0 = module_0.post_changelog(str_0, str_1, str_0, str_1)

def test_case_6():
    str_0 = "G9X'p"
    bool_0 = module_0.upload_to_release(str_0, str_0, str_0, str_0)

def test_case_7():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.domain()

def test_case_8():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.api_url()

def test_case_9():
    str_0 = '(S\nQ`\txw3fune]#)'
    str_1 = 'v}3Q?'
    str_2 = 'Qf0fY0K\x0bWe|^;7x'
    str_3 = 'n\nZ,7qTpL[D['
    bool_0 = module_0.upload_to_release(str_0, str_1, str_2, str_3)
    optional_0 = module_0.get_token()

def test_case_10():
    str_0 = '(S\nQ`\txw3fune]#)'
    str_1 = 'v}3Q?'
    str_2 = 'Qf0fY0K\x0bWe|^;7x'
    str_3 = 'n\nZJ,7qTpL[DJ['
    bool_0 = module_0.upload_to_release(str_0, str_1, str_2, str_3)
    optional_0 = module_0.get_domain()

def test_case_11():
    bool_0 = module_0.check_token()
    str_0 = "y!w=E?8'OK0"
    str_1 = 'breaking'
    gitlab_0 = module_0.Gitlab()
    str_2 = gitlab_0.api_url()
    bool_1 = module_0.post_changelog(str_0, str_0, str_0, str_1)

def test_case_12():
    str_0 = 'Post changelog.'
    str_1 = '@s'
    bool_0 = True
    token_auth_0 = module_0.TokenAuth(bool_0)
    bool_1 = module_0.post_changelog(str_0, str_0, str_0, str_1)
    str_2 = '\n    Decorator that adds all the options in COMMON_OPTIONS\n    '
    str_3 = '"h!$J'
    str_4 = '/vqtH>$T.3{9G'
    str_5 = 'L;smXO&3|0G\x0cxK'
    bool_2 = module_0.post_changelog(str_2, str_3, str_4, str_5)
    str_6 = 'n\nZJ,7qTpL[DJ'
    str_7 = '`iJZs~'
    str_8 = 'Xm|L'
    bool_3 = module_0.upload_to_release(str_7, str_1, str_6, str_8)
    github_0 = module_0.Github()
    session_0 = github_0.session(bool_1)
    var_0 = token_auth_0.__call__(session_0)