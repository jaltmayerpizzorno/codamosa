# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        str_0 = '&rANq;$%'
        token_0 = module_0.tokenize_yaml(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b''
        any_0 = module_0.validate_yaml(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xa0y>PR\x9dS<\x8f\xc0\xc9v\\K\x9b'
        any_0 = module_0.validate_yaml(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x94\xb8R\xd6\xa8%O\xbd\x03\xcd\x8b\xd5C\x13\xc3\x01\xa8\xf8'
        any_0 = module_0.validate_yaml(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'hello'
        token_0 = module_0.tokenize_yaml(bytes_0)
        str_0 = '1'
        token_1 = module_0.tokenize_yaml(str_0)
        str_1 = '1.0'
        token_2 = module_0.tokenize_yaml(str_1)
        str_2 = 'true'
        token_3 = module_0.tokenize_yaml(str_2)
        str_3 = 'false'
        token_4 = module_0.tokenize_yaml(str_3)
        str_4 = '1\n2\n3'
        token_5 = module_0.tokenize_yaml(str_4)
        str_5 = '{ a: 1 }'
        token_6 = module_0.tokenize_yaml(str_5)
        str_6 = '[{ a: 1 }]'
        token_7 = module_0.tokenize_yaml(str_6)
        bool_0 = False
        field_0 = module_1.Field(allow_null=bool_0)
        any_0 = module_0.validate_yaml(bytes_0, field_0)
    except BaseException:
        pass