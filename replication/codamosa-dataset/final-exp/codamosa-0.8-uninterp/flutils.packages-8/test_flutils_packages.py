# Automatically generated by Pynguin.
import flutils.packages as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '1.3.4'
    str_1 = module_0.bump_version(str_0)

def test_case_2():
    str_0 = '1.34'
    str_1 = module_0.bump_version(str_0)

def test_case_3():
    str_0 = 'a'
    str_1 = '1.2.4a0'
    str_2 = module_0.bump_version(str_1)

def test_case_4():
    int_0 = 1
    str_0 = '1.2.3'
    str_1 = module_0.bump_version(str_0, int_0)

def test_case_5():
    str_0 = '1.3.4'
    int_0 = 0
    str_1 = module_0.bump_version(str_0, int_0)
    str_2 = 'a'
    str_3 = '1.2.4a0'
    str_4 = module_0.bump_version(str_3)

def test_case_6():
    str_0 = '1.2.2'
    int_0 = 2
    str_1 = 'a'
    str_2 = module_0.bump_version(str_0, int_0, str_1)

def test_case_7():
    str_0 = '1.2.2'
    str_1 = module_0.bump_version(str_0)
    str_2 = '1.2.3'
    int_0 = 1
    str_3 = module_0.bump_version(str_2, int_0)
    str_4 = '1.3.4'
    str_5 = module_0.bump_version(str_4, int_0)
    str_6 = 'a'
    str_7 = module_0.bump_version(str_2)
    str_8 = '1.2.4a0'
    str_9 = module_0.bump_version(str_8)
    int_1 = -3
    str_10 = module_0.bump_version(str_3, int_1)