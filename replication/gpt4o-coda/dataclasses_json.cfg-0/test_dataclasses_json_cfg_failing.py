# Automatically generated by Pynguin.
import dataclasses_json.cfg as module_0

def test_case_0():
    try:
        bytes_0 = b'\xb1'
        str_0 = '*\n_-\\PL\r)'
        dict_0 = module_0.config(letter_case=bytes_0, undefined=str_0, field_name=str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '*%\n_-\\P\r)'
        dict_0 = module_0.config(mm_field=str_0, undefined=str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        optional_0 = None
        tuple_0 = ()
        str_0 = ')lT1O'
        dict_0 = module_0.config(encoder=optional_0, decoder=tuple_0, letter_case=str_0, undefined=str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        exclude_0 = module_0.Exclude()
        str_0 = ''
        bool_0 = False
        dict_0 = module_0.config(str_0, mm_field=bool_0, field_name=str_0)
    except BaseException:
        pass