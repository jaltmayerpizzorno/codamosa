# Automatically generated by Pynguin.
import cookiecutter.zipfile as module_0

def test_case_0():
    try:
        str_0 = 'tests/test-repo-pre/'
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        var_0 = module_0.unzip(bool_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'M/Y9JS,"Z}3b'
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'https://github.com/abhirfma/cookiecutter-matlb/archive/mast{r.zip'
        bool_0 = True
        var_0 = module_0.unzip(str_0, bool_0, str_0, bool_0)
    except BaseException:
        pass