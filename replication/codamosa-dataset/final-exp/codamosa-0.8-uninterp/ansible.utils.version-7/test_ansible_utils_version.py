# Automatically generated by Pynguin.
import ansible.utils.version as module_0
import ansible.module_utils.compat.version as module_1

def test_case_0():
    pass

def test_case_1():
    semantic_version_0 = module_0.SemanticVersion()
    var_0 = semantic_version_0.__gt__(semantic_version_0)
    semantic_version_1 = module_0.SemanticVersion()
    float_0 = 416.652
    alpha_0 = module_0._Alpha(float_0)

def test_case_2():
    semantic_version_0 = module_0.SemanticVersion()
    semantic_version_1 = module_0.SemanticVersion()
    var_0 = semantic_version_1.__gt__(semantic_version_0)
    semantic_version_2 = module_0.SemanticVersion()
    float_0 = 416.652
    alpha_0 = module_0._Alpha(float_0)
    str_0 = 'import_playbook statRments must specify the file name to import'
    var_1 = semantic_version_2.__repr__()
    alpha_1 = module_0._Alpha(str_0)
    int_0 = 677
    var_2 = alpha_0.__eq__(int_0)

def test_case_3():
    str_0 = 'L9'
    alpha_0 = module_0._Alpha(str_0)
    str_1 = '"z\'}Vl~5$FdTRKC|Enkm'
    alpha_1 = module_0._Alpha(str_1)
    var_0 = alpha_1.__gt__(alpha_0)

def test_case_4():
    int_0 = -962
    numeric_0 = module_0._Numeric(int_0)
    var_0 = numeric_0.__repr__()

def test_case_5():
    semantic_version_0 = module_0.SemanticVersion()

def test_case_6():
    semantic_version_0 = module_0.SemanticVersion()
    semantic_version_1 = module_0.SemanticVersion()
    var_0 = semantic_version_1.__ne__(semantic_version_0)

def test_case_7():
    semantic_version_0 = module_0.SemanticVersion()
    semantic_version_1 = module_0.SemanticVersion()
    var_0 = semantic_version_1.__lt__(semantic_version_0)

def test_case_8():
    semantic_version_0 = module_0.SemanticVersion()
    var_0 = semantic_version_0.__gt__(semantic_version_0)
    semantic_version_1 = module_0.SemanticVersion()

def test_case_9():
    str_0 = '1.0.0'
    semantic_version_0 = module_0.SemanticVersion(str_0)

def test_case_10():
    str_0 = '1.2.3'
    loose_version_0 = module_1.LooseVersion(str_0)
    semantic_version_0 = module_0.SemanticVersion(str_0)
    loose_version_1 = module_1.LooseVersion(str_0)
    str_1 = '1.2.0'
    semantic_version_1 = module_0.SemanticVersion(str_1)
    str_2 = '1'
    loose_version_2 = module_1.LooseVersion(str_2)
    str_3 = '1.0.0'
    semantic_version_2 = module_0.SemanticVersion(str_3)
    str_4 = '1.2.3-rc1.dev4'
    loose_version_3 = module_1.LooseVersion(str_4)
    semantic_version_3 = module_0.SemanticVersion(str_4)
    str_5 = '1.2.3+rc1.dev4'
    loose_version_4 = module_1.LooseVersion(str_5)
    semantic_version_4 = module_0.SemanticVersion()

def test_case_11():
    str_0 = '1.2.3'
    loose_version_0 = module_1.LooseVersion(str_0)
    semantic_version_0 = module_0.SemanticVersion(str_0)
    str_1 = '1.2'
    loose_version_1 = module_1.LooseVersion(str_1)
    str_2 = '1.2.0'
    semantic_version_1 = module_0.SemanticVersion(str_2)
    str_3 = '1'
    loose_version_2 = module_1.LooseVersion(str_3)
    str_4 = '1.0.0'
    semantic_version_2 = module_0.SemanticVersion(str_4)
    str_5 = '1.2.3-rc1.dev4'
    semantic_version_3 = module_0.SemanticVersion(str_5)
    str_6 = '1.2.3+rc1.dev4'
    loose_version_3 = module_1.LooseVersion(str_6)
    semantic_version_4 = module_0.SemanticVersion(str_6)

def test_case_12():
    semantic_version_0 = module_0.SemanticVersion()
    str_0 = '1.0.0'
    semantic_version_1 = module_0.SemanticVersion()
    semantic_version_2 = module_0.SemanticVersion(str_0)
    str_1 = '0.1.0'
    semantic_version_3 = module_0.SemanticVersion(str_1)
    str_2 = '0.0.1'
    semantic_version_4 = module_0.SemanticVersion(str_2)
    str_3 = '0.0.1-alpha1.beta2.rc'
    semantic_version_5 = module_0.SemanticVersion(str_3)
    str_4 = '0.0.1+build.1234'
    semantic_version_6 = module_0.SemanticVersion(str_4)
    str_5 = '0.0.1-alpha1.beta2.rc+build.1234'
    semantic_version_7 = module_0.SemanticVersion(str_5)
    str_6 = '0.0.1-alpha.1'
    semantic_version_8 = module_0.SemanticVersion(str_6)