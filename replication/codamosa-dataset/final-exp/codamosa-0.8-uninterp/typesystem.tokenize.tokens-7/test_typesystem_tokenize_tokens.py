# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    int_0 = 0
    scalar_token_0 = module_0.ScalarToken(list_0, int_0, int_0)

def test_case_2():
    bytes_0 = b'j: '
    int_0 = 5
    int_1 = 3
    scalar_token_0 = module_0.ScalarToken(bytes_0, int_0, int_1)
    any_0 = scalar_token_0.__hash__()
    int_2 = -341
    int_3 = -1232
    token_0 = module_0.Token(any_0, int_2, int_3)
    token_1 = module_0.Token(token_0, int_0, int_0)
    str_0 = token_1.__repr__()

def test_case_3():
    int_0 = 36
    scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
    scalar_token_1 = module_0.ScalarToken(int_0, int_0, int_0)

def test_case_4():
    str_0 = 'pLc;L=5%'
    dict_0 = {}
    list_0 = [dict_0, str_0, dict_0]
    dict_token_0 = module_0.DictToken(*list_0)

def test_case_5():
    int_0 = 959
    list_0 = [int_0, int_0, int_0]
    bytes_0 = b'\xcf\xb1#\xa4\x8bv\xc2\xcb\xff'
    int_1 = 1037
    str_0 = '>jMtk >r][SX{XFDw\x0c'
    token_0 = module_0.Token(bytes_0, int_1, int_1, str_0)
    bool_0 = token_0.__eq__(list_0)