# Automatically generated by Pynguin.
import ansible.module_utils.compat.version as module_0

def test_case_0():
    try:
        str_0 = 'mu5XToTD2Nd~>'
        loose_version_0 = module_0.LooseVersion()
        strict_version_0 = module_0.StrictVersion(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "1sZtBg'&I$\\q\r[$/,oa"
        loose_version_0 = module_0.LooseVersion(str_0)
        var_0 = loose_version_0.__gt__(loose_version_0)
        version_0 = module_0.Version()
        var_1 = version_0.__repr__()
    except BaseException:
        pass

def test_case_2():
    try:
        version_0 = module_0.Version()
        int_0 = None
        var_0 = version_0.__eq__(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        loose_version_0 = module_0.LooseVersion()
        tuple_0 = (loose_version_0,)
        version_0 = module_0.Version()
        var_0 = version_0.__lt__(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '1.0'
        str_1 = "1sZtBcg'&I$\\q\r[$/,oa"
        loose_version_0 = module_0.LooseVersion(str_1)
        strict_version_0 = module_0.StrictVersion(str_0)
        str_2 = ''
        var_0 = str(str_2)
        var_1 = str(strict_version_0)
        version_0 = module_0.Version()
        version_1 = module_0.Version()
        var_2 = version_1.__le__(version_0)
    except BaseException:
        pass

def test_case_5():
    try:
        version_0 = None
        version_1 = module_0.Version()
        var_0 = version_1.__gt__(version_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '1.2.3'
        strict_version_0 = module_0.StrictVersion(str_0)
        str_1 = '1.2a2'
        strict_version_1 = module_0.StrictVersion(str_1)
        str_2 = '1.2b2'
        strict_version_2 = module_0.StrictVersion(str_2)
        bool_0 = False
        version_0 = module_0.Version()
        var_0 = version_0.__ge__(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        strict_version_0 = module_0.StrictVersion()
        var_0 = strict_version_0.__str__()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = "1sZtBcg'&I$\\q\r[$/,oa"
        loose_version_0 = module_0.LooseVersion(str_0)
        var_0 = loose_version_0.__repr__()
        strict_version_0 = module_0.StrictVersion(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '1.2.3'
        strict_version_0 = module_0.StrictVersion(str_0)
        str_1 = '1.2b2'
        strict_version_1 = module_0.StrictVersion(str_1)
        str_2 = '  1.2b2'
        strict_version_2 = module_0.StrictVersion(str_2)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'O\x0cKDTM@<v'
        loose_version_0 = module_0.LooseVersion(str_0)
        var_0 = loose_version_0.__str__()
        var_1 = loose_version_0.__str__()
        str_1 = 'You must specify a collection name or a requirements file.'
        var_2 = loose_version_0.__gt__(loose_version_0)
        var_3 = loose_version_0.__gt__(str_1)
        version_0 = module_0.Version()
        var_4 = version_0.__repr__()
    except BaseException:
        pass