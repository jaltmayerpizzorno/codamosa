# Automatically generated by Pynguin.
import ansible.modules.pip as module_0

def test_case_0():
    try:
        bool_0 = False
        float_0 = -109.0
        int_0 = 4601
        str_0 = '\n    Returns True if checksum value has supported URL scheme, else False.'
        var_0 = module_0.setup_virtualenv(bool_0, float_0, int_0, str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        str_0 = "h+?}_c9'w\x0cgs\x0b+1&x)B"
        package_0 = module_0.Package(list_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0]
        package_0 = module_0.Package(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\\>SO'
        package_0 = module_0.Package(str_0)
        var_0 = package_0.__str__()
        dict_0 = None
        list_0 = [var_0, dict_0, str_0]
        package_1 = module_0.Package(dict_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'i'
        package_0 = module_0.Package(str_0)
        var_0 = package_0.is_satisfied_by(package_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -1038.0
        str_0 = '1'
        package_0 = module_0.Package(float_0, str_0)
    except BaseException:
        pass