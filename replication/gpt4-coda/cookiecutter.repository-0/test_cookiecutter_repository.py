# Automatically generated by Pynguin.
import cookiecutter.repository as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ']t4`6Xa5d`H]NUH'
    var_0 = module_0.repository_has_cookiecutter_json(str_0)

def test_case_2():
    str_0 = 'gh'
    str_1 = 'bb'
    str_2 = 'https://github.com/{0}'
    str_3 = 'https://bitbucket.org/{0}'
    str_4 = {str_0: str_2, str_1: str_3}
    str_5 = 'not-an-abbreviation'
    var_0 = module_0.expand_abbreviations(str_5, str_4)
    var_1 = module_0.expand_abbreviations(str_0, str_4)
    str_6 = 'gh:audreyr/cookiecutter-pypackage'
    var_2 = module_0.expand_abbreviations(str_6, str_4)
    str_7 = 'gl:someone/some-repo'
    var_3 = module_0.expand_abbreviations(str_7, str_4)