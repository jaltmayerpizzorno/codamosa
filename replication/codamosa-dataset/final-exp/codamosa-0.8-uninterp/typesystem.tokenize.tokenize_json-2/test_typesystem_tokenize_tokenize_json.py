# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0
import typesystem.tokenize.tokens as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '{"test": "string"}'
    token_0 = module_0.tokenize_json(str_0)

def test_case_2():
    str_0 = '{"foo": "bar", "baz": true, "a": 1.0, "b": [1, 2, 3]}'
    token_0 = module_0.tokenize_json(str_0)

def test_case_3():
    str_0 = '{}'
    token_0 = module_0.tokenize_json(str_0)
    int_0 = 0
    int_1 = 1
    str_1 = '[]'
    token_1 = module_0.tokenize_json(str_1)
    var_0 = []
    list_token_0 = module_1.ListToken(var_0, int_0, int_1, str_1)
    str_2 = '[1, 2, {"a": 3}]'
    token_2 = module_0.tokenize_json(str_2)
    scalar_token_0 = module_1.ScalarToken(int_1, int_1, int_1, str_2)
    int_2 = 3
    int_3 = 17
    scalar_token_1 = module_1.ScalarToken(int_2, int_3, int_3, str_2)

def test_case_4():
    str_0 = '{"a":1,"b":2,"c":true,"d":false,"e":null,"f":[1,2,3]}'
    token_0 = module_0.tokenize_json(str_0)