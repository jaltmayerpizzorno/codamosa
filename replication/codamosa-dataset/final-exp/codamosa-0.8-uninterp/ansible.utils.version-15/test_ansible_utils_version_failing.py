# Automatically generated by Pynguin.
import ansible.utils.version as module_0
import ansible.module_utils.compat.version as module_1

def test_case_0():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        str_0 = 'HsFa@X1Y8'
        bytes_0 = b'0V\x9c\xbd\x97\xc9\x9c\xc1w'
        alpha_0 = module_0._Alpha(bytes_0)
        var_0 = alpha_0.__ne__(str_0)
        str_1 = 'RG|{4k|\\P\x0c&L'
        alpha_1 = module_0._Alpha(str_1)
        int_0 = -1124
        var_1 = alpha_1.__lt__(alpha_1)
        semantic_version_1 = module_0.SemanticVersion(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1365
        bool_0 = True
        alpha_0 = module_0._Alpha(bool_0)
        var_0 = alpha_0.__lt__(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        set_0 = {bool_0}
        int_0 = 0
        alpha_0 = module_0._Alpha(int_0)
        var_0 = alpha_0.__gt__(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x9c'
        int_0 = 757
        int_1 = 3032
        numeric_0 = module_0._Numeric(int_1)
        var_0 = numeric_0.__repr__()
        alpha_0 = module_0._Alpha(int_0)
        var_1 = alpha_0.__gt__(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -4895.91256
        int_0 = 525
        numeric_0 = module_0._Numeric(int_0)
        var_0 = numeric_0.__ge__(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.from_loose_version(semantic_version_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '>jZ3c'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__gt__(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = set()
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.parse(set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        complex_0 = None
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__ne__(complex_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -1671
        semantic_version_0 = module_0.SemanticVersion()
        semantic_version_1 = module_0.SemanticVersion()
        var_0 = semantic_version_1.__lt__(semantic_version_0)
        numeric_0 = module_0._Numeric(int_0)
        float_0 = -916.1932
        var_1 = numeric_0.__lt__(float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        list_0 = []
        int_0 = 133
        alpha_0 = module_0._Alpha(int_0)
        alpha_1 = module_0._Alpha(alpha_0)
        var_0 = alpha_1.__eq__(list_0)
        bool_0 = True
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.__le__(bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        semantic_version_0 = None
        str_0 = 'e\x0c0s1xs7V1/WM u^gQ'
        alpha_0 = module_0._Alpha(str_0)
        alpha_1 = module_0._Alpha(alpha_0)
        var_0 = alpha_1.__ne__(semantic_version_0)
        var_1 = semantic_version_0.__repr__()
        semantic_version_1 = module_0.SemanticVersion()
        bool_0 = False
        var_2 = semantic_version_1.__ge__(bool_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = -1671
        semantic_version_0 = module_0.SemanticVersion()
        semantic_version_1 = module_0.SemanticVersion()
        numeric_0 = module_0._Numeric(int_0)
        float_0 = -916.1932
        dict_0 = {}
        var_0 = numeric_0.__eq__(dict_0)
        var_1 = numeric_0.__lt__(float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        str_0 = ''
        var_0 = numeric_0.__le__(numeric_0)
        alpha_0 = module_0._Alpha(str_0)
        int_0 = 3296
        var_1 = alpha_0.__gt__(alpha_0)
        var_2 = numeric_0.__ge__(int_0)
        var_3 = alpha_0.__repr__()
        var_4 = numeric_0.__ge__(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        numeric_0 = None
        bool_0 = False
        numeric_1 = module_0._Numeric(bool_0)
        var_0 = numeric_1.__gt__(numeric_0)
    except BaseException:
        pass

def test_case_15():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__ne__(alpha_0)
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        str_0 = ''
        var_1 = numeric_0.__le__(alpha_0)
        alpha_1 = module_0._Alpha(str_0)
        int_0 = 3296
        var_2 = numeric_0.__ge__(int_0)
        dict_0 = {}
        alpha_2 = module_0._Alpha(dict_0)
        float_0 = 512.0
        alpha_3 = module_0._Alpha(float_0)
        set_0 = {var_0, float_0}
        var_3 = alpha_2.__ge__(set_0)
    except BaseException:
        pass

def test_case_16():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__ne__(alpha_0)
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        str_0 = ''
        var_1 = numeric_0.__le__(numeric_0)
        alpha_1 = module_0._Alpha(str_0)
        var_2 = alpha_1.__ge__(str_0)
        int_0 = 3296
        var_3 = alpha_0.__gt__(alpha_0)
        var_4 = numeric_0.__ge__(int_0)
        dict_0 = {}
        alpha_2 = module_0._Alpha(numeric_0)
        float_0 = 512.0
        alpha_3 = module_0._Alpha(float_0)
        var_5 = alpha_0.__ne__(dict_0)
        var_6 = semantic_version_0.from_loose_version(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        loose_version_0 = module_1.LooseVersion()
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_18():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__ne__(alpha_0)
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        str_0 = ''
        var_1 = numeric_0.__le__(numeric_0)
        var_2 = alpha_0.__repr__()
        alpha_1 = module_0._Alpha(str_0)
        int_0 = 3296
        var_3 = alpha_1.__gt__(var_2)
        var_4 = numeric_0.__ge__(int_0)
        dict_0 = {}
        alpha_2 = module_0._Alpha(var_0)
        float_0 = 512.0
        alpha_3 = module_0._Alpha(float_0)
        var_5 = alpha_0.__ne__(dict_0)
        set_0 = {var_0, float_0}
        semantic_version_1 = module_0.SemanticVersion()
        var_6 = semantic_version_1.from_loose_version(set_0)
    except BaseException:
        pass