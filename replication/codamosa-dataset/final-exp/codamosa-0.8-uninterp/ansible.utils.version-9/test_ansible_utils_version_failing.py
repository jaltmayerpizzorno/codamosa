# Automatically generated by Pynguin.
import ansible.utils.version as module_0
import ansible.module_utils.compat.version as module_1

def test_case_0():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        tuple_0 = ()
        alpha_0 = module_0._Alpha(tuple_0)
        var_0 = semantic_version_0.from_loose_version(alpha_0)
    except BaseException:
        pass

def test_case_1():
    try:
        alpha_0 = None
        bool_0 = False
        alpha_1 = module_0._Alpha(bool_0)
        var_0 = alpha_1.__gt__(alpha_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        tuple_0 = (list_0,)
        bool_0 = True
        numeric_0 = module_0._Numeric(bool_0)
        var_0 = numeric_0.__le__(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Qtzmn^\x0b02BkvCK2!](f"'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__gt__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__eq__(str_0)
        float_0 = 1092.6158
        var_1 = semantic_version_0.__ne__(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '1.2.3-a4'
        semantic_version_0 = module_0.SemanticVersion(str_0)
        loose_version_0 = module_1.LooseVersion()
        int_0 = -984
        var_0 = semantic_version_0.__lt__(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__gt__(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -514
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.from_loose_version(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '2.0.0-alpha.12'
        loose_version_0 = module_1.LooseVersion(str_0)
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__ne__(semantic_version_0)
        var_1 = semantic_version_0.__le__(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        bytes_0 = b'\xab\xc3\x14\x83\xc7\xe7\xabm\xa4f\xa2 \xeaz'
        var_0 = semantic_version_0.__ge__(bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        float_0 = 1834.0
        numeric_0 = module_0._Numeric(float_0)
        bool_0 = True
        var_0 = numeric_0.__eq__(bool_0)
        var_1 = semantic_version_0.from_loose_version(semantic_version_0)
    except BaseException:
        pass

def test_case_11():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        float_0 = -1139.1309
        numeric_0 = module_0._Numeric(float_0)
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__ge__(numeric_0)
        var_1 = semantic_version_0.__repr__()
        var_2 = alpha_0.__gt__(numeric_0)
        str_0 = '{q lxn"{ sL-'
        var_3 = numeric_0.__ne__(str_0)
        var_4 = semantic_version_0.__le__(semantic_version_0)
        list_0 = [float_0, float_0]
        var_5 = numeric_0.__eq__(list_0)
        bool_0 = False
        alpha_1 = module_0._Alpha(bool_0)
        var_6 = alpha_1.__repr__()
        str_1 = ''
        var_7 = semantic_version_0.__eq__(str_1)
        str_2 = '--host'
        semantic_version_1 = module_0.SemanticVersion()
        var_8 = semantic_version_1.__eq__(str_2)
    except BaseException:
        pass

def test_case_12():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        float_0 = 0.2
        numeric_0 = module_0._Numeric(float_0)
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__gt__(numeric_0)
        var_1 = semantic_version_0.__le__(semantic_version_0)
        var_2 = numeric_0.__lt__(alpha_0)
        bool_0 = False
        alpha_1 = module_0._Alpha(bool_0)
        var_3 = alpha_1.__repr__()
        str_0 = ''
        var_4 = semantic_version_0.__eq__(str_0)
        var_5 = alpha_1.__repr__()
        str_1 = '--host'
        semantic_version_1 = module_0.SemanticVersion()
        var_6 = semantic_version_1.__eq__(str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        loose_version_0 = module_1.LooseVersion()
        var_0 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass