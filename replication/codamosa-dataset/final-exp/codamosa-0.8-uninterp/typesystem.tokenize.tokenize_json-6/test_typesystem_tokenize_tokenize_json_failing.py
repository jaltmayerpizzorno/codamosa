# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0

def test_case_0():
    try:
        tokenizing_decoder_0 = module_0._TokenizingDecoder()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'3\xe4\xc0\x13B\x8b3\x0c4'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b's\xd2'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n    {\n        "numbers": [1, 2, -3],\n        "bools": [true, false],\n        "null": null,\n        "nested": {\n            "string": "Hello world",\n            "string_escapes": "\\"Wow\\"",\n            "unicode": "\\u00fc",\n            "int": 123,\n            "float": 123.45,\n            "exp": 1.23e+10\n        }\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
        bytes_0 = b''
        token_1 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}'
        any_0 = module_0.validate_json(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'ti\xa0'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'format'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '"'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'n\xc0q!\xde\x95\x13\xcfe|SK\xec\xd3\xfd\x01\xe9\xc7G\xa2'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\xc9{{\xa8('
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '{'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        type_0 = None
        bytes_0 = b'5'
        any_0 = module_0.validate_json(bytes_0, type_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '\n    {\n        "numbers": [1, 2, -3],\n        "bools": [true, false],\n        "null": ull,\n        "nested": {\n            "string": "Hello world",\n            "string_escapes": "\\"Wow\\"",\n            "unicode": "\\u00fc",\n            "int": 123,\n        $   "float": 123.45,\n            "exp": 1.23e+10\n        }\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\n    {\n        "numbers": [1, 2, -3],\n        "bools": [true, false],\n        "null": null,\n        "nested": {\n            "string": "Hello world",\n            "string_escapes": "\\"Wow\\"",\n            "unicode": "\\u00fc",\n            "int": 123,\n            "float": 123.45,\n          W "exp": 1.23e+10\n        }\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '\n    {\n        "numbers": [1, 2, -3],\n        "bools": [true, false],\n        "null":null,\n        "nested": {\n            "string": "Hello world",\n           "string_escapUs": "\\"Wow\\"",\n            "unic*de": "\\u00fc",\n          "int": 123,\n            "float": 123.A5,\n            Sexp": 1*23e+10\n        }\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '\n   {\n        "numbers": [1, 2, -3],\n        "bools": [true, false],\n        "null":null,\n        "nested": {\n            "string": "Hello world",\n            "string_escapUs": "\\"Wow\\"",            "unic*de": "\\u00fc",\n          "int" 123,\n            "float": 123.45,\n            Sexp": 1.23e+10\n        }\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b'{"child-key":{"child-array":[1,2,3],"child-dict":{"child-key":"child-val"}}'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '['
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass