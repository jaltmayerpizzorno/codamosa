# Automatically generated by Pynguin.
import dataclasses_json.mm as module_0
import typing as module_1
import builtins as module_2

def test_case_0():
    try:
        schema_f_0 = None
        str_0 = 'No field of type dataclasses_json.CatchAll defined'
        str_1 = 'VKC!2`2FO'
        dict_0 = {str_0: str_1, str_1: str_0}
        dict_1 = {str_1: str_0}
        iso_field_0 = module_0._IsoField(load_default=schema_f_0, missing=schema_f_0, error_messages=dict_0, metadata=dict_1)
        bytes_0 = b'b\xb7\xe9\xe7zk\xcdNw\xf4'
        dict_2 = {str_1: str_1, str_1: bytes_0, bytes_0: dict_1}
        timestamp_field_0 = module_0._TimestampField(validate=dict_2, **dict_1)
        bool_0 = True
        list_0 = []
        tuple_0 = (iso_field_0, bool_0, list_0)
        union_field_0 = module_0._UnionField(timestamp_field_0, bool_0, tuple_0)
        str_2 = 'c=0lUf2,'
        dict_3 = {str_2: timestamp_field_0, str_2: dict_2}
        var_0 = module_0.build_type(union_field_0, dict_3, dict_3, iso_field_0, union_field_0)
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
        str_0 = 'Unknown1[ype'
        type_var_0 = module_1.TypeVar(str_0)
        var_0 = module_0.build_type(type_var_0, type_var_0, type_var_0, type_var_0, type_var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        bytearray_0 = module_2.bytearray()
        list_0 = [bool_0, bytearray_0]
        str_0 = ';)j!bzTxt<r'
        str_1 = ' that is not an instance of dataclass_json. Did you mean to recursively serialize this field? If so, make sure to augment '
        str_2 = None
        str_3 = '_TVYFVeta+h=Y!>*T-{D'
        str_4 = 'R, LD|3*::+A<>"hP'
        dict_0 = {str_0: str_1, str_2: str_0, str_0: str_3, str_2: str_4}
        tuple_0 = None
        var_0 = module_0.schema(list_0, dict_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        type_0 = None
        bool_0 = False
        bytes_0 = b'\xba\xc5\x8e\xc2\xf2DW_\xe9\xfa\xfd8Z\x1d\xce'
        str_0 = 'uz65Nf%fc\th'
        str_1 = 'letter_case'
        dict_0 = {str_0: str_1}
        type_1 = module_0.build_schema(type_0, bool_0, bytes_0, dict_0)
    except BaseException:
        pass