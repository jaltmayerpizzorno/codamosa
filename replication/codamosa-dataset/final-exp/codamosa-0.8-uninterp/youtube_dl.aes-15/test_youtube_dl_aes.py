# Automatically generated by Pynguin.
import youtube_dl.utils as module_0
import youtube_dl.aes as module_1
import base64 as module_2

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'1qazqazqazqazqaz'
    var_0 = module_0.bytes_to_intlist(bytes_0)
    var_1 = module_1.key_expansion(var_0)
    var_2 = module_1.aes_encrypt(var_0, var_1)

def test_case_2():
    bytes_0 = b's\x87\x92_\xa6\xef\xa1\x87\xf8\x1c\xb5\x95@1'
    var_0 = module_1.sub_bytes_inv(bytes_0)

def test_case_3():
    float_0 = 3322.88795
    list_0 = [float_0]
    var_0 = module_1.inc(list_0)

def test_case_4():
    bytes_0 = b'U2FsdGVkX1+Eu6Rjx6x2u6zzsTvTjfm3G/3c7JVBkWY='
    var_0 = module_0.bytes_to_intlist(bytes_0)
    bytes_1 = b'00000000000000000000000000000000'
    var_1 = module_0.bytes_to_intlist(bytes_1)
    var_2 = module_0.bytes_to_intlist(bytes_1)
    var_3 = module_1.aes_cbc_decrypt(var_0, var_1, var_2)

def test_case_5():
    str_0 = '1234567890123456'
    var_0 = module_0.bytes_to_intlist(str_0)
    var_1 = module_0.bytes_to_intlist(var_0)
    var_2 = module_2.b64decode(str_0)
    var_3 = module_0.bytes_to_intlist(var_2)
    var_4 = module_1.aes_cbc_encrypt(var_3, var_0, var_1)
    var_5 = module_1.aes_cbc_decrypt(var_4, var_0, var_1)
    var_6 = bytes(var_5)
    var_7 = bytes(var_3)

def test_case_6():
    str_0 = 'password'
    str_1 = 'ApEFyg4BH4QJZOtXvYtBjWF5r5xQyki6OWLN/JN5w1RE='
    int_0 = 16
    var_0 = module_1.aes_decrypt_text(str_1, str_0, int_0)
    str_2 = 'password'
    str_3 = 'BxlD6y7GpvfehWwFzKj3q6ZY9B0e2hacr5xQyki6KWLN/JN5w1RE='
    var_1 = module_1.aes_decrypt_text(str_3, str_2, int_0)

def test_case_7():
    str_0 = 'password'
    str_1 = 'ApEFyg4BH4QJZOtXvYtBjWF5r5xQyki6OWLN/JN5w1RE='
    int_0 = 16
    var_0 = module_1.aes_decrypt_text(str_1, str_0, int_0)
    str_2 = 'password'
    str_3 = 'BxlD6y7GpvfehWwFzKj3q6ZY9B0e2hacr5xQyki6KWLN/JN5w1RE='
    int_1 = 24
    var_1 = module_1.aes_decrypt_text(str_3, str_2, int_1)

def test_case_8():
    int_0 = 255
    int_1 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    var_0 = module_1.inc(int_1)
    str_0 = '[Error] Unit test for inc(data) failed'
    var_1 = print(str_0)
    str_1 = '[Success] Unit test for inc(data) passed'
    var_2 = print(str_1)
    var_3 = module_1.inc(int_1)