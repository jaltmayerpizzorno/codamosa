# Automatically generated by Pynguin.
import dataclasses_json.cfg as module_0
import dataclasses_json.undefined as module_1

def test_case_0():
    try:
        str_0 = '-J^okH/whaq\\`>'
        dict_0 = module_0.config(undefined=str_0, field_name=str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2744
        int_1 = 3867
        str_0 = '_yPs+'
        dict_0 = module_0.config(letter_case=int_1, field_name=str_0)
        dict_1 = module_0.config(decoder=int_0, mm_field=str_0)
        str_1 = '\x0cONTL/'
        str_2 = 'n*|\x0b\r6?7ur/vMS{Oo#'
        dict_2 = {str_1: int_1, str_2: str_0, str_1: int_1, str_1: dict_1}
        exclude_0 = module_0.Exclude(**dict_2)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xa8q\xaa\xc2\x16b\x1a'
        str_0 = '^Sb'
        dict_0 = module_0.config(letter_case=bytes_0, field_name=str_0)
        dict_1 = {}
        str_1 = 'cls'
        dict_2 = {str_1: str_1, str_1: str_1, str_1: dict_1}
        exclude_0 = module_0.Exclude(**dict_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '-J^ok/whaq\\`>'
        dict_0 = module_0.config(encoder=str_0, undefined=str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ' that is not an instance of dataclass_json. Did you mean to recursively serialize this field? If so, make sure to augment '
        dict_0 = {}
        bytes_0 = b'q,\xbb-\xe5N\xda\xa6\x18\\\xb1\xf4\xe8JA\xaa"\xfak'
        dict_1 = module_0.config(decoder=dict_0, letter_case=bytes_0, undefined=str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        global_config_0 = module_0._GlobalConfig()
        dict_0 = {global_config_0: global_config_0}
        str_0 = '` EB[H'
        callable_0 = None
        dict_1 = module_0.config(dict_0, letter_case=callable_0, undefined=str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'A\\].O1Y0{9~%+@# 9Lt'
        dict_0 = module_0.config(undefined=str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = -3297.0
        global_config_0 = module_0._GlobalConfig()
        dict_0 = module_0.config(undefined=float_0)
        global_config_1 = module_0._GlobalConfig()
        exclude_0 = module_0.Exclude()
        global_config_2 = module_0._GlobalConfig()
        global_config_3 = module_0._GlobalConfig()
        dict_1 = None
        var_0 = exclude_0.<lambda>(dict_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '2y'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        global_config_0 = module_0._GlobalConfig()
        list_0 = [str_0, str_0, str_0]
        str_1 = 'decoder'
        undefined_0 = module_1.Undefined.RAISE
        float_0 = -4505.0
        set_0 = {str_0, undefined_0, global_config_0, undefined_0}
        dict_1 = module_0.config(dict_0, encoder=undefined_0, decoder=float_0, exclude=set_0)
        dict_2 = {str_1: str_0, str_1: list_0, str_1: str_1}
        exclude_0 = module_0.Exclude(*list_0, **dict_2)
    except BaseException:
        pass