# Automatically generated by Pynguin.
import ansible.module_utils.compat.version as module_0

def test_case_0():
    pass

def test_case_1():
    strict_version_0 = module_0.StrictVersion()

def test_case_2():
    str_0 = '1.2.3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0.__le__(strict_version_0)

def test_case_3():
    float_0 = -2082.238
    strict_version_0 = module_0.StrictVersion()
    var_0 = strict_version_0.__le__(float_0)

def test_case_4():
    str_0 = '0.0.1a1.post1'
    loose_version_0 = module_0.LooseVersion(str_0)
    str_1 = '1.1a1'
    loose_version_1 = module_0.LooseVersion(str_1)
    var_0 = loose_version_1 > loose_version_0

def test_case_5():
    loose_version_0 = module_0.LooseVersion()

def test_case_6():
    str_0 = "\n(N>D1.=.A0$y\x0ch3fet'"
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_7():
    strict_version_0 = module_0.StrictVersion()
    str_0 = '1.2a3'
    var_0 = strict_version_0.parse(str_0)
    var_1 = strict_version_0.__le__(strict_version_0)

def test_case_8():
    str_0 = '1.2.3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0.__le__(strict_version_0)
    var_1 = str(str_0)
    var_2 = str(strict_version_0)

def test_case_9():
    strict_version_0 = module_0.StrictVersion()
    str_0 = '1.2a3'
    var_0 = strict_version_0.parse(str_0)
    var_1 = strict_version_0.__le__(strict_version_0)
    var_2 = str(strict_version_0)

def test_case_10():
    str_0 = '1.2.3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0.__le__(str_0)

def test_case_11():
    var_0 = None
    str_0 = '1.1a1'
    loose_version_0 = module_0.LooseVersion(str_0)
    str_1 = '2.0.0'
    loose_version_1 = module_0.LooseVersion(str_1)
    var_1 = loose_version_0 > loose_version_1
    loose_version_2 = module_0.LooseVersion(var_0)

def test_case_12():
    str_0 = '1.2.3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = str(strict_version_0)
    str_1 = '1.2.0'
    strict_version_1 = module_0.StrictVersion(str_1)
    var_1 = str(strict_version_1)
    var_2 = strict_version_1.__le__(strict_version_0)
    strict_version_2 = module_0.StrictVersion(str_1)
    var_3 = str(strict_version_1)

def test_case_13():
    str_0 = '1.2.3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = str(strict_version_0)
    str_1 = '2.0'
    strict_version_1 = module_0.StrictVersion(str_1)
    var_1 = str(var_0)
    var_2 = strict_version_1.__le__(strict_version_0)
    strict_version_2 = module_0.StrictVersion(str_1)

def test_case_14():
    strict_version_0 = module_0.StrictVersion()
    str_0 = '1.2.0'
    var_0 = strict_version_0.parse(str_0)
    var_1 = str(strict_version_0)
    str_1 = '1.2a3'
    var_2 = strict_version_0.parse(str_1)
    var_3 = str(strict_version_0)
    var_4 = strict_version_0.__le__(strict_version_0)
    var_5 = strict_version_0.__le__(str_0)
    str_2 = 'V++hXkf_;^S;$'
    loose_version_0 = module_0.LooseVersion(str_2)

def test_case_15():
    strict_version_0 = module_0.StrictVersion()
    str_0 = '1.2.0'
    var_0 = strict_version_0.parse(str_0)
    str_1 = '1.2a3'
    var_1 = strict_version_0.__le__(str_1)