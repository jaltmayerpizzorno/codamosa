# Automatically generated by Pynguin.
import cookiecutter.repository as module_0

def test_case_0():
    try:
        set_0 = set()
        var_0 = module_0.is_zip_file(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        var_0 = module_0.expand_abbreviations(bool_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x0bW'
        var_0 = module_0.repository_has_cookiecutter_json(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/home/my-repos/cookiecuters/modern-package/'
        var_0 = {}
        bool_0 = True
        var_1 = module_0.determine_repo_dir(str_0, var_0, str_0, var_0, bool_0, var_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'MZlXB.mYb{w-y'
        complex_0 = None
        float_0 = -1246.9427592570125
        str_1 = '7=z\\-gic~ua~h=s>j.zip'
        float_1 = 104.909405
        var_0 = module_0.determine_repo_dir(str_1, str_0, complex_0, float_1, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        var_0 = {}
        bool_0 = False
        var_1 = module_0.determine_repo_dir(str_0, var_0, str_0, var_0, bool_0, var_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '.'
        bool_0 = True
        dict_0 = {str_0: bool_0, str_0: bool_0, bool_0: str_0}
        str_1 = 'oNk u\n@]]o2l^1'
        complex_0 = None
        str_2 = '={Hy?A!u4*TIY`\x0bdZ'
        set_0 = {str_2, str_2, complex_0, complex_0}
        var_0 = module_0.expand_abbreviations(str_0, set_0)
        float_0 = -1246.943
        var_1 = module_0.determine_repo_dir(bool_0, dict_0, str_1, complex_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '7=Z\\-giC~uA~hGS>J'
        str_1 = 'oNk u\n@]]o2l^1'
        complex_0 = None
        str_2 = 'qz'
        set_0 = {str_2, str_2, complex_0, complex_0}
        var_0 = module_0.expand_abbreviations(str_0, set_0)
        str_3 = ':B4Vm'
        var_1 = module_0.expand_abbreviations(str_3, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'git@github.com/audreyr/cookiecutter-pypackage'
        var_0 = {}
        str_1 = 'cookiecutter-pypackage'
        str_2 = ''
        bool_0 = True
        var_1 = module_0.determine_repo_dir(str_0, var_0, str_1, str_2, bool_0)
    except BaseException:
        pass