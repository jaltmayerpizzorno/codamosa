# Automatically generated by Pynguin.
import ansible.utils.vars as module_0

def test_case_0():
    try:
        int_0 = -2362
        str_0 = 'r?gnwV'
        var_0 = module_0.merge_hash(int_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x97\xd0X\xcd*\xff\\}_\xa55\x8c\xf2\xad\xb1x\xd8A\x96('
        bool_0 = False
        var_0 = module_0.merge_hash(bytes_0, bool_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'G'
        complex_0 = None
        var_0 = module_0.combine_vars(str_0, complex_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = None
        float_0 = 1163.8
        bytes_0 = b'\xa9\x91\xaf\xde\x1d\xc1\xc2\xffO\xc4\xa9\xa6\xbd\x07Y%'
        var_0 = module_0.combine_vars(bool_0, float_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        var_0 = module_0.load_extra_vars(tuple_0)
        bytes_0 = b'\xf7\xd3'
        var_1 = module_0.load_extra_vars(bytes_0)
        str_0 = 'ppc'
        int_0 = 32700
        var_2 = module_0.merge_hash(tuple_0, str_0, int_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        bytes_0 = b'6\xbbz\xe1H\x9d\x8f\xe7\xff\xfeT'
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bytes_0, bool_0: bool_0}
        var_0 = module_0.combine_vars(dict_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '-D'
        tuple_0 = None
        dict_0 = {}
        var_0 = module_0.combine_vars(str_0, tuple_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'a'
        list_0 = []
        int_0 = 254
        int_1 = {str_0: int_0}
        bytes_0 = b'\x84\xaes\x87-\x1ce\x97"'
        bool_0 = False
        var_0 = module_0.load_extra_vars(bool_0)
        var_1 = module_0._isidentifier_PY3(bytes_0)
        int_2 = 2
        int_3 = {str_0: int_2}
        bool_1 = False
        str_1 = 'replace'
        list_1 = []
        dict_0 = {str_0: list_1}
        var_2 = module_0.load_options_vars(dict_0)
        var_3 = module_0.merge_hash(int_1, int_3, bool_1, str_1)
        var_4 = module_0.merge_hash(bytes_0, list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '%s | UNREACHABLE!: %s'
        dict_0 = {str_0: str_0}
        var_0 = module_0.merge_hash(dict_0, dict_0)
        var_1 = module_0.get_unique_id()
        dict_1 = {}
        set_0 = set()
        var_2 = module_0.combine_vars(dict_1, set_0)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = {}
        var_1 = dict(a=var_0)
        dict_0 = None
        var_2 = module_0.load_options_vars(dict_0)
        int_0 = 656000
        float_0 = 60.0
        var_3 = module_0.load_options_vars(float_0)
        var_4 = module_0.load_extra_vars(int_0)
        var_5 = dict(a=var_0)
        var_6 = dict(a=dict_0)
        var_7 = module_0.merge_hash(var_1, var_6)
        list_0 = []
        str_0 = 'Ih8jm8'
        var_8 = module_0._isidentifier_PY3(str_0)
        set_0 = set()
        var_9 = module_0._isidentifier_PY3(set_0)
        var_10 = module_0.load_extra_vars(list_0)
        str_1 = '1\t,x3MyUr)x3=%zh'
        var_11 = module_0.load_extra_vars(str_1)
        set_1 = set()
        var_12 = module_0.combine_vars(set_1, str_1)
    except BaseException:
        pass