# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = -1676.05
    int_0 = 5
    token_0 = module_0.Token(float_0, int_0, int_0)

def test_case_2():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    dict_token_0 = module_0.DictToken(*list_0)
    list_1 = []
    token_0 = dict_token_0.lookup(list_1)
    bool_0 = token_0.__eq__(dict_token_0)

def test_case_3():
    str_0 = '?s1'
    int_0 = 3
    scalar_token_0 = module_0.ScalarToken(str_0, int_0, int_0)
    any_0 = scalar_token_0.__hash__()
    int_1 = None
    int_2 = -1153
    scalar_token_1 = module_0.ScalarToken(any_0, int_1, int_2)

def test_case_4():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    dict_token_0 = module_0.DictToken(*list_0)

def test_case_5():
    str_0 = '?s1'
    int_0 = 3
    scalar_token_0 = module_0.ScalarToken(str_0, int_0, int_0)
    any_0 = scalar_token_0.__hash__()
    int_1 = -833
    scalar_token_1 = module_0.ScalarToken(str_0, int_0, int_1)
    scalar_token_2 = module_0.ScalarToken(any_0, int_0, int_0)

def test_case_6():
    float_0 = -461.4783
    int_0 = 1904
    scalar_token_0 = module_0.ScalarToken(float_0, int_0, int_0)
    any_0 = scalar_token_0.__hash__()
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    dict_token_0 = module_0.DictToken(*list_0)
    list_1 = []
    token_0 = dict_token_0.lookup(list_1)
    token_1 = token_0.lookup(list_1)
    bool_0 = token_0.__eq__(list_0)
    scalar_token_1 = module_0.ScalarToken(dict_0, int_0, int_0)
    bool_1 = token_0.__eq__(scalar_token_1)
    int_1 = 35
    int_2 = -484
    int_3 = 3
    str_0 = 'a)0y:'
    list_token_0 = module_0.ListToken(int_1, int_2, int_3, str_0)
    bool_2 = token_0.__eq__(list_1)
    bool_3 = token_1.__eq__(str_0)