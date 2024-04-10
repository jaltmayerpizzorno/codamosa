# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        str_0 = 'C'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '5Zq=Z'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tokenizing_decoder_0 = module_0._TokenizingDecoder()
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xcbl\x9aX\xea\x02y\xcd'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b''
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '{'
        field_0 = module_1.Field()
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'n'
        field_0 = module_1.Field()
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '{\n        "key1": "value1",\n        "key2": 2,\n        "key3": true,\n        "key4": flse,\n        "key5": null,\n        "key6":{\n            "key7": "value7"\n        },\n        "key8": ["item1", "item2", "item3"],\n        "key9": 3.14,\n        "key10": [\n            {\n                "key11": "value11"\n            },\n            {\n                "key12"D "value12"\n d        x }\n        ],\n        "key13": [\n            [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n        ]\n    }'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '{'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '0'
        field_0 = module_1.Field()
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '{\n        "key1": "value1",\n        "key2":2,\n        "key3": tr(e,\n        "key4": flse,\n        "key5": null,\n        "key6":{\n            "key7": "value7"\n        },\n        "key8": ["item1", "item2", "item3"],\n        "key9": 3.14,\n        "key10": [\n            {\n               "key11": "value11"\n            },\n            {\n                "key12"D "value12"\n d        x }\n        ],\n        "key13": [\n            [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n        ]\n    }'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '{"a": 5"b"}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '1.123e1.+1'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '{"a":5""}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '{\n        "key1": "value1",\n        "key2": 2,\n        "key3": true,\n        "key4": false,\n        "key5": null,\n        "key6": {\n            "key7": "value7"\n        },\n        "key8": ["item1", "item2", "item3"],\n        "key9": 3.14,\n        "key10": [\n            {\n                "key11": "value11"\n            },\n            {\n                "key12"D "value12"\n d        x }\n        ],\n        "key13": [\n            [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n        ]\n    }'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '{\n        "key1": "value1",\n        "key2": 2,\n        "key3": true,\n        "key4": false,\n        "key5": null,\n        "key6": {\n            "key7": "value7"\n        },\n        key8": ["item1", "item2", "item3"],\n        "key9": 3.14,\n        "key10": [\n            {\n                "key11": "value11"\n            },\n            {\n                "key12"D "value12"\n d        x }\n        ],\n        "key13": [\n            [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n        ]\n    }'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '{"": "b"'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{\n        "key1": "value1",\n        "key2": 2,\n        "key3": true,\n        "key4": false,\n        "key5": null,\n        "key6": {\n            "key7": \nvalue7"\n        },\n        "key8": ["item1", "item2", "item3"],\n        "key9": 3.14,\n        "key10": [\n            {\n                "key11": "value11"\n            },\n            {\n                "key12"D "value12"\n d        x }\n        ],\n        "key13":r[\n            [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n        ]\n    }'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '{"a": 1}'
        token_0 = module_0.tokenize_json(str_0)
        str_1 = '{"a": 1.0}'
        token_1 = module_0.tokenize_json(str_1)
        str_2 = '{"a": 1e10}'
        token_2 = module_0.tokenize_json(str_2)
        str_3 = '{"a": null}'
        token_3 = module_0.tokenize_json(str_3)
        str_4 = '{"a":tue}'
        token_4 = module_0.tokenize_json(str_4)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '['
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass