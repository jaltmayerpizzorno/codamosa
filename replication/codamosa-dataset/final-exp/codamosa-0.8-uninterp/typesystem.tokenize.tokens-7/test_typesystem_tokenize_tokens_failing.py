# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0

def test_case_0():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        str_0 = ''
        int_0 = 620
        token_0 = module_0.Token(str_0, int_0, int_0)
        token_1 = token_0.lookup(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'I<'
        list_0 = [str_0, str_0, str_0, str_0]
        str_1 = ''
        list_1 = [list_0, str_0, str_0, str_1]
        list_2 = [list_1]
        tuple_0 = ()
        int_0 = 4
        token_0 = module_0.Token(tuple_0, int_0, int_0)
        token_1 = token_0.lookup_key(list_2)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        int_0 = 0
        scalar_token_0 = module_0.ScalarToken(list_0, int_0, int_0)
        any_0 = scalar_token_0.__hash__()
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        int_0 = 4
        token_0 = module_0.Token(tuple_0, int_0, int_0)
        bool_0 = token_0.__eq__(token_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'J\xa5\xc1\x93\xa6\x01gfs\xc8\x94\xa9\xad\x0eK'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        int_0 = -379
        scalar_token_0 = module_0.ScalarToken(bytes_0, int_0, int_0)
        int_1 = -1267
        int_2 = -613
        str_0 = 'BZ\x0c2LX\x0bA='
        scalar_token_1 = module_0.ScalarToken(dict_0, int_1, int_2, str_0)
        int_3 = 2779
        token_0 = module_0.Token(scalar_token_1, int_2, int_3)
        str_1 = token_0.__repr__()
        int_4 = -3282
        token_1 = module_0.Token(int_3, int_3, int_4, str_1)
        list_0 = [dict_0, dict_0, scalar_token_1]
        dict_1 = {}
        dict_token_0 = module_0.DictToken(*list_0, **dict_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 1
        int_1 = 0
        scalar_token_0 = module_0.ScalarToken(int_0, int_1, int_0)
        scalar_token_1 = module_0.ScalarToken(scalar_token_0, int_1, int_0)
        int_2 = 2
        scalar_token_2 = module_0.ScalarToken(int_2, int_1, int_0)
        list_0 = [scalar_token_1, int_2]
        int_3 = 2028
        token_0 = module_0.Token(list_0, int_0, int_3)
        token_1 = token_0.lookup(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 36
        scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
        int_1 = 56
        scalar_token_1 = module_0.ScalarToken(int_0, int_1, int_0)
        int_2 = -24
        scalar_token_2 = module_0.ScalarToken(int_2, int_0, int_0)
        list_0 = [int_0, scalar_token_2, int_0]
        int_3 = 2
        str_0 = 'Invalid argument '
        token_0 = module_0.Token(list_0, int_0, int_3, str_0)
        token_1 = token_0.lookup(list_0)
    except BaseException:
        pass