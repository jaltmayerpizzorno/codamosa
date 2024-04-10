# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0
import typesystem.tokenize.tokens as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xea\xea\xf13\xc5\xad\x8e'
    token_0 = module_0.tokenize_yaml(bytes_0)

def test_case_2():
    str_0 = '\n        a: 1\n        b: 2\n        c: 3\n    '
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_3():
    str_0 = 'patient: {type: patient, name: John}'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_4():
    str_0 = '{"key1":"string","key2":42,"key3":[4,2]}'
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_5():
    str_0 = '\n    name: aaaaa\n    value: 10\n    a: yes\n    b: true\n    d: [1,2,3]\n    e: [{a: a}, {a: b}]\n    '
    token_0 = module_0.tokenize_yaml(str_0)

def test_case_6():
    str_0 = '---\n\n3\n'
    token_0 = module_0.tokenize_yaml(str_0)
    int_0 = 3
    int_1 = [int_0]
    int_2 = 1
    int_3 = 5
    list_token_0 = module_1.ListToken(int_1, int_2, int_3)
    str_1 = '---\n\n3.5\n'
    token_1 = module_0.tokenize_yaml(str_1)
    float_0 = 3.5
    float_1 = [float_0]
    list_token_1 = module_1.ListToken(float_1, int_2, int_3)
    str_2 = '---\n\ntrue\n'
    token_2 = module_0.tokenize_yaml(str_2)
    bool_0 = True
    bool_1 = [bool_0]
    list_token_2 = module_1.ListToken(bool_1, bool_0, int_3)
    str_3 = '---\n\nfalse\n'
    token_3 = module_0.tokenize_yaml(str_3)
    bool_2 = False
    bool_3 = [bool_2]
    list_token_3 = module_1.ListToken(bool_3, bool_0, int_3)
    str_4 = '---\n\nnull\n'
    token_4 = module_0.tokenize_yaml(str_4)
    var_0 = None
    var_1 = [var_0]
    list_token_4 = module_1.ListToken(var_1, bool_0, int_3)
    str_5 = '---\n\n- 1\n  - 2\n'
    token_5 = module_0.tokenize_yaml(str_5)
    int_4 = 2
    var_2 = [bool_0, int_4]
    list_token_5 = module_1.ListToken(var_2, bool_0, int_3)