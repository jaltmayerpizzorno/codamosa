# Automatically generated by Pynguin.
import pytutils.files as module_0

def test_case_0():
    try:
        str_0 = None
        int_0 = -1271
        var_0 = module_0.burp(str_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'I\'b{$W62"XOpW$tKrSSD'
        float_0 = None
        var_0 = module_0.burp(str_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'I\'b{$W62"OW$KSSD'
        float_0 = None
        dict_0 = {str_0: float_0}
        bytes_0 = b'\xab\xc1\xe1\x15\xbdT?\xfamh\xa4\x8e\x91\xa7Xq\xa5\x90'
        int_0 = -4458
        float_1 = -4406.424912
        complex_0 = None
        var_0 = module_0.burp(dict_0, bytes_0, int_0, float_1, complex_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b"\x19\xc2j\xe5\x87P\x9c(\xdf\xa2p'\x02*\xc7"
        dict_0 = {}
        str_0 = 'cs'
        list_0 = []
        bool_0 = None
        var_0 = module_0.burp(bytes_0, dict_0, str_0, list_0, list_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '-'
        var_0 = module_0.islurp(str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'tesO&t'
        var_0 = module_0.islurp(str_0)
        var_1 = list(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '-'
        bool_0 = False
        int_0 = 100
        int_1 = None
        var_0 = module_0.islurp(str_0, int_0, int_1, bool_0)
        dict_0 = None
        float_0 = -1912.574933
        var_1 = module_0.islurp(dict_0, str_0, float_0)
        var_2 = list(var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '-'
        bool_0 = False
        set_0 = {bool_0, str_0, bool_0, str_0}
        int_0 = -118
        bytes_0 = b''
        int_1 = -1082
        int_2 = 1971
        var_0 = module_0.islurp(int_1, int_2)
        var_1 = module_0.burp(str_0, set_0, int_0, bytes_0)
    except BaseException:
        pass