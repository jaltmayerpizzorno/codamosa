# Automatically generated by Pynguin.
import flutils.packages as module_0

def test_case_0():
    try:
        str_0 = ''
        str_1 = module_0.bump_version(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '=B1+Y@}YEkqc'
        str_1 = module_0.bump_version(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1.2.2'
        int_0 = 0
        str_1 = module_0.bump_version(str_0, int_0)
        int_1 = 3485
        str_2 = module_0.bump_version(str_0, int_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1.2.2'
        str_1 = module_0.bump_version(str_0)
        int_0 = 2
        str_2 = 'a'
        str_3 = module_0.bump_version(str_0, int_0, str_2)
        str_4 = '1.2.3'
        int_1 = 1
        str_5 = module_0.bump_version(str_4, int_1)
        int_2 = -717
        str_6 = module_0.bump_version(str_1, int_2)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '1.2.2'
        str_1 = module_0.bump_version(str_0)
        int_0 = 1
        str_2 = '?'
        str_3 = module_0.bump_version(str_1, int_0, str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '1.2.3'
        str_1 = module_0.bump_version(str_0)
        int_0 = 0
        str_2 = module_0.bump_version(str_0, int_0)
        str_3 = '1.2.4'
        str_4 = 'a'
        str_5 = module_0.bump_version(str_3, int_0, str_4)
    except BaseException:
        pass