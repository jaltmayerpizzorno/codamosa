# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 3690
    int_1 = 542
    scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_1)
    any_0 = scalar_token_0.__hash__()

def test_case_2():
    int_0 = -872
    token_0 = module_0.Token(int_0, int_0, int_0)
    str_0 = token_0.__repr__()

def test_case_3():
    list_0 = []
    int_0 = 0
    token_0 = module_0.Token(list_0, int_0, int_0)
    dict_0 = {}
    list_1 = [dict_0, token_0, int_0, token_0]
    dict_token_0 = module_0.DictToken(*list_1)

def test_case_4():
    str_0 = ' to JSON Schema'
    int_0 = 159
    list_0 = []
    list_1 = [int_0]
    int_1 = 2957
    token_0 = module_0.Token(list_1, int_1, int_0)
    token_1 = token_0.lookup(list_0)
    bool_0 = token_1.__eq__(str_0)
    int_2 = -898
    token_2 = module_0.Token(str_0, int_0, int_2)

def test_case_5():
    int_0 = 1
    scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
    scalar_token_1 = module_0.ScalarToken(int_0, int_0, int_0)
    var_0 = scalar_token_0 == scalar_token_1
    int_1 = 2
    scalar_token_2 = module_0.ScalarToken(int_0, int_1, int_0)
    var_1 = scalar_token_2 == scalar_token_1
    scalar_token_3 = module_0.ScalarToken(int_0, int_0, int_1)
    var_2 = scalar_token_3 == scalar_token_1
    scalar_token_4 = module_0.ScalarToken(int_1, int_0, int_0)
    var_3 = scalar_token_4 == scalar_token_1
    scalar_token_5 = [scalar_token_1]
    list_token_0 = module_0.ListToken(scalar_token_5, int_0, int_0)
    var_4 = list_token_0 == scalar_token_1
    var_5 = list_token_0 == scalar_token_1