# Automatically generated by Pynguin.
import dataclasses_json.cfg as module_0
import dataclasses_json.undefined as module_1

def test_case_0():
    try:
        str_0 = 'n\t+N3#y*\x0b-9S2=~|4'
        dict_0 = module_0.config(undefined=str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'n\t+N3#y*\x0b-9S2=~|4'
        dict_0 = module_0.config(undefined=str_0, field_name=str_0, exclude=str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'exclude'
        dict_0 = module_0.config(undefined=str_0)
        str_1 = '\r'
        list_0 = []
        bytes_0 = b'\xa76GdZ*\xb6f\xee\xeb\x9a'
        dict_1 = module_0.config(encoder=bytes_0)
        optional_0 = None
        dict_2 = module_0.config(decoder=list_0, letter_case=list_0, undefined=str_1, exclude=optional_0)
    except BaseException:
        pass

def test_case_3():
    try:
        global_config_0 = module_0._GlobalConfig()
        str_0 = 'hG9..\x0biZQI$1K1=d=s4X'
        dict_0 = {str_0: str_0, str_0: global_config_0, str_0: str_0}
        dict_1 = module_0.config(undefined=dict_0, field_name=str_0)
        undefined_0 = module_1.Undefined.EXCLUDE
        exclude_0 = module_0.Exclude()
        var_0 = exclude_0.<lambda>(undefined_0)
    except BaseException:
        pass