# Automatically generated by Pynguin.
import cookiecutter.zipfile as module_0

def test_case_0():
    try:
        bytes_0 = b'v\x82A'
        var_0 = module_0.unzip(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'https://github.com/audreyr/cookiecutte-pypackage/archive/master.zip'
        var_0 = module_0.unzip(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xd4'
        set_0 = set()
        var_0 = module_0.unzip(bytes_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/w-ser.zip'
        var_0 = module_0.unzip(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'http://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
        var_0 = module_0.unzip(str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'test.zip'
        bool_0 = False
        var_0 = module_0.unzip(str_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'test.zip'
        bool_0 = False
        var_0 = module_0.unzip(str_0, bool_0)
    except BaseException:
        pass