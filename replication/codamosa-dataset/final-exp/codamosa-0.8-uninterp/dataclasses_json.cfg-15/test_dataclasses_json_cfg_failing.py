# Automatically generated by Pynguin.
import dataclasses_json.cfg as module_0
import dataclasses_json.undefined as module_1

def test_case_0():
    try:
        str_0 = 'My1N1WVdE(JQ$#w3'
        dict_0 = module_0.config(letter_case=str_0, undefined=str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        dict_0 = {}
        str_1 = 'B'
        float_0 = 343.734291
        float_1 = 1580.9
        dict_1 = {str_0: dict_0, str_1: dict_0}
        global_config_0 = module_0._GlobalConfig()
        bytes_0 = b'\xb4o\xdc\x1b\x06_gJ\xef\xb1Ok}l\x16\x1f'
        list_0 = [str_1, float_0, bytes_0, float_1]
        dict_2 = {}
        dict_3 = module_0.config(dict_1, encoder=global_config_0, decoder=bytes_0, mm_field=list_0, undefined=str_1, exclude=dict_2)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'B'
        global_config_0 = module_0._GlobalConfig()
        none_type_0 = None
        none_type_1 = None
        dict_0 = module_0.config(none_type_0, letter_case=none_type_1, undefined=str_0, field_name=str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        exclude_0 = module_0.Exclude()
        undefined_0 = module_1.Undefined.EXCLUDE
        dict_0 = module_0.config(undefined=undefined_0)
        var_0 = exclude_0.<lambda>(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        global_config_0 = module_0._GlobalConfig()
        str_0 = '[,E\rs?YmZU^{]HLwa4'
        int_0 = 554
        dict_0 = module_0.config(letter_case=global_config_0, field_name=str_0, exclude=int_0)
        str_1 = '+Ca'
        bytes_0 = b'\xfb[\r\xe2\xa5^$\xed'
        dict_1 = module_0.config(encoder=bytes_0, field_name=str_1, exclude=str_1)
        global_config_1 = module_0._GlobalConfig()
        dict_2 = module_0.config(undefined=str_1, field_name=str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'exclude'
        bytes_0 = b'\xfb[\r\xe2\xa5^$\xed'
        dict_0 = module_0.config(encoder=bytes_0, field_name=str_0, exclude=str_0)
        dict_1 = module_0.config(undefined=str_0, field_name=str_0)
        dict_2 = {str_0: str_0}
        dict_3 = module_0.config(letter_case=dict_2)
        exclude_0 = module_0.Exclude()
        var_0 = exclude_0.<lambda>(exclude_0)
    except BaseException:
        pass