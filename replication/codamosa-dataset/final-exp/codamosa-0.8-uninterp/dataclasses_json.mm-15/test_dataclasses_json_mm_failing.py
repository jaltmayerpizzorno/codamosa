# Automatically generated by Pynguin.
import dataclasses_json.mm as module_0
import builtins as module_1
import decimal as module_2

def test_case_0():
    try:
        schema_f_0 = module_0.SchemaF()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\r\xd3'
        str_0 = 'VfxE$o;,=&]^k'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.build_type(bytes_0, str_0, bytes_0, dict_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\nx8Vs2=r9:9'
        int_0 = 2094
        bool_0 = False
        bool_1 = False
        dict_0 = {}
        timestamp_field_0 = module_0._TimestampField(attribute=str_0, required=bool_0, dump_only=bool_1, **dict_0)
        var_0 = module_0.schema(str_0, int_0, timestamp_field_0)
    except BaseException:
        pass

def test_case_3():
    try:
        type_0 = None
        float_0 = 1304.478
        dict_0 = {type_0: float_0}
        bool_0 = False
        schema_f_0 = None
        type_1 = module_0.build_schema(type_0, dict_0, bool_0, schema_f_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        str_0 = 'x_*\x0b\nJ&da2e\t\\$'
        str_1 = None
        str_2 = '`)7`}hhURu+x?'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_2}
        bytes_0 = b'\x17Tu;'
        list_0 = [bytes_0]
        var_0 = None
        list_1 = [var_0, var_0, var_0]
        union_field_0 = module_0._UnionField(list_0, dict_0, list_1)
        str_3 = '+I\r'
        str_4 = 'f'
        dict_1 = {str_1: str_3, str_3: str_1, str_1: str_4, str_3: str_2}
        var_1 = module_0.build_type(bool_0, str_0, bytes_0, dict_0, dict_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        bytes_0 = b'\xee}-fdK/\xdfwx\x12\x1c\xec\x04`\xf2'
        str_0 = 'Oxclu'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [dict_0]
        type_0 = module_1.type(*list_0)
        dict_1 = {}
        decimal_0 = module_2.Decimal()
        tuple_0 = (dict_1, decimal_0)
        str_1 = '^m>Q|]m\x0bUV;#FA{8\n'
        str_2 = 'MwQB\\B#%n2\n@t>)Fl'
        str_3 = 'h^s`r5ye38xOX>x'
        dict_2 = {str_1: bytes_0, str_2: bytes_0, str_3: dict_0, str_2: bool_0}
        str_4 = 'UBy'
        dict_3 = {str_4: str_3}
        complex_0 = None
        var_0 = module_0.build_type(type_0, tuple_0, dict_2, dict_3, complex_0)
    except BaseException:
        pass