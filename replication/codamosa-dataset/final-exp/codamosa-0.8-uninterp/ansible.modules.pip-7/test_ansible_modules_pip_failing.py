# Automatically generated by Pynguin.
import ansible.modules.pip as module_0

def test_case_0():
    try:
        int_0 = -199
        str_0 = 'CDuOH5s'
        str_1 = 'u'
        var_0 = module_0.setup_virtualenv(int_0, str_0, str_0, str_1, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1819.29
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
        package_0 = module_0.Package(dict_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'foo'
        str_1 = '=0.1V'
        package_0 = module_0.Package(str_0, str_1)
        var_0 = package_0.is_satisfied_by(str_0)
        str_2 = 'hu'
        list_0 = [str_2]
        list_1 = [list_0]
        package_1 = module_0.Package(list_1)
        var_1 = package_1.is_satisfied_by(list_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'hu'
        list_0 = [str_0]
        list_1 = [list_0]
        package_0 = module_0.Package(list_1)
        var_0 = package_0.__str__()
        var_1 = package_0.is_satisfied_by(list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        bool_1 = False
        dict_0 = {bool_1: bool_0}
        package_0 = module_0.Package(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'foo'
        str_1 = '0.1V'
        package_0 = module_0.Package(str_0, str_1)
        var_0 = package_0.is_satisfied_by(str_0)
        str_2 = 'hu'
        list_0 = [str_2]
        list_1 = [list_0]
        package_1 = module_0.Package(list_1)
        var_1 = package_1.is_satisfied_by(list_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'foo'
        str_1 = '=0.1V'
        package_0 = module_0.Package(str_0, str_1)
        var_0 = package_0.is_satisfied_by(str_0)
        var_1 = package_0.__str__()
        str_2 = 'hu'
        str_3 = 'Q6A$jh'
        var_2 = package_0.is_satisfied_by(str_3)
        list_0 = [str_2]
        list_1 = [list_0]
        package_1 = module_0.Package(list_1)
        tuple_0 = ()
        var_3 = package_1.is_satisfied_by(tuple_0)
    except BaseException:
        pass