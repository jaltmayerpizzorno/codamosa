# Automatically generated by Pynguin.
import ansible.utils.version as module_0
import ansible.module_utils.compat.version as module_1

def test_case_0():
    try:
        bool_0 = True
        alpha_0 = module_0._Alpha(bool_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.from_loose_version(alpha_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '4.5.0b1'
        loose_version_0 = module_1.LooseVersion(str_0)
        str_1 = '4.5.0-b1'
        semantic_version_0 = module_0.SemanticVersion(str_1)
        alpha_0 = module_0._Alpha(semantic_version_0)
        var_0 = alpha_0.__gt__(str_1)
        semantic_version_1 = module_0.SemanticVersion()
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0]
        str_0 = '9;z*JQ75#'
        alpha_0 = module_0._Alpha(str_0)
        var_0 = alpha_0.__lt__(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__eq__(semantic_version_0)
        bool_0 = None
        bytes_0 = b'\xb7O0\x82\x9e\x15=\xb2\x80\x85q\x89\xe9'
        alpha_0 = module_0._Alpha(bytes_0)
        var_1 = alpha_0.__eq__(bool_0)
        str_0 = '\n        Publishes a collection to a Galaxy server and returns the import task URI.\n\n        :param collection_path: The path to the collection tarball to publish.\n        :return: The import task URI that contains the import results.\n        '
        var_2 = alpha_0.__gt__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Q\\V~}]\t>4'
        str_1 = 'jYq\x0cT.Y4'
        alpha_0 = module_0._Alpha(str_1)
        var_0 = alpha_0.__ge__(str_0)
        var_1 = alpha_0.__repr__()
        semantic_version_0 = module_0.SemanticVersion()
        var_2 = semantic_version_0.parse(alpha_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        var_0 = numeric_0.__repr__()
        str_0 = 'Tc{M?'
        semantic_version_0 = module_0.SemanticVersion()
        var_1 = semantic_version_0.__eq__(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'nogroup'
        bool_0 = True
        numeric_0 = module_0._Numeric(bool_0)
        var_0 = numeric_0.__lt__(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        semantic_version_1 = module_0.SemanticVersion()
        var_0 = semantic_version_1.__eq__(semantic_version_0)
        float_0 = 2824.27027
        int_0 = -247
        numeric_0 = module_0._Numeric(int_0)
        var_1 = numeric_0.__gt__(float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '(~b5~O+yn73o7'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.parse(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'Tc{M?'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__eq__(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = "8y'v|/:~:3@\n"
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__le__(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__lt__(semantic_version_0)
        semantic_version_1 = module_0.SemanticVersion()
        str_0 = '*4gy:,['
        var_1 = semantic_version_1.__gt__(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        int_0 = 3226
        var_0 = semantic_version_0.__ge__(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'form_factor'
        str_1 = 'jYq\x0cT.Y4'
        alpha_0 = module_0._Alpha(str_1)
        var_0 = alpha_0.__ge__(str_0)
        var_1 = alpha_0.__repr__()
        bytes_0 = b'Q\x17U\xb7&?\xff\x1e\xb2\xa7\x94\x04\x17'
        alpha_1 = module_0._Alpha(bytes_0)
        int_0 = 99
        int_1 = -2056
        numeric_0 = module_0._Numeric(int_1)
        var_2 = numeric_0.__le__(int_0)
        semantic_version_0 = module_0.SemanticVersion()
        var_3 = semantic_version_0.parse(alpha_1)
    except BaseException:
        pass

def test_case_14():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__repr__()
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = 124.316349
        numeric_0 = module_0._Numeric(float_0)
        str_0 = 'Y\t(p~\\n'
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.from_loose_version(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bool_0 = True
        numeric_0 = module_0._Numeric(bool_0)
        str_0 = 'k"L/(OQ(d5wJ-\x0b:S9l'
        alpha_0 = module_0._Alpha(str_0)
        var_0 = alpha_0.__lt__(numeric_0)
        bytes_0 = b'\xc0\xe4\xab\xe6M\xbb\xe6'
        alpha_1 = module_0._Alpha(bytes_0)
        str_1 = 'g9jJKlU+Q@W>69La'
        numeric_1 = module_0._Numeric(str_1)
    except BaseException:
        pass

def test_case_17():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        str_0 = 'wg\r(y'
        var_0 = semantic_version_0.__ne__(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        bool_0 = False
        numeric_0 = module_0._Numeric(bool_0)
        alpha_0 = module_0._Alpha(numeric_0)
        alpha_1 = module_0._Alpha(alpha_0)
        bool_1 = True
        alpha_2 = module_0._Alpha(bool_1)
        alpha_3 = module_0._Alpha(alpha_2)
        var_0 = alpha_3.__le__(alpha_1)
        int_0 = None
        alpha_4 = module_0._Alpha(int_0)
        set_0 = set()
        alpha_5 = module_0._Alpha(set_0)
        var_1 = alpha_5.__ne__(alpha_4)
        str_0 = '2("dQ4D\\e\x0b*e@ \tu'
        numeric_1 = module_0._Numeric(str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        semantic_version_1 = module_0.SemanticVersion()
        var_0 = semantic_version_1.__eq__(semantic_version_0)
        bytes_0 = b'\xb7O0\x82\x9e\x15=\xb2\x80\x85q\x89\xe9'
        var_1 = semantic_version_1.__repr__()
        float_0 = 902.8957
        alpha_0 = module_0._Alpha(bytes_0)
        int_0 = 2403
        numeric_0 = module_0._Numeric(float_0)
        var_2 = numeric_0.__lt__(int_0)
        var_3 = numeric_0.__ge__(float_0)
    except BaseException:
        pass

def test_case_20():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__lt__(semantic_version_0)
        semantic_version_1 = module_0.SemanticVersion()
        var_1 = semantic_version_1.__eq__(semantic_version_0)
        bytes_0 = b'\xeaO\xc3\x99E\x94\x8a\xb2SEFm\x12\xf2\n'
        float_0 = 902.8957
        alpha_0 = module_0._Alpha(bytes_0)
        numeric_0 = module_0._Numeric(float_0)
        var_2 = numeric_0.__le__(alpha_0)
        var_3 = numeric_0.__ne__(numeric_0)
        tuple_0 = ()
        var_4 = semantic_version_0.from_loose_version(tuple_0)
    except BaseException:
        pass

def test_case_21():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        semantic_version_1 = module_0.SemanticVersion()
        var_0 = semantic_version_1.__eq__(semantic_version_0)
        bytes_0 = b'\xb7O0\x82\x9e\x15=\xb2\x80\x85q\x89\xe9'
        float_0 = 902.8957
        alpha_0 = module_0._Alpha(bytes_0)
        int_0 = 2403
        numeric_0 = module_0._Numeric(float_0)
        var_1 = numeric_0.__le__(alpha_0)
        var_2 = numeric_0.__lt__(int_0)
        var_3 = alpha_0.__le__(alpha_0)
        tuple_0 = ()
        var_4 = semantic_version_0.from_loose_version(tuple_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '1.2.3'
        alpha_0 = module_0._Alpha(str_0)
        alpha_1 = module_0._Alpha(str_0)
        alpha_2 = module_0._Alpha(str_0)
        str_1 = '1.2.4'
        alpha_3 = module_0._Alpha(str_1)
        var_0 = alpha_2 <= alpha_3
        alpha_4 = module_0._Alpha(str_1)
        alpha_5 = module_0._Alpha(str_1)
        alpha_6 = module_0._Alpha(str_1)
        alpha_7 = module_0._Alpha(str_0)
        var_1 = alpha_6 <= alpha_7
        alpha_8 = module_0._Alpha(str_0)
        alpha_9 = module_0._Alpha(str_0)
        var_2 = alpha_9 <= str_1
        alpha_10 = module_0._Alpha(str_0)
        numeric_0 = module_0._Numeric(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        var_0 = semantic_version_0.__lt__(semantic_version_0)
        semantic_version_1 = module_0.SemanticVersion()
        loose_version_0 = module_1.LooseVersion()
        var_1 = semantic_version_1.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_24():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        semantic_version_1 = module_0.SemanticVersion()
        var_0 = semantic_version_1.__eq__(semantic_version_0)
        str_0 = '<=KQ(%Ui-v;'
        loose_version_0 = module_1.LooseVersion(str_0)
        var_1 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_25():
    try:
        semantic_version_0 = module_0.SemanticVersion()
        semantic_version_1 = module_0.SemanticVersion()
        var_0 = semantic_version_1.__eq__(semantic_version_0)
        bytes_0 = b'\xb7O0\x82\x15=\xb2\x80\x85\xa5\x89'
        float_0 = 902.8957
        alpha_0 = module_0._Alpha(bytes_0)
        numeric_0 = module_0._Numeric(float_0)
        var_1 = numeric_0.__le__(alpha_0)
        var_2 = numeric_0.__repr__()
        str_0 = '<=KQi(%Ui-v;'
        var_3 = numeric_0.__eq__(str_0)
        var_4 = alpha_0.__le__(alpha_0)
        loose_version_0 = module_1.LooseVersion(str_0)
        var_5 = semantic_version_0.from_loose_version(loose_version_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = '4.4.0'
        loose_version_0 = module_1.LooseVersion(str_0)
        semantic_version_0 = module_0.SemanticVersion()
        loose_version_1 = module_1.LooseVersion()
        var_0 = semantic_version_0.from_loose_version(loose_version_0)
        float_0 = None
        var_1 = semantic_version_0.from_loose_version(float_0)
    except BaseException:
        pass