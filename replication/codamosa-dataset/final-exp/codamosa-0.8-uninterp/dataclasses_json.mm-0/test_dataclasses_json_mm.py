# Automatically generated by Pynguin.
import dataclasses_json.mm as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 5
    timestamp_field_0 = module_0._TimestampField(default=int_0)
    var_0 = timestamp_field_0.deserialize(int_0)

def test_case_2():
    iso_field_0 = module_0._IsoField()
    str_0 = '2017-11-12T15:07'
    var_0 = iso_field_0.deserialize(str_0)