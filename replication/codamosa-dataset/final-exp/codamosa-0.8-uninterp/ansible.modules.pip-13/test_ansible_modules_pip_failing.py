# Automatically generated by Pynguin.
import ansible.modules.pip as module_0

def test_case_0():
    try:
        float_0 = 216.208
        dict_0 = {}
        set_0 = set()
        package_0 = module_0.Package(dict_0)
        str_0 = 'i:~S.Gi Haw'
        var_0 = module_0.setup_virtualenv(float_0, dict_0, set_0, package_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 438
        tuple_0 = (int_0,)
        bytes_0 = b'\xc0\xb6n_v\x9a&\x85\xd5\xad\xf1\xa5q\xf6t'
        package_0 = module_0.Package(tuple_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '__main__'
        bool_0 = True
        package_0 = module_0.Package(str_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ilte'
        package_0 = module_0.Package(str_0)
        list_0 = [package_0]
        var_0 = package_0.is_satisfied_by(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xd3\xc9\xdbb+\xe7\xba\xdd9\xf1'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        package_0 = module_0.Package(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = []
        package_0 = module_0.Package(list_0)
        str_0 = 'sTojT$buQV*LK'
        str_1 = 'fE:,.'
        package_1 = module_0.Package(str_1, str_0)
        str_2 = '(v,R[P"5^p8|/2WgZF'
        package_2 = module_0.Package(str_2)
        int_0 = -101
        var_0 = package_2.canonicalize_name(int_0)
    except BaseException:
        pass