# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    try:
        optional_0 = module_0.get_domain()
        base_0 = module_0.Base()
        str_0 = base_0.api_url()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = module_0.check_token()
        base_0 = module_0.get_hvcs()
        str_0 = base_0.domain()
        base_1 = module_0.Base()
        optional_0 = base_1.token()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Q!96oC2Bg'
        str_1 = 'O?Z\tPK^X*a.DcO\x0c'
        str_2 = 'changelog'
        str_3 = 'prerelease'
        str_4 = 'lONmCK,'
        bool_0 = module_0.upload_to_release(str_2, str_3, str_3, str_4)
        base_0 = module_0.Base()
        bool_1 = base_0.check_build_status(str_0, str_1, str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = None
        bytes_1 = b'\xb2\x18>*4\xdf\x00V>\xc6'
        token_auth_0 = module_0.TokenAuth(bytes_1)
        var_0 = token_auth_0.__call__(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        github_0 = module_0.Github()
        str_0 = github_0.domain()
        float_0 = -1157.14
        token_auth_0 = module_0.TokenAuth(float_0)
        gitlab_0 = module_0.Gitlab()
        bool_0 = gitlab_0.check_build_status(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        optional_0 = module_0.get_token()
        list_0 = [optional_0, optional_0, optional_0]
        gitlab_0 = module_0.Gitlab(*list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '"A@EK`*og&=N#V&'
        optional_0 = module_0.get_token()
        str_1 = ':\x0b-h00ubH'
        str_2 = 'No release found to upload assets to'
        bool_0 = module_0.post_changelog(str_0, str_0, str_1, str_2)
        base_0 = module_0.Base()
        str_3 = base_0.domain()
    except BaseException:
        pass

def test_case_7():
    try:
        gitlab_0 = module_0.Gitlab()
        base_0 = module_0.get_hvcs()
        str_0 = gitlab_0.api_url()
        str_1 = gitlab_0.domain()
        str_2 = 'Z?dzqY<: \\eVh'
        str_3 = 'Github domain property\n\n        :return: The Github domain\n        '
        str_4 = '-:'
        bool_0 = base_0.check_build_status(str_2, str_3, str_4)
        optional_0 = module_0.get_token()
        str_5 = base_0.api_url()
        bool_1 = module_0.post_changelog(str_2, str_0, str_4, str_3)
        set_0 = {str_0, str_5}
        base_1 = module_0.get_hvcs()
        token_auth_0 = module_0.TokenAuth(set_0)
        github_0 = module_0.Github()
        session_0 = github_0.session()
        var_0 = token_auth_0.__call__(session_0)
        var_1 = token_auth_0.__call__(str_4)
    except BaseException:
        pass