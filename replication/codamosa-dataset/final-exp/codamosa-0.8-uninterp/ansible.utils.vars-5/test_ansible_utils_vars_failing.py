# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    try:
        bool_0 = False
        bytes_0 = b'\xaf\xa2[\x8a3\xe4\xf8\x11\xf8\xaerfk'
        var_0 = module_0.combine_vars(bool_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.get_unique_id()
        var_1 = module_0.get_unique_id()
        str_0 = '{Y:'
        dict_0 = {str_0: str_0, var_1: str_0, var_1: var_1}
        var_2 = module_0.load_extra_vars(dict_0)
        int_0 = 465
        var_3 = module_0.combine_vars(dict_0, dict_0)
        bytes_0 = b'\xe5\xb8I\xa4N\x0e(\x7f\xe7\x8f\xea\x98\x17TH\xd1c1\xbf'
        var_4 = module_0._isidentifier_PY3(bytes_0)
        str_1 = 'u'
        var_5 = module_0.combine_vars(int_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '3ECezEg>Orauuz'
        bytes_0 = None
        dict_0 = {bytes_0: str_0, bytes_0: bytes_0}
        var_0 = module_0.merge_hash(str_0, bytes_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '$\tvj26GX6`C?@e52,$c'
        bytes_0 = b'tW\n\xab\xfa\xf2\xddx\xf7\x91\xd6R'
        bool_0 = True
        var_0 = module_0.load_extra_vars(bool_0)
        str_1 = 'W'
        var_1 = module_0.load_options_vars(str_1)
        dict_0 = {}
        var_2 = module_0.load_options_vars(dict_0)
        int_0 = None
        var_3 = module_0.load_options_vars(int_0)
        var_4 = module_0.merge_hash(str_0, bytes_0, str_1, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'G#1K\nV^d|\n)2RI2yxuK2'
        var_0 = module_0._isidentifier_PY3(str_0)
        str_1 = '/(,BKW#'
        str_2 = ''
        var_1 = module_0.combine_vars(str_1, str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        bytes_0 = b'\xaf\xa2[\x8a3\xe4\xf8\x11\xf8\xaerfk'
        var_0 = module_0._isidentifier_PY3(bool_0)
        var_1 = module_0.combine_vars(bool_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '$\tvj26GX6`C?@e52,$c'
        bytes_0 = b'tW\n\xab\xfa\xf2\xddx\xf7\x91\xd6R'
        dict_0 = {str_0: bytes_0, str_0: bytes_0, bytes_0: str_0}
        list_0 = None
        var_0 = module_0.merge_hash(dict_0, list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        var_0 = module_0.get_unique_id()
        var_1 = module_0.get_unique_id()
        str_0 = '{Y:'
        dict_0 = {str_0: str_0, var_1: str_0, var_1: var_1}
        var_2 = module_0.load_extra_vars(dict_0)
        int_0 = 465
        dict_1 = {var_1: dict_0}
        var_3 = module_0.combine_vars(dict_1, dict_1)
        bytes_0 = b'\xe5\xb8I\xa4N\x0e(\x7f\xe7\x8f\xea\x98\x17TH\xd1c1\xbf'
        var_4 = module_0._isidentifier_PY3(bytes_0)
        str_1 = ''
        var_5 = module_0.combine_vars(int_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = {}
        var_1 = {}
        var_2 = module_0.merge_hash(var_0, var_1)
        var_3 = {}
        str_0 = ''
        int_0 = 1
        int_1 = {str_0: int_0}
        var_4 = module_0.merge_hash(var_3, int_1)
        int_2 = {str_0: int_0}
        int_3 = 2
        int_4 = {str_0: int_3}
        str_1 = "qdi\nmZa6zp'"
        var_5 = module_0._isidentifier_PY3(str_1)
        bytes_0 = b'8\xf6Ym\xa4\xb2C\r\x16T:9\xc4\x8fm\xeb\xc0\xc2\xe5\x00'
        var_6 = module_0.load_extra_vars(bytes_0)
        var_7 = module_0.merge_hash(int_2, int_4)
        int_5 = {str_0: int_3}
        var_8 = module_0.merge_hash(int_4, int_5)
        int_6 = {str_0: int_3}
        bool_0 = False
        var_9 = module_0.merge_hash(int_0, int_6, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = {}
        var_1 = {}
        var_2 = module_0.merge_hash(var_0, var_1)
        str_0 = '--comment'
        int_0 = -3
        int_1 = {str_0: int_0}
        bytes_0 = b'8\xf6Ym\xa4\xb2C\r\x16T:9\xc4\x8fm\xeb\xc0\xc2\xe5\x00'
        tuple_0 = ()
        var_3 = module_0.load_options_vars(tuple_0)
        var_4 = module_0.load_extra_vars(bytes_0)
        int_2 = {str_0: int_1}
        int_3 = {str_0: int_0}
        var_5 = module_0.merge_hash(int_2, int_3)
        var_6 = module_0.load_options_vars(int_1)
        var_7 = module_0._isidentifier_PY3(tuple_0)
    except BaseException:
        pass