# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0
import typesystem.base as module_1

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    int_0 = -2713
    list_token_0 = module_0.ListToken(list_0, int_0, int_0)

def test_case_2():
    bytes_0 = b'\xc6\xd1W\xea\xe3'
    int_0 = -2957
    int_1 = -858
    str_0 = "*Lj'Kg~-NXpzhe%pdZ"
    token_0 = module_0.Token(int_0, int_1, int_0, str_0)
    bool_0 = token_0.__eq__(bytes_0)

def test_case_3():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    dict_token_0 = module_0.DictToken(*list_0, **dict_0)

def test_case_4():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    int_0 = 2115
    scalar_token_0 = module_0.ScalarToken(dict_0, int_0, int_0)
    dict_token_0 = module_0.DictToken(*list_0, **dict_0)
    bool_0 = scalar_token_0.__eq__(dict_token_0)

def test_case_5():
    int_0 = 1
    int_1 = 0
    scalar_token_0 = module_0.ScalarToken(int_0, int_1, int_1)
    bool_0 = scalar_token_0.__eq__(scalar_token_0)
    bool_1 = scalar_token_0.__eq__(scalar_token_0)
    scalar_token_1 = module_0.ScalarToken(int_0, int_1, int_0)
    bool_2 = scalar_token_1.__eq__(scalar_token_1)
    int_2 = 2
    scalar_token_2 = module_0.ScalarToken(int_2, int_1, int_1)
    bool_3 = scalar_token_2.__eq__(scalar_token_2)

def test_case_6():
    int_0 = 1
    int_1 = 0
    scalar_token_0 = module_0.ScalarToken(int_0, int_1, int_1)
    scalar_token_1 = module_0.ScalarToken(int_0, int_1, int_1)
    bool_0 = scalar_token_0.__eq__(scalar_token_1)
    scalar_token_2 = module_0.ScalarToken(int_0, int_0, int_1)
    bool_1 = scalar_token_0.__eq__(scalar_token_2)
    scalar_token_3 = module_0.ScalarToken(int_0, int_1, int_0)
    bool_2 = scalar_token_0.__eq__(scalar_token_3)
    int_2 = 2
    scalar_token_4 = module_0.ScalarToken(int_2, int_1, int_1)
    bool_3 = scalar_token_0.__eq__(scalar_token_4)

def test_case_7():
    int_0 = 10
    int_1 = 1
    int_2 = 5
    scalar_token_0 = module_0.ScalarToken(int_0, int_1, int_2)
    int_3 = 2
    int_4 = 3
    position_0 = module_1.Position(int_1, int_4, int_3)
    int_5 = 12
    position_1 = module_1.Position(int_1, int_5, int_0)
    scalar_token_1 = module_0.ScalarToken(int_0, int_1, int_2)
    var_0 = scalar_token_1.value