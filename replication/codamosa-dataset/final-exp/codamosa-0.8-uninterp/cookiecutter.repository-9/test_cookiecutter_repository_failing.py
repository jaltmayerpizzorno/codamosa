# Automatically generated by Pynguin.
import cookiecutter.repository as module_0

def test_case_0():
    try:
        str_0 = '__`main__'
        str_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.determine_repo_dir(str_0, str_1, str_0, str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '_`m.n__'
        str_1 = {}
        var_0 = module_0.determine_repo_dir(str_0, str_1, str_0, str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        var_0 = module_0.repository_has_cookiecutter_json(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '_n?ew_lines'
        set_0 = {str_0, str_0, str_0, str_0}
        dict_0 = {str_0: set_0, str_0: str_0}
        str_1 = 'o].zip'
        var_0 = module_0.repository_has_cookiecutter_json(str_1)
        list_0 = [str_0, dict_0, str_0]
        bytes_0 = b'<\x02$&$\xady\x01`D\xda!\xc9%\x97r\x82\x18'
        var_1 = module_0.determine_repo_dir(str_1, str_0, dict_0, set_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "L5'"
        str_1 = ':F'
        int_0 = 0
        bool_0 = False
        bytes_0 = b'*~^\t\x91\xe5@\xf8\xdc\xd6\xbf\x12\xa1g\xb1'
        tuple_0 = (int_0, str_1, bool_0, bytes_0)
        var_0 = module_0.expand_abbreviations(str_0, tuple_0)
        var_1 = module_0.repository_has_cookiecutter_json(str_1)
        str_2 = 'o].zip'
        int_1 = -3103
        var_2 = module_0.determine_repo_dir(str_1, str_2, int_1, int_1, int_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        str_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.determine_repo_dir(str_0, str_1, str_0, str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'test'
        str_1 = 'https://github.com/{}/'
        str_2 = {str_0: str_1}
        var_0 = None
        bool_0 = False
        str_3 = 'test/test-test'
        var_1 = module_0.determine_repo_dir(str_0, str_2, str_3, var_0, bool_0, var_0, str_3)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'test'
        var_0 = {}
        bool_0 = False
        var_1 = module_0.determine_repo_dir(str_0, var_0, str_0, str_0, bool_0)
    except BaseException:
        pass