# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    try:
        github_0 = module_0.Github()
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
        str_0 = '{w)`jG@7m'
        list_0 = []
        base_0 = module_0.Base(*list_0)
        bool_0 = base_0.check_build_status(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'yasc`'
        list_0 = [str_0, str_0]
        bool_0 = True
        token_auth_0 = module_0.TokenAuth(bool_0)
        var_0 = token_auth_0.__call__(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'bCk{BJ'
        optional_0 = module_0.get_domain()
        str_1 = 'gitlab-ci-token:'
        gitlab_0 = module_0.Gitlab()
        bool_0 = gitlab_0.check_build_status(str_1, str_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        base_0 = module_0.get_hvcs()
        str_0 = base_0.domain()
        optional_0 = module_0.get_token()
        str_1 = base_0.api_url()
        str_2 = '-%'
        list_0 = []
        str_3 = ''
        int_0 = None
        token_auth_0 = module_0.TokenAuth(int_0)
        dict_0 = {str_0: str_0, str_3: str_3, str_2: token_auth_0}
        gitlab_0 = module_0.Gitlab(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = "o.H'ZyV]F,U"
        str_1 = '8@X]d)ekf%HDO\r/"i`W'
        github_0 = module_0.Github()
        bool_0 = github_0.check_build_status(str_0, str_1, str_1)
        base_0 = module_0.get_hvcs()
        str_2 = 'pz|(D1='
        github_1 = module_0.Github()
        str_3 = github_1.api_url()
        str_4 = base_0.api_url()
        dict_0 = {str_2: str_2, str_2: str_2}
        str_5 = 'L'
        str_6 = 'C9D6aQh}\x0c9R[]wr&k]'
        bool_1 = module_0.post_changelog(str_2, str_5, str_6, str_5)
        gitlab_0 = module_0.Gitlab(**dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'M1:F h"8?8B~SWWoW$'
        str_1 = 'No release will be made.'
        bool_0 = module_0.post_changelog(str_0, str_1, str_0, str_1)
        base_0 = module_0.Base()
        optional_0 = base_0.token()
    except BaseException:
        pass