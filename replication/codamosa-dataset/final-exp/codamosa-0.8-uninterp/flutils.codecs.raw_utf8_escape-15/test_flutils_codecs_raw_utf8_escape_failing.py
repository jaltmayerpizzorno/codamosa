# Automatically generated by Pynguin.
import flutils.codecs.raw_utf8_escape as module_0
import collections as module_1
import codecs as module_2

def test_case_0():
    try:
        bytes_0 = b'\xe3 \xb6\x88\x7fc\xf2p\xda\x05\x93\xb0\x92fb\xc1'
        int_0 = 1203
        tuple_0 = (bytes_0, int_0)
        module_0.register()
        int_1 = 86
        module_0.register()
        user_string_0 = module_1.UserString(int_1)
        tuple_1 = module_0.encode(user_string_0)
        str_0 = 'X{{9aZWpt"\tfR\x0bjaKBy1'
        var_0 = user_string_0.capitalize()
        tuple_2 = module_0.encode(user_string_0)
        tuple_3 = (str_0, int_0)
        dict_0 = {int_0: tuple_3, tuple_0: int_0}
        user_string_1 = module_1.UserString(dict_0)
        tuple_4 = module_0.encode(str_0)
        tuple_5 = module_0.encode(str_0)
        tuple_6 = module_0.encode(user_string_1, user_string_1)
    except BaseException:
        pass

def test_case_1():
    try:
        module_0.register()
        bytes_0 = b'\xf4\xd8\x0b+}[\xb7\x01}k\xcb#8\x17\x97\xffT#\xfe'
        module_0.register()
        user_string_0 = module_1.UserString(bytes_0)
        var_0 = user_string_0.isidentifier()
        tuple_0 = module_0.encode(user_string_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xe3 \xb6\x88\x7fc\xf2p\xfc\xda\x05\x93\xb0\x92fb\xc1'
        module_0.register()
        module_0.register()
        str_0 = 'X{{9aZWpC"\tfR\x0bjaKBy1'
        tuple_0 = module_0.encode(str_0)
        tuple_1 = module_0.decode(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '>-#16guj@},\t-'
        int_0 = 80
        tuple_0 = module_0.encode(str_0, str_0)
        dict_0 = {}
        tuple_1 = module_0.encode(str_0, str_0)
        tuple_2 = module_0.decode(dict_0)
        module_0.register()
        tuple_3 = (str_0, int_0)
        module_0.register()
        tuple_4 = module_0.decode(tuple_3, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Vf<!Wv'
        tuple_0 = module_0.decode(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        module_0.register()
        module_0.register()
        byte_string_0 = None
        tuple_0 = module_0.decode(byte_string_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'X'
        var_0 = module_2.getdecoder(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        module_0.register()
        bytes_0 = b"\xef\xa0\xe2\xbd\xf9\xfeZ\\\xe3\\\xe1\x80'\xd8\x94\x10\x80s"
        complex_0 = None
        user_string_0 = module_1.UserString(complex_0)
        tuple_0 = module_0.decode(bytes_0, user_string_0)
    except BaseException:
        pass