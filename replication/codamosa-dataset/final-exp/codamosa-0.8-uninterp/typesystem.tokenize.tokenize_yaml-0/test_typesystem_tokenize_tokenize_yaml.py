# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '_target'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_2():
    str_0 = '\n    name: John Doe\n    age: 50\n    address:\n        street: University Sreet\n        city: Boston\n        zipcode: 12345\n    favorite_foods:\n    - Pizza\n    - Pasta\n    - Bacon\n    '
    token_0 = module_0.tokenize_yaml(str_0)