# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0

def test_case_0():
    str_0 = 'JSONSchema'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_1():
    str_0 = 'name: John Doe\nage: 30'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_2():
    bytes_0 = b'\xa6~\xcf'
    token_0 = module_0.tokenize_yaml(bytes_0)

def test_case_3():
    str_0 = 'key: value\nlist:\n  - item1\n  - item2'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_4():
    str_0 = 'on'
    token_0 = module_0.tokenize_yaml(str_0)