# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0
import typesystem.tokenize.tokens as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'object'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_2():
    str_0 = '123'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_3():
    str_0 = '{p}'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_4():
    str_0 = '\n    test: value\n    list:\n    - item1\n    - item2\n    '
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_5():
    str_0 = '123'
    token_0 = module_0.tokenize_yaml(str_0)
    int_0 = 123
    int_1 = 0
    int_2 = 2
    scalar_token_0 = module_1.ScalarToken(int_0, int_1, int_2, str_0)
    token_1 = module_0.tokenize_yaml(str_0)
    str_1 = 'abc'
    int_3 = 5
    scalar_token_1 = module_1.ScalarToken(str_1, int_1, int_3, str_0)
    str_2 = 'true'
    token_2 = module_0.tokenize_yaml(str_2)
    str_3 = '[1, 2, 3]'
    token_3 = module_0.tokenize_yaml(str_3)