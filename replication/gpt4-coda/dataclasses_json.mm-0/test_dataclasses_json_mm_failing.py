# Automatically generated by Pynguin.
import dataclasses_json.mm as module_0

def test_case_0():
    try:
        int_0 = 1253
        str_0 = 'j'
        dict_0 = {str_0: int_0}
        timestamp_field_0 = module_0._TimestampField(attribute=str_0, **dict_0)
        union_field_0 = module_0._UnionField(dict_0, timestamp_field_0, dict_0)
        var_0 = module_0.build_type(int_0, str_0, union_field_0, union_field_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        schema_f_0 = module_0.SchemaF(**dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytearray_0 = None
        tuple_0 = ()
        int_0 = -1682
        var_0 = module_0.schema(bytearray_0, tuple_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        type_0 = None
        bool_0 = False
        str_0 = None
        str_1 = '\rST(_~P'
        str_2 = "\n    Because JSON object keys must be strs, we need the extra step of decoding\n    them back into the user's chosen python type\n    "
        str_3 = 'undefined'
        dict_0 = {str_0: str_0, str_1: str_2, str_0: str_3}
        timestamp_field_0 = module_0._TimestampField(missing=type_0, required=bool_0, load_only=bool_0, error_messages=dict_0)
        float_0 = 2088.494411
        var_0 = None
        list_0 = [float_0, var_0]
        type_1 = module_0.build_schema(type_0, timestamp_field_0, list_0, dict_0)
    except BaseException:
        pass