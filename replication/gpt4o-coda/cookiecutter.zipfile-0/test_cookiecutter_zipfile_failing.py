# Automatically generated by Pynguin.
import cookiecutter.zipfile as module_0

def test_case_0():
    try:
        float_0 = 54.8
        var_0 = module_0.unzip(float_0, float_0)
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
        str_0 = '+Az45\x0c,8/dX&s)'
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/dev/null'
        int_0 = None
        var_0 = module_0.unzip(str_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'D&HiI/'
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'https://bitbucket.org/{0}'
        str_1 = 'CB8;KRE-*Fk7vDrOG'
        var_0 = module_0.unzip(str_0, str_1)
    except BaseException:
        pass