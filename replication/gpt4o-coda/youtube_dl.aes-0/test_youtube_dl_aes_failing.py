# Automatically generated by Pynguin.
import youtube_dl.aes as module_0

def test_case_0():
    try:
        int_0 = -3392
        list_0 = [int_0, int_0, int_0]
        set_0 = None
        var_0 = module_0.aes_ctr_decrypt(set_0, list_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 107
        int_1 = 91
        tuple_0 = ()
        bool_0 = False
        list_0 = [int_0, int_1, int_0, bool_0, int_0, int_0, bool_0, int_1]
        set_0 = None
        var_0 = module_0.aes_ctr_decrypt(tuple_0, list_0, set_0)
        float_0 = 1741.0
        str_0 = '%Yp~sN45\x0c]9$CbK'
        var_1 = module_0.aes_cbc_decrypt(float_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -2398.591664
        bool_0 = False
        float_1 = 1993.910529
        var_0 = module_0.aes_cbc_encrypt(float_0, bool_0, float_1)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        var_0 = module_0.key_expansion(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        float_0 = -2879.443
        str_0 = '67P"V@1IJwXsYnR'
        set_0 = None
        tuple_0 = (bool_0, float_0, str_0, set_0)
        str_1 = '\x0c!J#<nL<\\veXeC^q@+|E'
        dict_0 = {str_1: set_0, tuple_0: float_0, set_0: bool_0}
        var_0 = module_0.aes_decrypt_text(tuple_0, dict_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Gv"'
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.key_expansion(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b' \xe4\x90\xc2\xa7\x7fkB\x06y\xa9\xf4\x07~'
        var_0 = module_0.sub_bytes_inv(bytes_0)
        bytes_1 = b'\xc9d'
        var_1 = module_0.shift_rows_inv(bytes_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'l\xaa^I'
        var_0 = module_0.mix_columns(bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\xf0O\x8f\x9f\xcc\x93\xe1\xe6\xeb]\xfe'
        var_0 = module_0.mix_columns_inv(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        var_0 = module_0.shift_rows(bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        tuple_0 = ()
        float_0 = None
        int_0 = None
        str_0 = '|%w\x0c32E$2PTzaBwH'
        var_0 = module_0.shift_rows(str_0)
        dict_0 = {float_0: tuple_0, float_0: int_0, int_0: tuple_0}
        var_1 = module_0.sub_bytes_inv(dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'Q\x86\x89\xa5\xc8\x8fQ\xb8\xe4\xdf\xda\xe8\xc17L'
        var_0 = module_0.shift_rows_inv(bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'-/\xe4\xc0\xb1E\x1e\xe0\x92~'
        var_0 = module_0.inc(bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        tuple_0 = None
        var_0 = module_0.inc(tuple_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'f!nx'
        str_1 = 'gc@-~i``.b||'
        int_0 = -426
        tuple_0 = (str_0, str_1, int_0, int_0)
        list_0 = []
        dict_0 = {str_0: str_0, str_1: int_0, int_0: list_0}
        bool_0 = False
        var_0 = module_0.rijndael_mul(bool_0, list_0)
        var_1 = module_0.key_schedule_core(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        tuple_0 = ()
        var_0 = module_0.inc(tuple_0)
        str_0 = '\tv/!wraM0OhsTzPY\x0b|'
        var_1 = module_0.shift_rows_inv(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'f!nx'
        list_0 = []
        var_0 = module_0.aes_decrypt(str_0, list_0)
        bytes_0 = b'\xefd6\xbe\x0f\xd4\xe0\x9c\x86&l\xeb6~'
        set_0 = set()
        var_1 = module_0.aes_decrypt_text(bytes_0, list_0, set_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'f!nx'
        list_0 = []
        var_0 = module_0.aes_decrypt(str_0, list_0)
        bytes_0 = b''
        str_1 = '>'
        str_2 = '3'
        var_1 = module_0.aes_decrypt_text(bytes_0, str_1, str_2)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = 91
        int_1 = 119
        tuple_0 = ()
        bool_0 = True
        list_0 = [int_1, int_0, bool_0, int_1, int_1]
        set_0 = None
        set_1 = {int_0, set_0}
        var_0 = module_0.aes_ctr_decrypt(tuple_0, list_0, set_1)
        float_0 = -1383.0
        int_2 = 1311970571
        var_1 = module_0.aes_cbc_decrypt(float_0, list_0, int_2)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 69
        int_1 = 91
        int_2 = 119
        int_3 = 116
        tuple_0 = ()
        bool_0 = False
        list_0 = [int_3, int_0, bool_0, int_2, int_2, int_3, int_1, int_0]
        set_0 = None
        set_1 = {int_3, set_0}
        var_0 = module_0.aes_ctr_decrypt(tuple_0, list_0, set_1)
        list_1 = [list_0, set_1]
        str_0 = '"G\rmaL'
        var_1 = module_0.aes_ctr_decrypt(list_1, list_0, str_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 69
        int_1 = 91
        int_2 = 116
        tuple_0 = ()
        bool_0 = True
        list_0 = [int_2, int_0, bool_0, int_2, int_2, int_2, int_1, int_0]
        str_0 = "'ag"
        var_0 = module_0.aes_decrypt(tuple_0, str_0)
        bytes_0 = b'WE'
        var_1 = module_0.aes_cbc_encrypt(bool_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_21():
    try:
        tuple_0 = ()
        str_0 = 'http://v.ku6.com/show/JG-8yS14xzBr4bCn1pu0xw...html'
        var_0 = module_0.aes_decrypt(tuple_0, str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        bool_0 = False
        int_0 = 116
        int_1 = 91
        int_2 = 119
        list_0 = [int_0, int_0, bool_0, int_2, int_2, int_0, int_1, int_0]
        tuple_0 = (int_0,)
        bytes_0 = b'\xcfJ'
        var_0 = module_0.aes_cbc_decrypt(tuple_0, list_0, bytes_0)
    except BaseException:
        pass