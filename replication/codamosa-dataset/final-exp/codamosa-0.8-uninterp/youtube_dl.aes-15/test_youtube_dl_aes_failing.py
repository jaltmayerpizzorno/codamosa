# Automatically generated by Pynguin.
import youtube_dl.aes as module_0
import youtube_dl.utils as module_1
import base64 as module_2

def test_case_0():
    try:
        bool_0 = None
        bytes_0 = b''
        var_0 = module_0.aes_ctr_decrypt(bool_0, bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b' \xbeX'
        var_0 = module_0.aes_cbc_decrypt(bytes_0, bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 9.0
        bool_0 = False
        str_0 = '3'
        list_0 = [bool_0, bool_0, bool_0]
        var_0 = module_0.aes_cbc_encrypt(float_0, list_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "FG~W'*6.PtjV`"
        var_0 = module_0.key_expansion(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = None
        var_0 = module_0.key_expansion(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = None
        list_0 = []
        var_0 = module_0.aes_decrypt(bool_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        set_0 = None
        bytes_0 = b'@S\xc5\xdfw\x15,\xfb\xa8'
        var_0 = module_0.aes_decrypt_text(str_0, set_0, bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 554
        var_0 = module_0.sub_bytes(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'000000000000000000000000000'
        var_0 = module_1.bytes_to_intlist(bytes_0)
        var_1 = module_0.aes_cbc_decrypt(bytes_0, var_0, bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '#]\tUMJ@fcrArteAX3.'
        var_0 = module_0.mix_columns_inv(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'c\x03\xbb:u\x95a\xcf\xae0\xf8\xab\xf2\x1f\xcc'
        var_0 = module_0.sub_bytes(bytes_0)
        bytes_1 = b'\xd7\xfd_\xc9\x89q\xb7\x1a \x13'
        var_1 = module_0.shift_rows(bytes_1)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = -1119.1
        var_0 = module_0.shift_rows_inv(float_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '+(urpgA[:TR]_C\x0cFV#'
        var_0 = module_0.inc(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b''
        var_0 = module_0.inc(bytes_0)
        bool_0 = True
        str_0 = '3'
        list_0 = [bool_0, bool_0, bool_0]
        var_1 = module_0.aes_cbc_encrypt(str_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        var_0 = module_0.mix_columns_inv(list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = ''
        set_0 = set()
        var_0 = module_1.bytes_to_intlist(set_0)
        str_1 = '=IG4:@C"5'
        float_0 = 2156.8
        tuple_0 = (float_0,)
        complex_0 = None
        tuple_1 = (tuple_0, set_0, complex_0)
        bool_0 = False
        var_1 = module_0.rijndael_mul(tuple_1, bool_0)
        tuple_2 = ()
        var_2 = module_0.aes_cbc_decrypt(str_0, str_1, tuple_2)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '1234567890123456'
        var_0 = module_1.bytes_to_intlist(str_0)
        var_1 = module_2.b64decode(str_0)
        var_2 = module_0.aes_cbc_encrypt(str_0, var_0, var_0)
    except BaseException:
        pass