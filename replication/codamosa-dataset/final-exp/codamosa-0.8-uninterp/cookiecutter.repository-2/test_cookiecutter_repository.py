# Automatically generated by Pynguin.
import cookiecutter.repository as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'qugw0`Zi^'
    var_0 = module_0.is_zip_file(str_0)

def test_case_2():
    str_0 = 'bb'
    str_1 = 'https://github.com/{}.git'
    str_2 = 'https://bitbucket.org/{}.git'
    str_3 = {str_1: str_1, str_0: str_2}
    str_4 = 'gh:audreyr/cookiecutter-pypackage'
    var_0 = module_0.expand_abbreviations(str_4, str_3)
    str_5 = 'bb:pydanny/cookiecutter-django'
    var_1 = module_0.expand_abbreviations(str_5, str_3)