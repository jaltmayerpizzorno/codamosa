# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    base_0 = module_0.get_hvcs()

def test_case_1():
    bool_0 = True
    token_auth_0 = module_0.TokenAuth(bool_0)
    str_0 = None
    str_1 = 'If(G%@ X.'
    bool_1 = module_0.post_changelog(str_1, str_0, str_1, str_1)

def test_case_2():
    optional_0 = module_0.get_domain()
    str_0 = "-uV8v0'ru1WK!h;zHw"
    str_1 = '"kj5c\tz::bH)UvJYdf^z'
    str_2 = ''
    bool_0 = module_0.post_changelog(str_1, str_1, str_2, str_1)
    str_3 = 'Helper for using Twine to upload to PyPI.\n'
    str_4 = 'Bw]-&WT} Wj'
    bool_1 = module_0.check_build_status(str_3, str_4, str_0)
    base_0 = module_0.get_hvcs()
    token_auth_0 = module_0.TokenAuth(str_0)
    var_0 = token_auth_0.__eq__(str_0)

def test_case_3():
    optional_0 = module_0.get_domain()
    str_0 = "-uV8v0'ru1WK!h;zHw"
    str_1 = '"kj5c\tz::bH)UvJYdf^z'
    str_2 = ''
    bool_0 = module_0.post_changelog(str_1, str_1, str_2, str_1)
    str_3 = 'Helper for using Twine to upload to PyPI.\n'
    dict_0 = None
    bytes_0 = b'\xe6\xf3\xc7#hb\x0bc|b\x0c0\xe2V\xaeH\xd7'
    token_auth_0 = module_0.TokenAuth(bytes_0)
    var_0 = token_auth_0.__ne__(dict_0)
    optional_1 = module_0.get_domain()
    base_0 = module_0.get_hvcs()
    str_4 = base_0.domain()
    base_1 = module_0.get_hvcs()
    str_5 = ''
    bool_1 = module_0.check_build_status(str_1, str_3, str_5)
    str_6 = '%}PvZa?@a5%k0'
    str_7 = '9ng(o~xb`'
    str_8 = '#rPg8\r9,k$"w.e\'z$'
    bool_2 = module_0.post_changelog(str_0, str_6, str_7, str_8)

def test_case_4():
    base_0 = module_0.get_hvcs()
    str_0 = base_0.domain()
    optional_0 = base_0.token()

def test_case_5():
    str_0 = 'mgrast'
    str_1 = 'mg-rast-v4-api'
    bool_0 = module_0.check_build_status(str_0, str_1, str_1)

def test_case_6():
    bool_0 = module_0.check_token()

def test_case_7():
    str_0 = 'G}o[?&'
    bool_0 = module_0.post_changelog(str_0, str_0, str_0, str_0)

def test_case_8():
    bool_0 = module_0.check_token()
    str_0 = 'x)iws";a W6q\r*}Xb:1'
    str_1 = 'DCGJ\x0b2U2I5Lpu\n8L'
    bool_1 = module_0.upload_to_release(str_0, str_0, str_0, str_1)

def test_case_9():
    gitlab_0 = module_0.Gitlab()
    str_0 = gitlab_0.api_url()

def test_case_10():
    str_0 = None
    str_1 = 'If(G%@ X.'
    bool_0 = module_0.post_changelog(str_1, str_0, str_1, str_1)
    gitlab_0 = module_0.Gitlab()
    optional_0 = gitlab_0.token()

def test_case_11():
    optional_0 = module_0.get_domain()
    str_0 = '^"\t6DIVljT:us#('
    str_1 = 'No release will be made.'
    str_2 = "-uV8v0'ru1WK!h;zHw"
    str_3 = '"kj5c\tz::bH)UvJYdf^z'
    str_4 = ''
    bool_0 = module_0.post_changelog(str_3, str_3, str_4, str_3)
    str_5 = 'Helper for using Twine to upload to PyPI.\n'
    str_6 = 'Bw]-&WT} Wj'
    bool_1 = module_0.check_build_status(str_5, str_6, str_2)
    bool_2 = module_0.post_changelog(str_0, str_1, str_0, str_2)

def test_case_12():
    optional_0 = module_0.get_domain()
    str_0 = 'BRANCH_NAME'
    str_1 = "zd'$."
    str_2 = 'XRD'
    bool_0 = module_0.upload_to_release(str_0, str_1, str_2, str_2)
    str_3 = '^"\t6DIVljT:us#('
    dict_0 = {}
    token_auth_0 = module_0.TokenAuth(dict_0)
    base_0 = module_0.get_hvcs()
    str_4 = base_0.domain()
    github_0 = module_0.Github()
    session_0 = github_0.session()
    var_0 = token_auth_0.__call__(session_0)
    int_0 = 1599
    var_1 = token_auth_0.__ne__(int_0)
    optional_1 = module_0.get_domain()
    str_5 = base_0.domain()
    gitlab_0 = module_0.Gitlab()
    str_6 = gitlab_0.api_url()
    bool_1 = module_0.check_build_status(str_5, str_3, str_3)
    str_7 = ''
    str_8 = 'pmwN`$l%u\t\t\\T@hX8'
    str_9 = '0\rTCijh'
    bool_2 = module_0.post_changelog(str_8, str_9, str_4, str_7)