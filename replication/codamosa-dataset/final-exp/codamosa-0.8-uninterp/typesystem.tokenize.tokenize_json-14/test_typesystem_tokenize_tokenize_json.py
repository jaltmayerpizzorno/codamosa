# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0
import typesystem.tokenize.tokens as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '{"name":"test","age":12,"details":{"height":5.5,"weight":12.5}}'
    token_0 = module_0.tokenize_json(str_0)

def test_case_2():
    str_0 = '{"foo": [1, 2, 3]}'
    token_0 = module_0.tokenize_json(str_0)

def test_case_3():
    str_0 = 'false'
    token_0 = module_0.tokenize_json(str_0)

def test_case_4():
    str_0 = '\n    {\n        "username": "jsmith",\n        "first_name": "Joe",\n        "last_name": "Smith",\n        "email": "jsmith@example.com",\n        "phone_number": "123-456-7890",\n        "address": {\n            "street": "123 Main Street",\n            "city": "Evergreen",\n            "state": "PA",\n            "zip_code": 12345\n        },\n        "favorite_color": "blue",\n        "hobbies": ["climbing", "hiking", "biking"]\n    }\n    '
    token_0 = module_0.tokenize_json(str_0)

def test_case_5():
    str_0 = 'foo'
    int_0 = 3
    int_1 = 5
    scalar_token_0 = module_1.ScalarToken(str_0, int_0, int_1, str_0)
    str_1 = 'bar'
    int_2 = 14
    int_3 = 16
    scalar_token_1 = module_1.ScalarToken(str_1, int_2, int_3, str_1)
    int_4 = 1
    str_2 = '"foo"'
    token_0 = module_0.tokenize_json(str_2)
    scalar_token_2 = module_1.ScalarToken(str_0, int_4, int_0, str_0)
    str_3 = '[]'
    token_1 = module_0.tokenize_json(str_3)
    var_0 = []
    str_4 = ''
    list_token_0 = module_1.ListToken(var_0, int_4, int_4, str_4)
    str_5 = 'null'
    token_2 = module_0.tokenize_json(str_5)
    var_1 = None
    scalar_token_3 = module_1.ScalarToken(var_1, int_4, int_0, str_5)

def test_case_6():
    str_0 = '\n    {\n    "name" :"Python",\n    "age": 26\n    }\n    '
    token_0 = module_0.tokenize_json(str_0)
    var_0 = print(token_0)