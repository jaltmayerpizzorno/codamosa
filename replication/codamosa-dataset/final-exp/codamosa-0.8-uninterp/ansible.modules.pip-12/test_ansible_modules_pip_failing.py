# Automatically generated by Pynguin.
import ansible.modules.pip as module_0

def test_case_0():
    try:
        str_0 = 'd!s*&8+)=J.(149en\r'
        package_0 = module_0.Package(str_0)
        var_0 = package_0.__str__()
        bool_0 = False
        tuple_0 = (bool_0,)
        int_0 = 165
        var_1 = package_0.is_satisfied_by(int_0)
        float_0 = 2691.53326
        str_1 = 'O~}IN\x0ca&-'
        var_2 = package_0.__str__()
        bool_1 = True
        var_3 = module_0.setup_virtualenv(package_0, tuple_0, float_0, str_1, bool_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        package_0 = module_0.Package(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ansrble.modules.pip'
        package_0 = module_0.Package(str_0)
        var_0 = package_0.is_satisfied_by(package_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '7W'
        str_1 = '+'
        str_2 = '`fB\x0b-kb[.^o7?k T^'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_2}
        package_0 = module_0.Package(dict_0)
        var_0 = package_0.__str__()
        str_3 = 'distribute'
        package_1 = module_0.Package(str_3)
        bytes_0 = b'tz\xe2\xd3\xb9\xab'
        var_1 = package_1.__str__()
        var_2 = package_1.is_satisfied_by(bytes_0)
    except BaseException:
        pass