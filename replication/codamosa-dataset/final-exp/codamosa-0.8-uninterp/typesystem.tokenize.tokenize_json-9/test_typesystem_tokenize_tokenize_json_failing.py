# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        bytes_0 = b'\x96<8\xddd\xe7e'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '1E4\x0bkaRl)hH:D=`7'
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
        str_0 = '1E4\x0bkaRl)hH:D=`7'
        field_0 = module_1.Field()
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 't41h'
        str_1 = '{"f8o": "bar", "number": 1, "float": 3.333, "null": null}'
        token_0 = module_0.tokenize_json(str_1)
        token_1 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'f\x19牒bz'
        str_1 = '1z;MXg-Q'
        bool_0 = False
        field_0 = module_1.Field(description=str_1, allow_null=bool_0)
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '{"-oo":"bar", "number": 1, "float": 3.333, "null": nul}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = ''
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'false'
        str_1 = '1?('
        field_0 = module_1.Field(description=str_1, default=str_0)
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '\n    {\n      "level1": {\n          "level2": [\n      m       "level3_value0",\n              "level3_value1",\n              ".evel3_value2"\n          ]\n      }\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = "{'a': '1', 'b': '2}"
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '\n    {\n      "level1": {\n          "level2": [\n             "level3_value0",\n              "level3_value1",\n              "level3_value2"\n          ]\n      \n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\n    {\n      "level1": {\n          "level2"7 [\n      m       "level3_value0",\n              "level3_value1",\n              ".evel3_value2"\n       xe ]\n      }\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '{"foo": "bar", "number": 1,v"float": 3.333, "null": null}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '\n    {\n      "level1": \n          "level2": [\n      m       "level3_vlue0",\n              "level3_value1",\n             9".evel3_value2"\n          ]\n      }\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '[\r'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass