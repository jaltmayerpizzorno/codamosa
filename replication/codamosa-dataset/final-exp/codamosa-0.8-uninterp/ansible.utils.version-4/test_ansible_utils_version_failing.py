# Automatically generated by Pynguin.
import ansible.utils.version as module_0
import ansible.module_utils.compat.version as module_1

def test_case_0():
    try:
        str_0 = '\t0]JE,\x0c=dU-$N\n_v]=Ob'
        bytes_0 = b''
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        str_1 = '|0u$Q0h'
        tuple_0 = (set_0, str_1)
        alpha_0 = module_0._Alpha(tuple_0)
        var_0 = alpha_0.__ne__(str_0)
        str_2 = '2.0.0-pre.1'
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.parse(str_2)
        var_2 = semantic_version_0.__gt__(semantic_version_0)
        int_0 = None
        var_3 = semantic_version_0.__ge__(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        int_0 = 32603
        alpha_0 = module_0._Alpha(int_0)
        var_0 = alpha_0.__le__(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        float_0 = -1063.8
        numeric_0 = module_0._Numeric(float_0)
        var_0 = numeric_0.__ne__(tuple_0)
        bytes_0 = b''
        bool_0 = False
        var_1 = numeric_0.__eq__(bool_0)
        alpha_0 = module_0._Alpha(var_0)
        var_2 = alpha_0.__ne__(bytes_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_3 = alpha_0.__gt__(alpha_0)
        var_4 = semantic_version_0.__le__(semantic_version_0)
        bool_1 = False
        var_5 = numeric_0.__gt__(bool_1)
        var_6 = numeric_0.__repr__()
        var_7 = alpha_0.__le__(numeric_0)
        str_0 = 'N\x0c)k.D '
        loose_version_0 = module_1.LooseVersion(str_0)
        var_8 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_3():
    try:
        semantic_version_0 = None
        numeric_0 = module_0._Numeric(semantic_version_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 0.001
        numeric_0 = module_0._Numeric(float_0)
        str_0 = 'was not defined'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__lt__(str_0)
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
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = None
        var_0 = semantic_version_0.from_loose_version(alpha_0)
    except BaseException:
        pass

def test_case_7():
    try:
        complex_0 = None
        alpha_0 = module_0._Alpha(complex_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__le__(alpha_0)
    except BaseException:
        pass

def test_case_8():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__ne__(alpha_0)
        bool_0 = True
        var_1 = semantic_version_0.__ge__(bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__ne__(alpha_0)
        semantic_version_1 = module_0.SemanticVersion()
        str_0 = '4SQhR|mF9'
        var_1 = alpha_0.__ge__(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        alpha_0 = module_0._Alpha(semantic_version_0)
        semantic_version_1 = module_0.SemanticVersion()
        str_0 = '--become-password-file'
        var_0 = alpha_0.__lt__(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = 0.001
        numeric_0 = module_0._Numeric(float_0)
        str_0 = 'was not defined'
        bool_0 = False
        var_0 = numeric_0.__le__(bool_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.__lt__(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '2.0.0-pre.1'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.parse(str_0)
        var_1 = semantic_version_0.__gt__(semantic_version_0)
        loose_version_0 = module_1.LooseVersion()
        int_0 = 963
        numeric_0 = module_0._Numeric(int_0)
        var_2 = numeric_0.__eq__(semantic_version_0)
        var_3 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 4994
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__le__(semantic_version_0)
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        var_1 = numeric_0.__lt__(int_0)
        semantic_version_1 = module_0.SemanticVersion()
        var_2 = numeric_0.__lt__(semantic_version_1)
    except BaseException:
        pass

def test_case_14():
    try:
        tuple_0 = ()
        float_0 = 1331.13
        numeric_0 = module_0._Numeric(float_0)
        var_0 = numeric_0.__ne__(tuple_0)
        int_0 = 4994
        alpha_0 = module_0._Alpha(int_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = alpha_0.__gt__(alpha_0)
        loose_version_0 = module_1.LooseVersion()
        var_2 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_15():
    try:
        tuple_0 = ()
        float_0 = -1063.8
        numeric_0 = module_0._Numeric(float_0)
        var_0 = numeric_0.__ne__(tuple_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.__le__(semantic_version_0)
        bool_0 = False
        var_2 = numeric_0.__gt__(bool_0)
        str_0 = 'N\x0c))k.D '
        loose_version_0 = module_1.LooseVersion(str_0)
        var_3 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 4994
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__le__(semantic_version_0)
        complex_0 = None
        semantic_version_1 = module_0.SemanticVersion(complex_0)
        numeric_0 = module_0._Numeric(int_0)
        bool_0 = False
        var_1 = numeric_0.__gt__(bool_0)
        numeric_1 = module_0._Numeric(bool_0)
        var_2 = numeric_1.__lt__(numeric_0)
        loose_version_0 = module_1.LooseVersion()
        var_3 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '1.2.3-alpha.1.2+build.1.2'
        semantic_version_0 = module_0.SemanticVersion(str_0)
        str_1 = 'alpha'
        alpha_0 = module_0._Alpha(str_1)
        str_2 = '1'
        numeric_0 = module_0._Numeric(str_2)
        str_3 = '2'
        int_0 = 5000
        var_0 = numeric_0.__ge__(int_0)
        numeric_1 = module_0._Numeric(str_3)
        str_4 = 'build'
        alpha_1 = module_0._Alpha(str_4)
        numeric_2 = module_0._Numeric(str_2)
        numeric_3 = module_0._Numeric(str_3)
        str_5 = '1.2.3'
        semantic_version_1 = module_0.SemanticVersion(str_5)
        int_1 = -3108
        var_1 = semantic_version_1.__eq__(int_1)
    except BaseException:
        pass

def test_case_18():
    try:
        tuple_0 = ()
        float_0 = 1331.13
        numeric_0 = module_0._Numeric(float_0)
        var_0 = numeric_0.__ne__(tuple_0)
        bytes_0 = b'B\xcb\xcb\xafc!&\xe3\xedY\xad\xe9'
        int_0 = 4994
        alpha_0 = module_0._Alpha(int_0)
        var_1 = alpha_0.__ne__(bytes_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_2 = alpha_0.__gt__(alpha_0)
        var_3 = semantic_version_0.__le__(semantic_version_0)
        var_4 = numeric_0.__lt__(alpha_0)
        complex_0 = None
        semantic_version_1 = module_0.SemanticVersion(complex_0)
        var_5 = semantic_version_0.from_loose_version(numeric_0)
    except BaseException:
        pass

def test_case_19():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        loose_version_0 = module_1.LooseVersion()
        var_0 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_20():
    try:
        bool_0 = True
        str_0 = 'Y-'
        alpha_0 = module_0._Alpha(str_0)
        alpha_1 = module_0._Alpha(alpha_0)
        var_0 = alpha_1.__ne__(bool_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.__repr__()
        str_1 = '~yDY'
        var_2 = alpha_0.__gt__(str_1)
        bytes_0 = b'\xd0M\x9b^\xdf^\xf0\xee\xf3\x0c\xa42\x91.R'
        var_3 = alpha_1.__ge__(bytes_0)
    except BaseException:
        pass

def test_case_21():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__le__(semantic_version_0)
        str_0 = 'N\x0c))k.D '
        loose_version_0 = module_1.LooseVersion(str_0)
        var_1 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '1.2.3+testing'
        semantic_version_0 = module_0.SemanticVersion(str_0)
        loose_version_0 = module_1.LooseVersion(str_0)
        str_1 = '1.2.3-testing+testing'
        loose_version_1 = module_1.LooseVersion(str_1)
        loose_version_2 = module_1.LooseVersion(str_1)
        str_2 = '1.2.3.dev-testing+testing'
        loose_version_3 = module_1.LooseVersion(str_2)
        var_0 = semantic_version_0.parse(semantic_version_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '2.0.0-re.1'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__gt__(semantic_version_0)
        var_1 = semantic_version_0.__ge__(str_0)
    except BaseException:
        pass

def test_case_24():
    try:
        tuple_0 = ()
        float_0 = 1331.13
        numeric_0 = module_0._Numeric(float_0)
        var_0 = numeric_0.__ne__(tuple_0)
        complex_0 = None
        semantic_version_0 = module_0.SemanticVersion(complex_0)
        var_1 = semantic_version_0.__lt__(semantic_version_0)
        bool_0 = False
        var_2 = numeric_0.__gt__(bool_0)
        str_0 = 'o?Ue--.y-u?c>9J0s?'
        loose_version_0 = module_1.LooseVersion(str_0)
        var_3 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass