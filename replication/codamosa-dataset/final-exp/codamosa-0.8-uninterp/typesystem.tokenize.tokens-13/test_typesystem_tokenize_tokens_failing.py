# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0

def test_case_0():
    try:
        list_0 = None
        tuple_0 = ()
        list_1 = [list_0, tuple_0, list_0]
        list_2 = []
        bool_0 = False
        int_0 = -100
        int_1 = -1420
        token_0 = module_0.Token(bool_0, int_0, int_1)
        token_1 = token_0.lookup(list_2)
        token_2 = token_1.lookup_key(list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'w'
        list_0 = [str_0]
        bytes_0 = b'\xd5\xc9U\x13\xb3\xdf\xca]2\xba\x80:\x10\x88\xf8'
        int_0 = -1435
        int_1 = -1976
        str_1 = 'y7y@)?~ g/@'
        token_0 = module_0.Token(bytes_0, int_0, int_1, str_1)
        token_1 = token_0.lookup_key(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        list_0 = []
        list_1 = [dict_0, list_0, list_0]
        dict_token_0 = module_0.DictToken(*list_1, **dict_0)
        int_0 = -3804
        token_0 = module_0.Token(dict_token_0, int_0, int_0)
        str_0 = token_0.__repr__()
        bool_0 = dict_token_0.__eq__(token_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_token_0 = module_0.DictToken()
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        list_0 = []
        list_1 = [dict_0, list_0, list_0]
        dict_token_0 = module_0.DictToken(*list_1, **dict_0)
        int_0 = -3804
        token_0 = module_0.Token(dict_token_0, int_0, int_0)
        bool_0 = dict_token_0.__eq__(token_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -1360.037
        set_0 = {float_0}
        int_0 = 18
        int_1 = -2992
        int_2 = 1645
        list_token_0 = module_0.ListToken(int_0, int_2, int_2)
        str_0 = '#GF7SXVO?=+$\t'
        scalar_token_0 = module_0.ScalarToken(set_0, int_0, int_1, str_0)
        str_1 = 'Unsupported $ref style in document.'
        int_3 = 997
        int_4 = 609
        scalar_token_1 = module_0.ScalarToken(scalar_token_0, int_3, int_4)
        int_5 = 1372
        token_0 = module_0.Token(str_1, int_5, int_5)
        dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1, str_1: str_1}
        list_0 = [dict_0, str_1, str_1]
        dict_token_0 = module_0.DictToken(*list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b''
        list_0 = [bytes_0, bytes_0]
        list_1 = [list_0]
        dict_0 = {}
        list_2 = [dict_0, dict_0, dict_0, dict_0]
        dict_token_0 = module_0.DictToken(*list_2)
        token_0 = dict_token_0.lookup_key(list_1)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = {}
        list_0 = [dict_0]
        list_1 = []
        list_2 = [dict_0, list_1, list_1]
        dict_token_0 = module_0.DictToken(*list_2, **dict_0)
        token_0 = dict_token_0.lookup(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        list_0 = []
        list_1 = [dict_0, list_0, list_0]
        dict_token_0 = module_0.DictToken(*list_1, **dict_0)
        int_0 = 3
        list_token_0 = module_0.ListToken(list_1, int_0, int_0)
        bool_0 = dict_token_0.__eq__(list_token_0)
    except BaseException:
        pass