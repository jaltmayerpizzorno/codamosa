# Automatically generated by Pynguin.
import cookiecutter.zipfile as module_0

def test_case_0():
    try:
        dict_0 = None
        float_0 = None
        var_0 = module_0.unzip(dict_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xb7\x80\xb4'
        dict_0 = None
        var_0 = module_0.unzip(bytes_0, dict_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -1777
        str_0 = "6s=1\x0bBy>M'R@"
        var_0 = module_0.unzip(int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\rLl/^>eAG(^'
        float_0 = -775.4
        var_0 = module_0.unzip(str_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zi\n'
        bool_0 = True
        var_0 = module_0.unzip(str_0, bool_0)
    except BaseException:
        pass