# Automatically generated by Pynguin.
import ansible.module_utils.compat.version as module_0

def test_case_0():
    pass

def test_case_1():
    strict_version_0 = module_0.StrictVersion()

def test_case_2():
    str_0 = '0.5b3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == str_0

def test_case_3():
    str_0 = '0.4.0'
    strict_version_0 = module_0.StrictVersion(str_0)
    loose_version_0 = module_0.LooseVersion(str_0)
    var_0 = strict_version_0.__str__()
    var_1 = var_0 == loose_version_0

def test_case_4():
    loose_version_0 = module_0.LooseVersion()

def test_case_5():
    str_0 = '5.u~[|}B!mO&2Hv3v'
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_6():
    str_0 = '0.4.1'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == str_0

def test_case_7():
    str_0 = '0.53'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == strict_version_0

def test_case_8():
    str_0 = '0.4.1'
    strict_version_0 = module_0.StrictVersion(str_0)
    strict_version_1 = module_0.StrictVersion(str_0)
    var_0 = strict_version_1.__str__()
    var_1 = strict_version_1 == str_0

def test_case_9():
    str_0 = '0.5b3'
    strict_version_0 = module_0.StrictVersion(str_0)
    str_1 = '+mtN<?-,\r%RGO8+'
    var_0 = strict_version_0.__str__()
    loose_version_0 = module_0.LooseVersion(str_1)
    var_1 = loose_version_0.__repr__()
    var_2 = strict_version_0 == str_0

def test_case_10():
    str_0 = '1.0'
    str_1 = '0.9'
    strict_version_0 = module_0.StrictVersion(str_1)
    var_0 = str_0 > strict_version_0
    var_1 = type(var_0)
    strict_version_1 = module_0.StrictVersion(str_1)
    var_2 = strict_version_1 > strict_version_1
    strict_version_2 = module_0.StrictVersion(str_1)
    var_3 = type(strict_version_1)

def test_case_11():
    str_0 = '0.5b3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == strict_version_0

def test_case_12():
    str_0 = '0.5b3'
    strict_version_0 = module_0.StrictVersion(str_0)
    str_1 = '+mtN<?-,\r%RGO8+'
    loose_version_0 = module_0.LooseVersion(str_1)
    var_0 = loose_version_0.__repr__()
    var_1 = strict_version_0 == loose_version_0
    var_2 = loose_version_0.__str__()

def test_case_13():
    str_0 = '0.4.0'
    strict_version_0 = module_0.StrictVersion(str_0)
    loose_version_0 = module_0.LooseVersion(str_0)
    var_0 = str_0 == loose_version_0
    var_1 = strict_version_0.__str__()
    var_2 = strict_version_0.__str__()
    var_3 = var_2 == loose_version_0

def test_case_14():
    str_0 = '0.4.0'
    var_0 = str_0 == str_0
    strict_version_0 = module_0.StrictVersion(str_0)
    strict_version_1 = module_0.StrictVersion(str_0)
    loose_version_0 = module_0.LooseVersion(str_0)
    var_1 = strict_version_0 == loose_version_0
    var_2 = strict_version_1.__str__()
    var_3 = loose_version_0.__str__()
    strict_version_2 = module_0.StrictVersion(str_0)
    var_4 = strict_version_2 == strict_version_2
    var_5 = strict_version_2.__str__()
    var_6 = loose_version_0 == loose_version_0

def test_case_15():
    str_0 = '0.9'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = type(strict_version_0)
    var_1 = strict_version_0 > strict_version_0
    var_2 = type(var_1)
    strict_version_1 = module_0.StrictVersion(str_0)

def test_case_16():
    str_0 = '0.4.1'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0 == str_0
    str_1 = '0.5b3'
    set_0 = None
    var_1 = strict_version_0.__le__(set_0)
    strict_version_1 = module_0.StrictVersion(str_1)
    var_2 = strict_version_1 == str_1
    str_2 = 'E'
    loose_version_0 = module_0.LooseVersion(str_2)