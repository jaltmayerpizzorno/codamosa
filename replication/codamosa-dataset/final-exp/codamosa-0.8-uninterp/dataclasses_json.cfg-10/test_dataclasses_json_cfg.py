# Automatically generated by Pynguin.
import dataclasses_json.cfg as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '76`V\\K|=f-<;T'
    dict_0 = {}
    dict_1 = module_0.config(field_name=str_0, exclude=dict_0)

def test_case_2():
    str_0 = '76`V\\K|=f-<;T'
    bytes_0 = b'\x1f\x96\xf7$\xfe\xd7sE\x9e\x1d0)\xb6\x93^>'
    global_config_0 = module_0._GlobalConfig()
    dict_0 = module_0.config(encoder=bytes_0, letter_case=global_config_0, field_name=str_0)

def test_case_3():
    dict_0 = module_0.config()
    str_0 = 'Object'
    str_1 = 'name'
    str_2 = 'type'
    str_3 = {str_1: str_0, str_2: str_1}
    str_4 = {str_0: str_3}
    str_5 = 'encoder'
    str_6 = {str_1: str_5}
    str_7 = 'decoder'
    str_8 = {str_1: str_7}
    str_9 = 'mm_field'
    str_10 = {str_1: str_9}
    str_11 = 'letter_case'
    str_12 = {str_1: str_11}
    str_13 = 'RAISE'
    str_14 = {str_1: str_4}
    dict_1 = module_0.config(str_4, encoder=str_6, decoder=str_8, mm_field=str_10, letter_case=str_12, undefined=str_13, exclude=str_14)