# Automatically generated by Pynguin.
import flutils.packages as module_0

def test_case_0():
    try:
        str_0 = ''
        str_1 = module_0.bump_version(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '1.2.3'
        int_0 = -1
        str_1 = module_0.bump_version(str_0, int_0)
        str_2 = 'b'
        str_3 = module_0.bump_version(str_0, int_0, str_2)
        int_1 = 545
        str_4 = module_0.bump_version(str_1, int_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1.2.3'
        str_1 = module_0.bump_version(str_0)
        int_0 = 0
        str_2 = module_0.bump_version(str_0, int_0)
        str_3 = 'a'
        str_4 = module_0.bump_version(str_0, int_0, str_3)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1.2.3'
        int_0 = -1
        str_1 = module_0.bump_version(str_0, int_0)
        str_2 = 'b'
        str_3 = module_0.bump_version(str_0, int_0, str_2)
        int_1 = -3589
        str_4 = module_0.bump_version(str_3, int_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '1.2.3'
        str_1 = module_0.bump_version(str_0)
        int_0 = 1
        str_2 = module_0.bump_version(str_0, int_0)
        str_3 = '\\'
        str_4 = module_0.bump_version(str_0, int_0, str_3)
    except BaseException:
        pass