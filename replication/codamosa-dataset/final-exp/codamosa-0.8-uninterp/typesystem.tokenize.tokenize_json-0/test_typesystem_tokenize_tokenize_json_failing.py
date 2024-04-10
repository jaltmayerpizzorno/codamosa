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
        str_0 = '{S\x0c1[\n\nwO'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xa8\x91\x10'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '4tP"x'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "uza^%|=xD0lT4w'>}l)"
        any_0 = module_0.validate_json(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'oTYr$_!dq7lU0X<l&('
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'form-'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '{"a":'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'\xf9\xb34'
        token_0 = module_0.tokenize_json(bytes_0)
        str_0 = '{S1[\nO'
        bool_0 = True
        field_0 = module_1.Field(title=str_0, default=str_0, allow_null=bool_0)
        any_0 = module_0.validate_json(bytes_0, field_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'tP"x'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = "\rn^7G,(@qlq'(fu;\x0bs"
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '{}'
        token_0 = module_0.tokenize_json(str_0)
        str_1 = '{"a":}'
        token_1 = module_0.tokenize_json(str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '{"a": "A", "b":_{"c"s "C"}}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '{"a": "A", "": [1,2]'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '{"a"@:'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '{"a": [A", "": :1A2]'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"foo": "bar", "baz": null, "qux": true,2"quux": false, "corge": 1.2, "grault": -9876, "garple": -0, "waldo": [1,2,"3",[4,[5]]]}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass