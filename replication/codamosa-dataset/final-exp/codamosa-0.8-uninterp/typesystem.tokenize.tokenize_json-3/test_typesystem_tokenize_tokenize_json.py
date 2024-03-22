# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0

def test_case_0():
    str_0 = '{"Line1":"Line1 Val","Line2":"Line2 Val","Line3":"Line3 Val","Line4":"Line4 Val"}'
    token_0 = module_0.tokenize_json(str_0)

def test_case_1():
    str_0 = '\n    {\n      "firstName": "John",\n      "lastName": "Smith",\n      "isAlive": true,\n      "age": 25,\n      "address": {\n        "streetAddress": "21 2nd Street",\n        "city": "New York",\n        "state": "NY",\n        "postalCode": "10021-3100"\n      },\n      "phoneNumbers": [\n        {\n          "type": "home",\n          "number": "212 555-1234"\n        },\n        {\n          "type": "office",\n          "number": "646 555-4567"\n        }\n      ],\n      "children": [],\n      "spouse": null\n    }\n    '
    token_0 = module_0.tokenize_json(str_0)

def test_case_2():
    str_0 = '{"hello": [1, 2.5, "text", true, null, false]}'
    token_0 = module_0.tokenize_json(str_0)

def test_case_3():
    str_0 = '\n    {\n        "name": "Steve",\n        "age": "old",\n        "address": {\n            "street": "some street",\n            "city": {\n                "id": 1,\n                "name": "Sofia"\n            }\n        }\n    }'
    token_0 = module_0.tokenize_json(str_0)

def test_case_4():
    bytes_0 = b'{"a" : true}'
    token_0 = module_0.tokenize_json(bytes_0)
    str_0 = '{"a" : true}'
    bytes_1 = b'{"a" : true, "b" : false, "c" : 1.0}'
    token_1 = module_0.tokenize_json(bytes_1)
    token_2 = module_0.tokenize_json(str_0)
    bytes_2 = b'{"a" : [1, 2, 3]}'
    token_3 = module_0.tokenize_json(bytes_2)
    token_4 = module_0.tokenize_json(bytes_0)