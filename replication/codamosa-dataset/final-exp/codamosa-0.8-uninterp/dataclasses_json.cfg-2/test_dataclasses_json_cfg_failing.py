# Automatically generated by Pynguin.
import dataclasses_json.cfg as module_0
import marshmallow.fields as module_1

def test_case_0():
    try:
        str_0 = 'Us8od?AN?[*"'
        dict_0 = module_0.config(undefined=str_0, field_name=str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'YJw7)/'
        callable_0 = None
        bool_0 = False
        dict_0 = module_0.config(decoder=callable_0, field_name=str_0, exclude=bool_0)
        dict_1 = module_0.config(field_name=str_0)
        global_config_0 = module_0._GlobalConfig()
        global_config_1 = module_0._GlobalConfig()
        dict_2 = module_0.config(encoder=callable_0, undefined=str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'YJw7)/'
        dict_0 = module_0.config(field_name=str_0)
        dict_1 = {str_0: str_0, str_0: str_0}
        dict_2 = None
        field_0 = module_1.Field(missing=str_0, dump_default=str_0, data_key=str_0, attribute=str_0, **dict_1)
        dict_3 = module_0.config(encoder=dict_2, mm_field=field_0, undefined=str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '{rD@|,u'
        dict_0 = module_0.config(encoder=str_0, undefined=str_0, field_name=str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Us8od?AN?[*"'
        dict_0 = module_0.config()
        dict_1 = module_0.config(undefined=str_0, field_name=str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        global_config_0 = module_0._GlobalConfig()
        bool_0 = True
        str_0 = 'GP0|4k}RmcG'
        tuple_0 = (str_0,)
        dict_0 = module_0.config(bool_0, mm_field=tuple_0, field_name=str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'owO'
        dict_0 = module_0.config(undefined=str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '__supertype__'
        str_1 = 'w1I'
        str_2 = '*iQKs;T'
        str_3 = 'LqzI,:EHR<*O3&"'
        str_4 = '\n        Returns a 2 dictionaries: defined and undefined parameters\n        '
        str_5 = None
        dict_0 = {str_0: str_0, str_1: str_2, str_3: str_4, str_5: str_0}
        dict_1 = {str_1: str_5, str_0: str_5, str_0: dict_0, str_0: str_2}
        bool_0 = True
        field_0 = module_1.Field(dump_default=str_1, default=str_1, attribute=str_2, allow_none=bool_0)
        float_0 = -2216.8
        dict_2 = module_0.config(decoder=dict_1, mm_field=field_0, letter_case=float_0, field_name=str_2)
        bool_1 = True
        bool_2 = False
        bool_3 = False
        field_1 = module_1.Field(dump_default=dict_0, default=str_1, attribute=str_1, validate=bool_1, required=bool_2, allow_none=bool_3, error_messages=dict_0, metadata=dict_0)
    except BaseException:
        pass