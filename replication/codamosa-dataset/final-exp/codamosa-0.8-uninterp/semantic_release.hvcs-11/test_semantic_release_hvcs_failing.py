# Automatically generated by Pynguin.
import semantic_release.hvcs as module_0

def test_case_0():
    try:
        base_0 = module_0.Base()
        str_0 = 'Upload wheels to PyPI with Twine.\n\n    Wheels must already be created and stored at the given path.\n\n    Credentials are taken from either the environment variable\n    ``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.\n\n    :param path: Path to dist folder containing the files to upload.\n    :param skip_existing: Continue uploading files if one already exists.\n        (Only valid when uploading to PyPI. Other implementations may not support this.)\n    :param glob_patterns: List of glob patterns to include in the upload (["*"] by default).\n    '
        str_1 = 'qX '
        str_2 = None
        bool_0 = module_0.upload_to_release(str_0, str_1, str_2, str_0)
        github_0 = module_0.Github()
        optional_0 = github_0.token()
        optional_1 = github_0.auth()
        str_3 = base_0.domain()
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        github_0 = module_0.Github()
        optional_0 = github_0.auth()
        optional_1 = module_0.get_domain()
        gitlab_0 = module_0.Gitlab(*list_0)
        base_0 = module_0.Base()
        optional_2 = base_0.token()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'c[y:oCX)5$|'
        token_auth_0 = module_0.TokenAuth(str_0)
        github_0 = module_0.Github()
        token_auth_1 = module_0.TokenAuth(github_0)
        var_0 = token_auth_1.__call__(token_auth_0)
    except BaseException:
        pass

def test_case_3():
    try:
        gitlab_0 = module_0.Gitlab()
        str_0 = '\r=xM;hG./~7(LH\x0b)~-q'
        str_1 = '^1>T-SOsV*\t\x0cwhzZ,HE'
        bool_0 = gitlab_0.check_build_status(str_0, str_1, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'X~VSeVc=my0O\n&'
        str_1 = ':_\nFWx,5WbEx\tlJ\tP'
        str_2 = 'ViHb\x0c=t}upZ+b?'
        str_3 = 's|"|:n431H'
        bool_0 = module_0.post_changelog(str_0, str_1, str_2, str_3)
        base_0 = module_0.Base()
        str_4 = base_0.api_url()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'i\tom#":mj'
        str_1 = 'Mgu&7Mt6'
        str_2 = 'Could not decode pyproject.toml: '
        str_3 = '|/^Gc7E;M{>V!Dn(I'
        bool_0 = module_0.post_changelog(str_1, str_2, str_2, str_3)
        base_0 = module_0.get_hvcs()
        str_4 = '!sC/:S\rG'
        str_5 = 'iNyg'
        base_1 = module_0.Base()
        bool_1 = base_1.check_build_status(str_0, str_4, str_5)
    except BaseException:
        pass

def test_case_6():
    try:
        optional_0 = module_0.get_token()
        base_0 = module_0.get_hvcs()
        gitlab_0 = module_0.Gitlab()
        list_0 = [gitlab_0]
        bool_0 = False
        github_0 = module_0.Github()
        session_0 = github_0.session(bool_0)
        str_0 = 'fA1CFD'
        str_1 = 'H[rBv}'
        dict_0 = {str_0: optional_0, str_1: list_0}
        token_auth_0 = module_0.TokenAuth(dict_0)
        token_auth_1 = module_0.TokenAuth(token_auth_0)
        var_0 = token_auth_1.__call__(session_0)
        base_1 = module_0.Base(*list_0)
    except BaseException:
        pass