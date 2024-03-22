# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        bytes_0 = b'\xcf\x8f\xd6EC\xe5I#\xd6\x85o\xf0'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '0P7&s2*5`F'
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
        bytes_0 = b'\xb4'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '{"ame":"test","age":12,"details":{"heiht":5.5,"weighg":12.5}'
        field_0 = module_1.Field(title=str_0, default=str_0)
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'tB'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'non-existent-file'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Must be greater than or equal to {minimum}.'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'f=\xeb\xf8\x8c\xfd\x95\xa9\x10\xcd*\xf6\x04:p\x8f'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '{KG#*Qu9A-rum. \tl\n'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '['
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'\xf7\xdd5'
        token_0 = module_0.tokenize_json(bytes_0)
        field_0 = None
        any_0 = module_0.validate_json(bytes_0, field_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '{\tr2a||x'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'true'
        field_0 = module_1.Field(title=str_0)
        field_1 = None
        any_0 = module_0.validate_json(str_0, field_1)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'["TEST", {"TEST" "TEST"}'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '[{"a": "b"}, {}]'
        token_0 = module_0.tokenize_json(str_0)
        int_0 = 0
        var_0 = token_0.value[int_0]
        str_1 = 'a'
        var_1 = token_0.value[int_0]
        var_2 = var_1.value[str_1]
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '{"ame":"test","age":1,details":{"eiht":5.5,"weighg":12.5}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"name":"test","age":12,"details":{"height":5.,"weight":12.5}}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '{"foo": [1, 2, %]}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '{"foo%": D[1, 2 3]}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '{"ame":"test","age":12,"details":{"heiht":5.5,"weighg":12.5}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass