# Automatically generated by Pynguin.
import cookiecutter.zipfile as module_0

def test_case_0():
    try:
        float_0 = 1010.995
        var_0 = module_0.unzip(float_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'ptN'
        dict_0 = None
        var_0 = module_0.unzip(str_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'lpkP;wC#UNJaft/Wz%'
        bytes_0 = b'\xb0~\x86'
        var_0 = module_0.unzip(str_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'https://github.com/audreyr/\\ookiecutter-pypackage/archive/master.zip'
        bool_0 = True
        var_0 = module_0.unzip(str_0, bool_0, str_0, bool_0)
    except BaseException:
        pass