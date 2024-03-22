# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2
import typesystem.composites as module_3

def test_case_0():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        iterator_0 = schema_definitions_0.__iter__()
        dict_0 = {iterator_0: iterator_0}
        str_0 = ' K'
        bool_0 = True
        field_0 = module_1.from_json_schema_type(dict_0, str_0, bool_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.ref_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.enum_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.const_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = None
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.all_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.any_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b"\n|vi\xc2\xe9\x0f\x91'A"
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.one_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_7():
    try:
        field_0 = module_2.Field()
        var_0 = module_1.to_json_schema(field_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'v`iccO-Q|Y'
        var_0 = module_1.to_json_schema(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        dict_0 = None
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.if_then_else_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_10():
    try:
        field_0 = module_2.Field()
        dict_0 = module_1.get_standard_properties(field_0)
        var_0 = module_1.to_json_schema(field_0)
    except BaseException:
        pass

def test_case_11():
    try:
        tuple_0 = None
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
        var_0 = module_1.to_json_schema(schema_definitions_0)
        dict_1 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
        dict_2 = {}
        schema_definitions_1 = module_0.SchemaDefinitions(**dict_2)
        field_0 = module_1.all_of_from_json_schema(dict_1, schema_definitions_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'UN=UcqkWH\x0b'
        str_1 = '27!\t\t^1UM'
        dict_0 = {str_0: str_0, str_1: str_0, str_1: str_0}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
        dict_1 = {}
        var_0 = module_1.to_json_schema(schema_definitions_0, dict_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'anyOf'
        str_1 = 'type'
        str_2 = {str_1: str_0}
        str_3 = [str_2]
        str_4 = {str_0: str_3}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.any_of_from_json_schema(str_4, schema_definitions_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'type'
        str_1 = 'enum'
        str_2 = 'number'
        str_3 = '1'
        str_4 = '2'
        str_5 = '3'
        str_6 = [str_3, str_4, str_5]
        str_7 = {str_0: str_2, str_1: str_6}
        var_0 = None
        field_0 = module_1.enum_from_json_schema(str_7, var_0)
        any_0 = field_0.validate(str_4)
        str_8 = '4'
        any_1 = field_0.validate(str_8)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'default'
        str_1 = 'oneOf'
        int_0 = 1
        str_2 = 'integer'
        var_0 = {str_0: int_0, str_1: str_2}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.one_of_from_json_schema(var_0, schema_definitions_0)
        any_0 = field_0.validate(int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'type'
        str_1 = 'properties'
        str_2 = 'object'
        str_3 = 'field'
        str_4 = 'if'
        str_5 = 'else'
        str_6 = 'pattern'
        str_7 = 'string'
        str_8 = '^a'
        str_9 = {str_0: str_7, str_6: str_8}
        str_10 = '^b'
        str_11 = {str_0: str_7, str_6: str_10}
        str_12 = '^c'
        str_13 = {str_0: str_7, str_6: str_12}
        str_14 = {str_4: str_9, str_7: str_11, str_5: str_13}
        str_15 = {str_3: str_14}
        str_16 = {str_0: str_2, str_1: str_15}
        field_0 = module_1.from_json_schema(str_16)
        any_0 = field_0.validate(str_15)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'type'
        str_1 = 'properties'
        str_2 = 'object'
        str_3 = 'field'
        str_4 = 'if'
        str_5 = 'then'
        str_6 = 'else'
        str_7 = 'pattern'
        str_8 = 'string'
        str_9 = '^a'
        str_10 = {str_0: str_8, str_7: str_9}
        str_11 = '^b'
        str_12 = {str_0: str_8, str_7: str_11}
        str_13 = '^c'
        str_14 = {str_0: str_8, str_7: str_13}
        str_15 = {str_4: str_10, str_5: str_12, str_6: str_14}
        str_16 = {str_3: str_15}
        str_17 = {str_0: str_2, str_1: str_16}
        field_0 = module_1.from_json_schema(str_17)
        str_18 = 'abc'
        str_19 = {str_3: str_18}
        any_0 = field_0.validate(str_19)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '$ref'
        str_1 = '#/definitions/JSONSchema'
        str_2 = {str_0: str_1}
        field_0 = module_1.from_json_schema(str_2)
        str_3 = 'type'
        str_4 = 'boolean'
        str_5 = {str_3: str_4}
        field_1 = module_1.from_json_schema(str_5)
        str_6 = 'null'
        str_7 = [str_4, str_6]
        str_8 = {str_3: str_7}
        field_2 = module_1.from_json_schema(str_8)
        var_0 = field_2.any_of
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'allOf'
        str_1 = 'type'
        str_2 = 'string'
        str_3 = {str_1: str_2}
        str_4 = [str_3, str_0]
        str_5 = {str_0: str_4}
        var_0 = None
        field_0 = module_1.all_of_from_json_schema(str_5, var_0)
    except BaseException:
        pass

def test_case_20():
    try:
        bool_0 = False
        field_0 = module_1.from_json_schema(bool_0)
        bool_1 = True
        field_1 = module_1.from_json_schema(bool_1)
        var_0 = print(field_1)
        str_0 = 'enum'
        int_0 = 3
        var_1 = {str_0: int_0}
        field_2 = module_1.from_json_schema(var_1)
    except BaseException:
        pass

def test_case_21():
    try:
        bool_0 = True
        field_0 = module_1.from_json_schema(bool_0)
        any_0 = module_2.Any()
        bool_1 = False
        field_1 = module_1.from_json_schema(bool_1)
        never_match_0 = module_3.NeverMatch()
        var_0 = {}
        field_2 = module_1.from_json_schema(var_0)
        any_1 = module_2.Any()
        str_0 = '$ref'
        str_1 = {str_0: str_0}
        field_3 = module_1.from_json_schema(str_1)
    except BaseException:
        pass

def test_case_22():
    try:
        list_0 = []
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'F7$\x0b7`Sd%^DuWT '
        boolean_0 = module_2.Boolean(description=str_0, default=list_0)
        int_0 = -1354
        integer_0 = module_2.Integer(precision=boolean_0, multiple_of=int_0)
        dict_1 = {str_0: dict_0}
        var_0 = module_1.to_json_schema(integer_0, dict_1)
        str_1 = 'S.P&4#1\\\x0c\t#AcaR8},^'
        field_0 = module_2.Field(title=str_1)
        var_1 = module_1.to_json_schema(field_0, dict_1)
    except BaseException:
        pass

def test_case_23():
    try:
        bool_0 = False
        field_0 = module_1.from_json_schema(bool_0)
        list_0 = [field_0]
        one_of_0 = module_3.OneOf(list_0)
        var_0 = module_1.to_json_schema(one_of_0)
        dict_0 = {}
        validation_result_0 = field_0.validate_or_error(var_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_1 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        var_1 = module_1.to_json_schema(field_1)
        str_0 = "Z-&LeK*?'YzuDNPU"
        field_2 = module_2.Field(title=str_0)
        var_2 = module_1.to_json_schema(field_2)
    except BaseException:
        pass