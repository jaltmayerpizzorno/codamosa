# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = "\n    field1: '1'\n    field2:\n        -\n            field3: '3'\n            field4: '4'\n        -\n            field5: true\n            field6: false\n    "
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_2():
    str_0 = '&70'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_3():
    str_0 = '6'
    token_0 = module_0.tokenize_yaml(str_0)