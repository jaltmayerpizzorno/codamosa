# Automatically generated by Pynguin.
import flutils.packages as module_0

def test_case_0():
    try:
        version_info_0 = module_0._VersionInfo()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        str_1 = module_0.bump_version(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'setup.command.'
        str_1 = module_0.bump_version(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1.2.2'
        int_0 = -797
        str_1 = module_0.bump_version(str_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '1.2.3'
        int_0 = 0
        str_1 = module_0.bump_version(str_0, int_0)
        str_2 = module_0.bump_version(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '1.2.3'
        int_0 = 1
        str_1 = module_0.bump_version(str_0, int_0)
        str_2 = module_0.bump_version(str_0, int_0, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '14.2.3'
        int_0 = 0
        str_1 = module_0.bump_version(str_0)
        str_2 = module_0.bump_version(str_0, int_0)
        int_1 = -2
        str_3 = module_0.bump_version(str_0, int_1)
        str_4 = '2.0'
        str_5 = module_0.bump_version(str_4)
        str_6 = 'LePy\nTUQodubu'
        str_7 = module_0.bump_version(str_6)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '1.2a4'
        int_0 = 0
        str_1 = module_0.bump_version(str_0)
        str_2 = module_0.bump_version(str_0, int_0)
        int_1 = 1
        str_3 = module_0.bump_version(str_0, int_1)
        str_4 = '14.3'
        str_5 = module_0.bump_version(str_4)
        str_6 = module_0.bump_version(str_0, int_0, str_3)
    except BaseException:
        pass