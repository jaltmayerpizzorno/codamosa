# Automatically generated by Pynguin.
import ansible.parsing.splitter as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.parse_kv(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "pRk`i$l'VM"
        var_0 = module_0.split_args(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\n        key1=value1\\=value2 key2=value3 "value4=value5" key3="key4=value6" key5\n    '
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 's&!HQ%EVEne'
        var_0 = module_0.parse_kv(str_0)
        str_1 = '\\?X:I7^8 \\'
        bytes_0 = b'\xb9R\x9ac\x8a24\xc2\xdd"\xea\x93\xc4\x08.\x9d'
        var_1 = module_0.parse_kv(str_1, bytes_0)
        bytes_1 = b'\xcb`$\xca\xf6#\x9c\x92|\xeb&'
        var_2 = module_0.parse_kv(bytes_1, bytes_1)
        str_2 = 'removed,'
        str_3 = '*rw(Pq]H0&?E+HVK'
        var_3 = module_0.parse_kv(str_2, str_3)
        float_0 = -1522.569
        dict_0 = {float_0: str_0}
        var_4 = module_0.parse_kv(float_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xe2\xf1"\xc6\xbcZ0X\xc7 bn\xden\xffp\n*\x12'
        var_0 = module_0.parse_kv(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "('%f2/~XEg;0ZiuhL\n\\"
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'u3OFjt,\nVR='
        var_0 = module_0.join_args(str_0)
        str_1 = 'C`='
        var_1 = module_0.parse_kv(str_1)
        str_2 = 'status'
        var_2 = module_0.split_args(str_2)
        str_3 = ''
        var_3 = module_0.split_args(str_3)
        str_4 = '^-R\\ttJ,'
        var_4 = module_0.parse_kv(str_4)
        str_5 = '0Wd!\n\r\x0br7dDPRuH>$.td'
        var_5 = module_0.parse_kv(str_5)
        str_6 = 'Ws\'Gj)*?I"nNp\x0cRPY iL'
        str_7 = '`hurw:as'
        float_0 = None
        var_6 = module_0.parse_kv(str_7, float_0)
        var_7 = module_0.parse_kv(str_6)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'n2p39fCXsbwnvZ\x0c{%@0'
        var_0 = module_0.parse_kv(str_0)
    except BaseException:
        pass