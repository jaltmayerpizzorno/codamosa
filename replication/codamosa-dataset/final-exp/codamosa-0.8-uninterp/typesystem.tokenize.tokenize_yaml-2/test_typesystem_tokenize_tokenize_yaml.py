# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '---\n    foo:\n        bar: baz\n    '
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_2():
    str_0 = 'Pu^M4:`'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_3():
    str_0 = '9%KMZo390Ky:'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_4():
    bytes_0 = b'\n        title: "title"\n        description: "description"\n        body: "body"\n        tags:\n          - tag1\n          - tag2\n          - tag3\n        '
    token_0 = module_0.tokenize_yaml(bytes_0)

def test_case_5():
    str_0 = "\n    version: 1.0\n    name: 'Foo Bar'\n    "
    token_0 = module_0.tokenize_yaml(str_0)