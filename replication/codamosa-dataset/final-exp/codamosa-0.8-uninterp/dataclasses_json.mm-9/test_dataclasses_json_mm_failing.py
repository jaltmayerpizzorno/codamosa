# Automatically generated by Pynguin.
import marshmallow.fields as module_0
import builtins as module_1
import dataclasses_json.mm as module_2

def test_case_0():
    try:
        integer_0 = module_0.Integer()
        str_0 = 'dqLO-y'
        bytearray_0 = module_1.bytearray()
        list_0 = []
        union_field_0 = module_2._UnionField(str_0, bytearray_0, list_0)
        list_1 = None
        var_0 = module_2.build_type(integer_0, integer_0, list_1, list_1, list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        schema_f_0 = module_2.SchemaF()
    except BaseException:
        pass

def test_case_2():
    try:
        integer_0 = module_0.Integer()
        list_0 = None
        var_0 = module_2.build_type(integer_0, integer_0, list_0, list_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'i\xbe/\x15u\xf1X\x1c~'
        bool_0 = False
        int_0 = -63
        tuple_0 = (bool_0, int_0)
        dict_0 = {bytes_0: bytes_0, int_0: bytes_0, tuple_0: tuple_0, bytes_0: bool_0}
        str_0 = '>X9G\\@n:X\x0b'
        str_1 = '|d'
        str_2 = '#oK=oGz97,Cl>;IzDYz|'
        bytes_1 = b'?\x9d&\xb2\xc6\xfa\xb0\x0e\x0c\xc7\xd2\x96\xa6\x1c\xd4'
        dict_1 = {str_0: int_0, str_1: tuple_0, str_2: bytes_1}
        tuple_1 = (bytes_0, tuple_0, dict_0, dict_1)
        bytearray_0 = module_1.bytearray()
        var_0 = module_2.schema(tuple_1, str_1, bytearray_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -3968
        str_0 = 'F<u]td\t<AST'
        str_1 = ''
        str_2 = ' detected when decoding '
        str_3 = ')&Xy? S\x0b'
        str_4 = '29D pI+}bsmYuIdNZ1BR'
        dict_0 = {str_1: str_2, str_3: str_4}
        none_type_0 = None
        timestamp_field_0 = module_2._TimestampField(attribute=str_0, error_messages=dict_0, metadata=none_type_0)
        bool_0 = True
        type_0 = module_2.build_schema(int_0, str_0, timestamp_field_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        integer_0 = module_0.Integer()
        dict_0 = {}
        list_0 = None
        list_1 = [dict_0]
        type_0 = module_1.type(*list_1)
        tuple_0 = ()
        str_0 = None
        list_2 = None
        var_0 = module_2.build_type(type_0, tuple_0, str_0, list_0, list_2)
    except BaseException:
        pass