# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.human_to_bytes(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '03w]\n`JN]s'
        var_0 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1M'
        int_0 = 1
        var_0 = module_0.human_to_bytes(int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 2419.3
        list_0 = [float_0, float_0]
        var_0 = module_0.bytes_to_human(list_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        var_0 = module_0.lenient_lowercase(list_0)
        int_0 = 3794
        var_1 = module_0.bytes_to_human(int_0)
        int_1 = 25
        bytes_0 = b' \x1c\x0cs\xc5\xfaH\xef\xf1\xbb\rYT\xb0'
        var_2 = module_0.human_to_bytes(int_1, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '?C7U4t'
        set_0 = {str_0, str_0, str_0, str_0}
        str_1 = '4T#\rCf7sy('
        str_2 = "}Gjx&S$YV'c)'.,_Q\t"
        list_0 = []
        bytes_0 = b'j{ic\xca\xb0k\xd2m\\\xb3\xfa\xf3\x05\x1d\x8e\x9a\x0e$'
        tuple_0 = (list_0, bytes_0)
        var_0 = module_0.human_to_bytes(str_1, str_2, tuple_0)
        tuple_1 = (str_0, set_0)
        var_1 = module_0.bytes_to_human(tuple_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '1M'
        var_0 = module_0.human_to_bytes(str_0)
        int_0 = 1
        var_1 = module_0.human_to_bytes(int_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '2Epi4>&9EG <&U;gc'
        var_0 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '52bvxVs"\'\nmZ\x0bI70e^:'
        float_0 = 1314.8
        var_0 = module_0.bytes_to_human(float_0, str_0)
        var_1 = module_0.lenient_lowercase(str_0)
        var_2 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass