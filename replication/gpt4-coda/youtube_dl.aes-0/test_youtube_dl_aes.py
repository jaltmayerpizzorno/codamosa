# Automatically generated by Pynguin.
import youtube_dl.aes as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'MGaLy\n3I\\-rF2ki`'
    int_0 = 16
    var_0 = module_0.aes_decrypt_text(str_0, str_0, int_0)

def test_case_2():
    str_0 = '3q2+7w=='
    int_0 = 16
    var_0 = module_0.aes_decrypt_text(str_0, str_0, int_0)

def test_case_3():
    int_0 = 217
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.key_expansion(list_0)
    bytes_0 = b'\xa5\x1f\xd8\x91\x18V\xdf\xdd1\xd3\xd6\xd0\xee\x18\r\xe4\xc3\xe7'
    var_1 = module_0.sub_bytes_inv(bytes_0)

def test_case_4():
    int_0 = 217
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.key_expansion(list_0)

def test_case_5():
    bytes_0 = b'\xa3\xf8\xb6\xd3\xaf\x9c\x05Td\\\x82\xb2\x92\xd8m#\x1bs'
    var_0 = module_0.mix_columns(bytes_0)

def test_case_6():
    int_0 = 72
    int_1 = 101
    int_2 = 108
    int_3 = 32
    int_4 = 87
    int_5 = 114
    int_6 = 100
    int_7 = 33
    int_8 = [int_0, int_1, int_2, int_2, int_6, int_3, int_4, int_6, int_5, int_2, int_6, int_7]
    int_9 = 1
    int_10 = [int_9]
    int_11 = 16
    var_0 = int_10 * int_11
    int_12 = 0
    int_13 = [int_12]
    var_1 = int_13 * int_11
    var_2 = module_0.aes_cbc_encrypt(int_8, var_0, var_1)
    var_3 = module_0.aes_cbc_decrypt(var_2, var_0, var_1)

def test_case_7():
    str_0 = 'MG&Ly\n,I\\-rFk`'
    int_0 = 24
    var_0 = module_0.aes_decrypt_text(str_0, str_0, int_0)

def test_case_8():
    int_0 = 87
    int_1 = 131
    var_0 = module_0.rijndael_mul(int_0, int_1)
    int_2 = 77
    int_3 = 2
    var_1 = module_0.rijndael_mul(int_2, int_3)
    int_4 = 1
    var_2 = module_0.rijndael_mul(int_4, int_4)
    int_5 = 0
    var_3 = module_0.rijndael_mul(int_5, int_3)
    var_4 = module_0.rijndael_mul(int_3, int_5)
    int_6 = 126
    int_7 = 19
    var_5 = module_0.rijndael_mul(int_6, int_7)

def test_case_9():
    int_0 = 0
    int_1 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.inc(int_1)
    int_2 = 18
    int_3 = 52
    int_4 = 86
    int_5 = 120
    int_6 = [int_2, int_3, int_4, int_5]
    var_1 = module_0.inc(int_6)
    int_7 = 255
    int_8 = [int_0, int_0, int_0, int_7]
    var_2 = module_0.inc(int_8)
    int_9 = [int_7, int_7, int_7, int_7]
    var_3 = module_0.inc(int_9)