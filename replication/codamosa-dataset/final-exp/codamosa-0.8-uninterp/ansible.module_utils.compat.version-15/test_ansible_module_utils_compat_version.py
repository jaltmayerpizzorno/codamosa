# Automatically generated by Pynguin.
import ansible.module_utils.compat.version as module_0

def test_case_0():
    pass

def test_case_1():
    version_0 = module_0.Version()

def test_case_2():
    str_0 = '1.3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = str_0 == strict_version_0

def test_case_3():
    str_0 = '2.0'
    loose_version_0 = module_0.LooseVersion(str_0)
    var_0 = loose_version_0 < loose_version_0

def test_case_4():
    str_0 = '2.0'
    loose_version_0 = module_0.LooseVersion(str_0)
    var_0 = str_0 < loose_version_0

def test_case_5():
    strict_version_0 = module_0.StrictVersion()
    str_0 = '1.2b1'
    var_0 = strict_version_0.parse(str_0)
    var_1 = strict_version_0 >= strict_version_0

def test_case_6():
    str_0 = '1.2.4'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = str(strict_version_0)
    var_1 = str(strict_version_0)

def test_case_7():
    loose_version_0 = module_0.LooseVersion()

def test_case_8():
    str_0 = 'base_class'
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_9():
    str_0 = '1.2b1'
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_10():
    str_0 = '1.2.0'
    loose_version_0 = module_0.LooseVersion(str_0)
    str_1 = '1.2'
    loose_version_1 = module_0.LooseVersion(str_1)
    var_0 = loose_version_0 >= loose_version_1

def test_case_11():
    strict_version_0 = module_0.StrictVersion()
    str_0 = '1.2b1'
    var_0 = strict_version_0.parse(str_0)
    var_1 = str_0 >= strict_version_0

def test_case_12():
    str_0 = '1.0'
    loose_version_0 = module_0.LooseVersion(str_0)
    str_1 = '2.0'
    loose_version_1 = module_0.LooseVersion(str_0)
    var_0 = loose_version_0 < str_1
    loose_version_2 = module_0.LooseVersion(str_1)
    loose_version_3 = module_0.LooseVersion(str_0)
    var_1 = loose_version_2 < loose_version_3
    loose_version_4 = module_0.LooseVersion(str_0)
    var_2 = loose_version_4 < loose_version_4

def test_case_13():
    strict_version_0 = module_0.StrictVersion()
    str_0 = '1.2b1'
    var_0 = strict_version_0.parse(str_0)
    var_1 = strict_version_0.__str__()
    loose_version_0 = module_0.LooseVersion(str_0)
    var_2 = strict_version_0 >= strict_version_0

def test_case_14():
    str_0 = '1.2.4'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = str(strict_version_0)
    str_1 = '1.2.4a1'
    strict_version_1 = module_0.StrictVersion(str_1)
    var_1 = str(strict_version_1)

def test_case_15():
    str_0 = '1.2'
    strict_version_0 = module_0.StrictVersion(str_0)
    strict_version_1 = module_0.StrictVersion(str_0)
    strict_version_2 = module_0.StrictVersion(str_0)
    str_1 = '1.3'
    strict_version_3 = module_0.StrictVersion(str_1)
    var_0 = strict_version_2 == strict_version_3
    strict_version_4 = module_0.StrictVersion(str_0)
    var_1 = strict_version_4 == str_0

def test_case_16():
    str_0 = '1.2'
    strict_version_0 = module_0.StrictVersion(str_0)
    strict_version_1 = module_0.StrictVersion(str_0)
    str_1 = '1.3'
    strict_version_2 = module_0.StrictVersion(str_1)
    var_0 = str_0 == strict_version_2
    var_1 = strict_version_1 == str_0