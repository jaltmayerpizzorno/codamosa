# Automatically generated by Pynguin.
import youtube_dl.aes as module_0
import youtube_dl.utils as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'gRLx1x3HqkyzsM+ktMn6nA=='
    str_1 = 'pwd'
    int_0 = 16
    var_0 = module_0.aes_decrypt_text(str_0, str_1, int_0)

def test_case_2():
    bytes_0 = b'\xbb\xd6\x8d\xa5\xcd*\x85\xe5\x07\x17\xe1\xf8I\xf7^\xf9\xc7'
    var_0 = module_0.shift_rows(bytes_0)

def test_case_3():
    bytes_0 = b'abcdefghijklmnopqrstuvwxyz'
    bytes_1 = b'YELLOW SUBMARINE'
    var_0 = module_1.bytes_to_intlist(bytes_1)
    var_1 = module_1.bytes_to_intlist(bytes_1)
    var_2 = module_1.bytes_to_intlist(bytes_0)
    var_3 = module_0.aes_cbc_encrypt(var_0, var_1, var_2)
    var_4 = module_1.intlist_to_bytes(var_3)
    var_5 = module_1.bytes_to_intlist(var_4)
    var_6 = module_1.bytes_to_intlist(bytes_1)
    var_7 = module_1.bytes_to_intlist(bytes_0)
    var_8 = module_0.aes_cbc_decrypt(var_5, var_6, var_7)
    var_9 = module_1.intlist_to_bytes(var_8)

def test_case_4():
    int_0 = 0
    int_1 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.inc(int_1)
    int_2 = 1
    int_3 = [int_0, int_0, int_0, int_2]
    var_1 = module_0.inc(int_3)
    int_4 = 255
    int_5 = [int_0, int_0, int_0, int_4]
    var_2 = module_0.inc(int_5)
    int_6 = [int_0, int_0, int_2, int_0]
    var_3 = module_0.inc(int_6)
    int_7 = [int_0, int_0, int_2, int_2]
    var_4 = module_0.inc(int_7)

def test_case_5():
    str_0 = 'AQAAAABQAAQAAAAIAQAAAAMAAAAEAAAABgAAAAYAAAAHAAAACAAAAAkAAAAJAAAACgAAABAAAAAQAAAA=='
    str_1 = ''
    int_0 = 16
    var_0 = module_0.aes_decrypt_text(str_0, str_1, int_0)
    int_1 = 24
    var_1 = module_0.aes_decrypt_text(str_0, str_1, int_1)

def test_case_6():
    str_0 = 'AQAAAABQAAQAAAAIAQAAAAMAAAAEAAAABgAAAAYAAAAHAAAACAAAAAkAAAAJAAAACgAAABAAAAAQAAAA=='
    str_1 = ''
    int_0 = 16
    var_0 = module_0.aes_decrypt_text(str_0, str_1, int_0)
    int_1 = 24
    var_1 = module_0.aes_decrypt_text(str_0, str_1, int_1)
    int_2 = 32
    var_2 = module_0.aes_decrypt_text(str_0, str_1, int_2)