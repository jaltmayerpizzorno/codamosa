# Automatically generated by Pynguin.
import flutils.packages as module_0

def test_case_0():
    try:
        str_0 = None
        str_1 = module_0.bump_version(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '1.2'
        int_0 = 2
        str_1 = 'a'
        str_2 = module_0.bump_version(str_0, int_0, str_1)
        str_3 = module_0.bump_version(str_2, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1.2.2'
        str_1 = module_0.bump_version(str_0)
        int_0 = 2
        int_1 = -27
        str_2 = module_0.bump_version(str_1)
        str_3 = 'a'
        str_4 = module_0.bump_version(str_1, int_0, str_3)
        str_5 = module_0.bump_version(str_2, int_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1.2.2'
        int_0 = 1
        str_1 = '1.34'
        str_2 = module_0.bump_version(str_1)
        str_3 = 'a'
        str_4 = module_0.bump_version(str_0, int_0, str_3)
        str_5 = module_0.bump_version(str_4, int_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '1.2.2'
        str_1 = module_0.bump_version(str_0)
        int_0 = -3
        str_2 = module_0.bump_version(str_1)
        str_3 = 'a'
        str_4 = module_0.bump_version(str_1, int_0, str_3)
    except BaseException:
        pass