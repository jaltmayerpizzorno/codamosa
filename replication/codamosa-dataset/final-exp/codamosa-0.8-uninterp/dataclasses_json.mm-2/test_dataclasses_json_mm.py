# Automatically generated by Pynguin.
import dataclasses_json.mm as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    str_0 = 'jxLH%Z'
    dict_0 = {str_0: str_0}
    timestamp_field_0 = module_0._TimestampField(dump_only=bool_0, error_messages=dict_0)
    dict_1 = {str_0: bool_0, str_0: dict_0, str_0: dict_0}
    var_0 = timestamp_field_0.deserialize(bool_0, **dict_1)