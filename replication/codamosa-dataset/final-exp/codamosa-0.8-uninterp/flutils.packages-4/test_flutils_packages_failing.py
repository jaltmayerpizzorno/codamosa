# Automatically generated by Pynguin.
import flutils.packages as module_0

def test_case_0():
    try:
        str_0 = '9<vZ|+g^>2'
        str_1 = module_0.bump_version(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '1.2.3'
        int_0 = 3
        str_1 = module_0.bump_version(str_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1.2.3'
        int_0 = 0
        str_1 = 'a'
        str_2 = module_0.bump_version(str_0, int_0, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1.2.3'
        int_0 = -4
        str_1 = module_0.bump_version(str_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'a'
        str_1 = '1.2.4a0'
        str_2 = module_0.bump_version(str_1)
        str_3 = module_0.bump_version(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '1.2.3'
        int_0 = 1
        str_1 = module_0.bump_version(str_0, int_0)
        str_2 = module_0.bump_version(str_1, int_0, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '1.2.2'
        int_0 = 1
        str_1 = module_0.bump_version(str_0, int_0)
        str_2 = '1.3.4'
        int_1 = -1
        str_3 = module_0.bump_version(str_2, int_1)
        str_4 = 'a'
        str_5 = module_0.bump_version(str_3, int_1, str_4)
        version_info_0 = module_0._VersionInfo()
    except BaseException:
        pass