# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        tokenizing_decoder_0 = module_0._TokenizingDecoder()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'{\xd4\x02X\xab\xe9\x9c'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '=@8)\r1N8i!0!9\\6e`}%'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '8;0i|\tvyk_'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'test_tokenize_json()'
        var_0 = print(str_0)
        str_1 = '{"test": "Hello"}'
        token_0 = module_0.tokenize_json(str_1)
        var_1 = print(token_0)
        str_2 = ''
        token_1 = module_0.tokenize_json(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x9e\xa8{udR'
        field_0 = module_1.Field()
        any_0 = module_0.validate_json(bytes_0, field_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'f\x03g&PH\x93\x85\x7f,\x83g\xe2c\xf5\xf8\xd0\xa4\xd0'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\n3E29'
        token_0 = module_0.tokenize_json(str_0)
        any_0 = module_0.validate_json(str_0, token_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'['
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'then'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'{\t\x02X\xab\xe9\x17p\x9c'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'nC]0N9HZ|E`'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '{"name": "J\'hn", "age": 3G}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '{"name": CJ\'hn", "age": 3G}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '{"tameS: "J\'hn", "a~e": 3G}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '{"nae": "Jhn", "[":}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '{"nae": "Jhn", ag": G}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"name": \nJ\'hn", "a^e"R 3G}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '\n3E29'
        token_0 = module_0.tokenize_json(str_0)
        str_1 = '{"na": "Jhn, \ra[": G}'
        token_1 = module_0.tokenize_json(str_1)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '{"fruits": ["apple", "orangq"]'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass