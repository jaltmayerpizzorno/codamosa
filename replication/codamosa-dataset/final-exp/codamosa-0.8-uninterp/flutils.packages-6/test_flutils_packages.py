# Automatically generated by Pynguin.
import flutils.packages as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '1.3.4'
    str_1 = module_0.bump_version(str_0)

def test_case_2():
    str_0 = '1.4'
    str_1 = module_0.bump_version(str_0)

def test_case_3():
    str_0 = '1.2.4a0'
    str_1 = module_0.bump_version(str_0)

def test_case_4():
    str_0 = '1.2.3'
    str_1 = module_0.bump_version(str_0)
    int_0 = 1
    str_2 = module_0.bump_version(str_0, int_0)
    int_1 = 2
    str_3 = module_0.bump_version(str_0, int_1)
    int_2 = -1
    str_4 = module_0.bump_version(str_0, int_2)
    int_3 = -2
    str_5 = module_0.bump_version(str_0, int_3)

def test_case_5():
    str_0 = '1.2.3'
    int_0 = 1
    str_1 = module_0.bump_version(str_0, int_0)

def test_case_6():
    str_0 = '1.2.2'
    int_0 = 1
    int_1 = 0
    str_1 = module_0.bump_version(str_0, int_1)
    str_2 = 'A'
    str_3 = module_0.bump_version(str_1, int_0, str_2)

def test_case_7():
    str_0 = '1.2.2'
    int_0 = 2
    str_1 = 'b'
    str_2 = module_0.bump_version(str_0, int_0, str_1)

def test_case_8():
    str_0 = '1.2.2'
    int_0 = 1
    int_1 = 0
    str_1 = module_0.bump_version(str_0, int_1)
    str_2 = module_0.bump_version(str_0, int_0)
    str_3 = 'b'
    str_4 = module_0.bump_version(str_1, int_0, str_3)
    str_5 = module_0.bump_version(str_4)

def test_case_9():
    str_0 = '1.2.2'
    int_0 = 1
    str_1 = 'A'
    str_2 = module_0.bump_version(str_0, int_0, str_1)

def test_case_10():
    int_0 = 1
    str_0 = '1.3.4'
    str_1 = 'b'
    str_2 = module_0.bump_version(str_0, int_0, str_1)

def test_case_11():
    str_0 = '1.2.2'
    int_0 = 2
    str_1 = module_0.bump_version(str_0, int_0)
    str_2 = 'A'
    str_3 = module_0.bump_version(str_1, int_0, str_2)