# Automatically generated by Pynguin.
import youtube_dl.aes as module_0

def test_case_0():
    try:
        int_0 = -275
        var_0 = module_0.sub_bytes(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"1Q\x97c\xcd\xb0\xfb'\xc8\xc3="
        tuple_0 = None
        str_0 = '#)'
        tuple_1 = (bytes_0, tuple_0, str_0)
        bytes_1 = b't\x9b\x0f\xa5\x08'
        list_0 = [bytes_0, str_0]
        var_0 = module_0.aes_cbc_decrypt(bytes_1, tuple_1, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        bytes_0 = b'\xe4\x04\xc0!d\x84\xd0\xcb\xd0\xa6\xc3q\xbd)\xad\xebNl\x82&'
        var_0 = module_0.aes_decrypt(bool_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'kf8cIdzvMV7ia5/Za5V8WwD5eoIqx3rPxBQ8WFD='
        int_0 = 18
        var_0 = module_0.aes_decrypt_text(str_0, str_0, int_0)
        bool_0 = True
        var_1 = module_0.sub_bytes_inv(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'P#|%T[az\nbJNU78'
        var_0 = module_0.mix_columns(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = None
        var_0 = module_0.mix_columns(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = None
        var_0 = module_0.mix_columns_inv(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = {}
        var_0 = module_0.shift_rows(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'HoH5*7{fg"'
        var_0 = module_0.shift_rows_inv(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = False
        var_0 = module_0.inc(bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        str_0 = '/d%s1B[Lektz2'
        list_0 = [str_0, str_0, bool_0]
        var_0 = module_0.aes_cbc_encrypt(str_0, list_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'kf8cIdzvMV7ia5/Za5V8WwD5eoIqx3rPxBQ8WFD='
        int_0 = 18
        var_0 = module_0.aes_decrypt_text(str_0, str_0, int_0)
        int_1 = 2050
        list_0 = [int_1, int_0]
        var_1 = module_0.sub_bytes_inv(list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'z?\rW>Iq#c=6'
        bool_0 = False
        var_0 = module_0.rijndael_mul(str_0, bool_0)
        set_0 = set()
        var_1 = module_0.shift_rows_inv(set_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'kf8cIdzvMV7ia5/Za5V8WwD5eoIqx3rPxBQ8WFD='
        int_0 = 24
        tuple_0 = ()
        var_0 = module_0.sub_bytes_inv(tuple_0)
        var_1 = module_0.aes_decrypt_text(str_0, str_0, int_0)
        float_0 = 606.76
        float_1 = 362.0
        float_2 = -940.7507
        str_1 = 'M'
        str_2 = 'Gd%1._B[LekJt2'
        float_3 = 1946.51
        list_0 = [int_0, float_1, var_1, float_3]
        dict_0 = {float_1: float_2}
        bytes_0 = b' \xa7nY\xfc\x0c\xfd\x06\x8dj<\xeb\xfdN'
        dict_1 = {float_1: float_0, bytes_0: float_2, str_1: str_2}
        var_2 = module_0.aes_cbc_encrypt(list_0, dict_0, dict_1)
    except BaseException:
        pass