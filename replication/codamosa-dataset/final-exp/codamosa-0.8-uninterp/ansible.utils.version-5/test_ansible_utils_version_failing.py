# Automatically generated by Pynguin.
import ansible.utils.version as module_0
import ansible.module_utils.compat.version as module_1

def test_case_0():
    try:
        str_0 = 'FBp:|4AK(11$'
        int_0 = -2242
        numeric_0 = module_0._Numeric(int_0)
        alpha_0 = module_0._Alpha(numeric_0)
        var_0 = alpha_0.__le__(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        semantic_version_0 = module_0.SemanticVersion()
        bytes_0 = b'\x91L\xac\x90\t\xf3\xf9\x9e\x1e'
        alpha_0 = module_0._Alpha(bytes_0)
        int_0 = -462
        numeric_0 = module_0._Numeric(int_0)
        var_0 = alpha_0.__gt__(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        complex_0 = None
        numeric_0 = module_0._Numeric(complex_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xe9m4CV8'
        alpha_0 = module_0._Alpha(bytes_0)
        str_0 = 'l\x0c?:(\tLu@gI$Uq@DAA'
        bool_0 = True
        numeric_0 = module_0._Numeric(bool_0)
        alpha_1 = module_0._Alpha(numeric_0)
        var_0 = numeric_0.__ge__(alpha_1)
        var_1 = alpha_1.__le__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'lCdukmg kR0'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__le__(str_0)
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
        bool_0 = False
        set_0 = {bool_0, bool_0}
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__ne__(set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        bytes_0 = None
        var_0 = semantic_version_0.__lt__(bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        str_0 = '__init__'
        var_0 = semantic_version_0.__gt__(semantic_version_0)
        var_1 = semantic_version_0.__ge__(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        float_0 = -155.45603
        bool_0 = True
        numeric_0 = module_0._Numeric(bool_0)
        str_0 = ''
        alpha_0 = module_0._Alpha(str_0)
        var_0 = alpha_0.__ge__(numeric_0)
        var_1 = semantic_version_0.__le__(float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -3095.47
        numeric_0 = module_0._Numeric(float_0)
        var_0 = numeric_0.__eq__(numeric_0)
        str_0 = ''
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.__le__(semantic_version_0)
        var_2 = semantic_version_0.from_loose_version(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = -1698.6818
        complex_0 = None
        dict_0 = {float_0: float_0, complex_0: float_0, float_0: complex_0}
        float_1 = -3.11602
        numeric_0 = module_0._Numeric(float_1)
        var_0 = numeric_0.__le__(dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'cLt)\r){UL>qTn>L7Z`\r'
        set_0 = {str_0, str_0}
        float_0 = -3095.47
        numeric_0 = module_0._Numeric(float_0)
        var_0 = numeric_0.__ne__(set_0)
        bool_0 = False
        tuple_0 = (bool_0,)
        var_1 = numeric_0.__gt__(tuple_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = "Yd?W?LB\x0cq'tbFD"
        str_1 = '\nFsKu[\x0cS\x0b&vbfy\n6d}`'
        alpha_0 = module_0._Alpha(str_1)
        var_0 = alpha_0.__repr__()
        alpha_1 = module_0._Alpha(alpha_0)
        var_1 = alpha_0.__repr__()
        var_2 = alpha_1.__gt__(str_0)
        str_2 = 'fdZPx'
        alpha_2 = module_0._Alpha(str_2)
        float_0 = 1.5
        semantic_version_0 = module_0.SemanticVersion()
        var_3 = semantic_version_0.__ne__(float_0)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = -3095.4749138795883
        numeric_0 = module_0._Numeric(float_0)
        bool_0 = True
        bytes_0 = b'-\r~,'
        var_0 = numeric_0.__ge__(numeric_0)
        var_1 = numeric_0.__le__(bool_0)
        alpha_0 = module_0._Alpha(bytes_0)
        str_0 = ''
        semantic_version_0 = module_0.SemanticVersion()
        var_2 = semantic_version_0.__le__(semantic_version_0)
        semantic_version_1 = module_0.SemanticVersion()
        var_3 = semantic_version_0.from_loose_version(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = 883.3
        numeric_0 = module_0._Numeric(float_0)
        bool_0 = True
        bytes_0 = b'-\r~,'
        var_0 = numeric_0.__ge__(numeric_0)
        var_1 = numeric_0.__le__(bool_0)
        alpha_0 = module_0._Alpha(bytes_0)
        str_0 = ''
        semantic_version_0 = module_0.SemanticVersion()
        var_2 = semantic_version_0.__le__(semantic_version_0)
        semantic_version_1 = module_0.SemanticVersion()
        var_3 = semantic_version_0.from_loose_version(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        loose_version_0 = module_1.LooseVersion()
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass