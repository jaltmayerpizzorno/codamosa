# Automatically generated by Pynguin.
import dataclasses_json.cfg as module_0
import marshmallow.fields as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xb2\x89\x17x\t'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = []
    dict_1 = {}
    dict_2 = module_0.config(encoder=bytes_0, decoder=dict_0, mm_field=list_0, letter_case=dict_1)

def test_case_2():
    int_0 = 5
    dict_0 = {int_0: int_0, int_0: int_0}
    bool_0 = True
    field_0 = module_1.Field(load_default=bool_0, dump_only=bool_0)
    str_0 = '"ai#^Sd0={=kr}HyDi,('
    str_1 = 'M@{e2,\x0cq^dF*'
    dict_1 = {str_0: str_0, str_1: str_0}
    str_2 = '-P 3\\:l^G!X097{'
    dict_2 = module_0.config(dict_0, encoder=bool_0, decoder=field_0, letter_case=dict_1, field_name=str_2)

def test_case_3():
    callable_0 = None
    str_0 = 'KL2]\n'
    dict_0 = module_0.config(encoder=callable_0, exclude=str_0)