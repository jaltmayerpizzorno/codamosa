# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -26
    scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
    bool_0 = scalar_token_0.__eq__(scalar_token_0)

def test_case_2():
    str_0 = 'b'
    int_0 = 6
    int_1 = {}
    int_2 = -255
    list_0 = [int_1, int_0, str_0]
    dict_token_0 = module_0.DictToken(*list_0)
    int_3 = 1171
    token_0 = module_0.Token(int_3, int_0, int_2, str_0)
    bool_0 = token_0.__eq__(int_3)
    str_1 = 'no_match'
    token_1 = module_0.Token(dict_token_0, int_2, int_3, str_1)
    str_2 = token_1.__repr__()

def test_case_3():
    str_0 = 'rF<Q9\x0bfSx1@\x0cjrEwW0T'
    int_0 = 2
    scalar_token_0 = module_0.ScalarToken(str_0, int_0, int_0)
    any_0 = scalar_token_0.__hash__()

def test_case_4():
    str_0 = 'b'
    int_0 = 4
    int_1 = {}
    list_0 = [int_1, int_0, str_0]
    dict_token_0 = module_0.DictToken(*list_0)

def test_case_5():
    int_0 = 1
    int_1 = 20
    scalar_token_0 = module_0.ScalarToken(int_1, int_0, int_0)
    bool_0 = scalar_token_0.__eq__(int_1)
    bool_1 = scalar_token_0.__eq__(scalar_token_0)

def test_case_6():
    int_0 = 1
    scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
    int_1 = 2
    scalar_token_1 = module_0.ScalarToken(int_1, int_0, int_0)
    bool_0 = scalar_token_0.__eq__(scalar_token_1)

def test_case_7():
    str_0 = 'b'
    int_0 = {}
    int_1 = -255
    list_0 = [int_0, int_1, str_0]
    dict_token_0 = module_0.DictToken(*list_0)
    scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
    bool_0 = scalar_token_0.__eq__(dict_token_0)
    list_1 = [list_0, str_0, int_1]
    bool_1 = scalar_token_0.__eq__(list_1)

def test_case_8():
    str_0 = 'b'
    int_0 = {}
    list_0 = [int_0, int_0, str_0]
    dict_token_0 = module_0.DictToken(*list_0)
    scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
    bool_0 = scalar_token_0.__eq__(dict_token_0)

def test_case_9():
    int_0 = 1
    scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
    any_0 = scalar_token_0.__hash__()
    dict_0 = {}
    int_1 = 1053
    list_token_0 = module_0.ListToken(dict_0, int_0, int_1)
    scalar_token_1 = module_0.ScalarToken(int_0, int_0, int_1)
    bool_0 = scalar_token_1.__eq__(list_token_0)

def test_case_10():
    str_0 = 'value'
    int_0 = 1
    int_1 = 1
    str_1 = 'content'
    token_0 = module_0.Token(str_0, int_0, int_1, str_1)
    var_0 = token_0.start
    var_1 = token_0.end