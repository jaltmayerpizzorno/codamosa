# Automatically generated by Pynguin.
import cookiecutter.zipfile as module_0

def test_case_0():
    try:
        str_0 = 'Unable to parse YAML file {}.'
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = None
        var_0 = module_0.unzip(set_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'F,/W:zBy;#F'
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'https://github.com/{0}.git'
        float_0 = -737.11873
        dict_0 = {}
        tuple_0 = (str_0, float_0, dict_0)
        var_0 = module_0.unzip(str_0, tuple_0, str_0, float_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'https://github.com/{0}.git'
        var_0 = module_0.unzip(str_0, str_0)
    except BaseException:
        pass