# Automatically generated by Pynguin.
import ansible.module_utils.compat.version as module_0

def test_case_0():
    version_0 = module_0.Version()

def test_case_1():
    str_0 = '1.2.3'
    strict_version_0 = module_0.StrictVersion(str_0)

def test_case_2():
    str_0 = '1.2.3'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = strict_version_0.__str__()

def test_case_3():
    loose_version_0 = module_0.LooseVersion()

def test_case_4():
    str_0 = 'aQA[D+m0iG'
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_5():
    str_0 = '1.5.2b2'
    loose_version_0 = module_0.LooseVersion(str_0)

def test_case_6():
    str_0 = '1.0'
    strict_version_0 = module_0.StrictVersion(str_0)

def test_case_7():
    str_0 = '1.0'
    strict_version_0 = module_0.StrictVersion(str_0)
    var_0 = str(strict_version_0)