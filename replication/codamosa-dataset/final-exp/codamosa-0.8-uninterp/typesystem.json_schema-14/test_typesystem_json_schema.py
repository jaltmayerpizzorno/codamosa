# Automatically generated by Pynguin.
import typesystem.json_schema as module_0
import typesystem.fields as module_1
import typesystem.composites as module_2
import typesystem.schemas as module_3

def test_case_0():
    pass

def test_case_1():
    float_0 = -334.4385179430374
    dict_0 = {float_0: float_0}
    field_0 = module_0.from_json_schema(dict_0)

def test_case_2():
    dict_0 = {}
    schema_definitions_0 = None
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)

def test_case_3():
    dict_0 = {}
    tuple_0 = module_0.get_valid_types(dict_0)

def test_case_4():
    str_0 = 'type'
    str_1 = 'enum'
    str_2 = 'default'
    str_3 = 'http://json-schema.org/draft-06/schema#'
    str_4 = 'string'
    str_5 = 'aaaa'
    str_6 = 'bbbb'
    str_7 = {str_6: str_3, str_0: str_4, str_1: str_6, str_2: str_5}
    field_0 = module_0.from_json_schema(str_7)

def test_case_5():
    any_0 = module_1.Any()
    var_0 = module_0.to_json_schema(any_0)
    never_match_0 = module_2.NeverMatch()
    string_0 = module_1.String()
    var_1 = module_0.to_json_schema(string_0)

def test_case_6():
    dict_0 = {}
    schema_definitions_0 = module_3.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_7():
    never_match_0 = module_2.NeverMatch()
    var_0 = module_0.to_json_schema(never_match_0)
    string_0 = module_1.String()
    var_1 = module_0.to_json_schema(string_0)
    bool_0 = True
    string_1 = module_1.String()
    field_0 = module_1.Field(default=string_1)

def test_case_8():
    str_0 = 'type'
    str_1 = 'string'
    str_2 = {str_0: str_1}
    field_0 = module_0.from_json_schema(str_2)
    string_0 = module_1.String()

def test_case_9():
    str_0 = 'type'
    str_1 = 'minimum'
    str_2 = 'number'
    int_0 = 5
    var_0 = {str_0: str_2, str_1: int_0}
    str_3 = 'maximum'
    int_1 = 8
    var_1 = {str_0: str_2, str_3: int_1}
    str_4 = 'anyOf'
    var_2 = [var_0, var_1]
    var_3 = {str_4: var_2}
    schema_definitions_0 = module_3.SchemaDefinitions()
    field_0 = module_0.any_of_from_json_schema(var_3, schema_definitions_0)
    float_0 = module_1.Float(minimum=int_0)
    float_1 = module_1.Float(maximum=int_1)
    float_2 = [float_0, float_1]
    union_0 = module_1.Union(float_2)

def test_case_10():
    str_0 = 'type'
    str_1 = 'ne'
    str_2 = 'integer'
    var_0 = {str_0: str_2, str_1: str_2}
    field_0 = module_0.from_json_schema(var_0)
    var_1 = module_0.to_json_schema(field_0)

def test_case_11():
    str_0 = 'foo'
    const_0 = module_1.Const(str_0)
    str_1 = 'const'
    str_2 = {str_1: str_0}
    var_0 = None
    field_0 = module_0.const_from_json_schema(str_2, var_0)

def test_case_12():
    str_0 = 'if'
    str_1 = 'then'
    str_2 = 'else'
    str_3 = 'type'
    str_4 = 'integer'
    str_5 = {str_3: str_4}
    str_6 = 'string'
    str_7 = {str_3: str_6}
    str_8 = 'number'
    str_9 = {str_3: str_8}
    str_10 = {str_0: str_5, str_1: str_7, str_2: str_9}
    var_0 = None
    field_0 = module_0.if_then_else_from_json_schema(str_10, var_0)
    integer_0 = module_1.Integer()
    string_0 = module_1.String()
    float_0 = module_1.Float()

def test_case_13():
    str_0 = 'properties'
    str_1 = 'string'
    str_2 = 'a8sKodv%/xkI^F]*2\ra'
    int_0 = 18
    var_0 = {str_2: str_2, str_1: int_0}
    var_1 = {str_1: str_1, str_0: var_0}
    var_2 = {str_0: str_1, str_0: var_1}
    field_0 = module_0.from_json_schema(var_2)

def test_case_14():
    schema_definitions_0 = module_3.SchemaDefinitions()
    str_0 = '$ref'
    str_1 = '#/definitions/string_schema'
    str_2 = {str_0: str_1}
    field_0 = module_0.from_json_schema(str_2, schema_definitions_0)
    str_3 = '#/definitions/integer_schema'
    str_4 = {str_0: str_3}
    field_1 = module_0.from_json_schema(str_4, schema_definitions_0)

def test_case_15():
    str_0 = 'not'
    str_1 = 'type'
    str_2 = 'string'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    var_0 = None
    field_0 = module_0.not_from_json_schema(str_4, var_0)

def test_case_16():
    str_0 = '^I\x0c/dU'
    str_1 = 'properties'
    str_2 = 'object'
    str_3 = 'name'
    str_4 = 'age'
    str_5 = 'minimum'
    str_6 = '#&PMo'
    int_0 = 18
    var_0 = {str_0: str_6, str_5: int_0}
    var_1 = {str_3: str_3, str_4: var_0}
    var_2 = {str_0: str_2, str_1: var_1}
    field_0 = module_0.from_json_schema(var_2)
    var_3 = module_0.to_json_schema(field_0)

def test_case_17():
    str_0 = '^I\x0c/dU'
    str_1 = 'properties'
    str_2 = 'object'
    str_3 = 'age'
    str_4 = 'string'
    str_5 = '#&PMo'
    int_0 = 18
    var_0 = {str_0: str_5, str_4: int_0}
    var_1 = {str_4: str_4, str_3: var_0}
    var_2 = {str_0: str_2, str_1: var_1}
    field_0 = module_0.from_json_schema(var_2)
    var_3 = module_0.to_json_schema(field_0)

def test_case_18():
    str_0 = 'type'
    str_1 = 'properties'
    str_2 = 'additionalProperties'
    str_3 = 'P;\rvvx@RM^"z~'
    str_4 = 'maxProperties'
    str_5 = 'object'
    str_6 = 'first_name'
    str_7 = 'last_name'
    str_8 = 'date_of_birth'
    str_9 = 'is_active'
    str_10 = 'string'
    str_11 = {str_0: str_10}
    str_12 = {str_0: str_10}
    str_13 = 'format'
    str_14 = 'date'
    str_15 = {str_0: str_10, str_13: str_14}
    str_16 = 'boolean'
    str_17 = {str_0: str_16}
    str_18 = 'items'
    str_19 = 'uniqueItems'
    str_20 = 'minItems'
    str_21 = 'maxItems'
    str_22 = 'array'
    str_23 = {str_0: str_10}
    bool_0 = True
    int_0 = 1000
    var_0 = {str_0: str_22, str_18: str_23, str_19: bool_0, str_20: bool_0, str_21: int_0}
    var_1 = {str_6: str_11, str_7: str_12, str_8: str_15, str_9: str_17, str_10: var_0}
    bool_1 = False
    int_1 = 10
    var_2 = {str_0: str_5, str_1: var_1, str_2: bool_1, str_3: bool_0, str_4: int_1}
    field_0 = module_0.from_json_schema(var_2)
    string_0 = module_1.String()

def test_case_19():
    any_0 = module_1.Any()
    never_match_0 = module_2.NeverMatch()
    var_0 = module_0.to_json_schema(never_match_0)
    string_0 = module_1.String()
    var_1 = module_0.to_json_schema(string_0)
    any_1 = never_match_0.get_default_value()
    integer_0 = module_1.Integer()
    string_1 = module_1.String()
    array_0 = module_1.Array(string_1)
    var_2 = module_0.to_json_schema(array_0)
    schema_definitions_0 = module_3.SchemaDefinitions()
    choice_0 = module_1.Choice()

def test_case_20():
    any_0 = module_1.Any()
    var_0 = module_0.to_json_schema(any_0)
    never_match_0 = module_2.NeverMatch()
    var_1 = module_0.to_json_schema(never_match_0)
    string_0 = module_1.String()
    var_2 = module_0.to_json_schema(string_0)
    bool_0 = True
    string_1 = module_1.String()
    var_3 = module_0.to_json_schema(string_1)
    int_0 = 0
    string_2 = module_1.String(min_length=int_0)
    var_4 = module_0.to_json_schema(string_2)
    var_5 = module_0.to_json_schema(string_0)
    integer_0 = module_1.Integer()
    var_6 = module_0.to_json_schema(integer_0)
    float_0 = module_1.Float()
    var_7 = module_0.to_json_schema(float_0)

def test_case_21():
    str_0 = 'iA?.7;\'GLg"\t\x0bEKC%\''
    any_0 = module_1.Any(title=str_0)
    bool_0 = False
    any_1 = any_0.validate(any_0, bool_0)
    const_0 = module_1.Const(any_0)
    var_0 = module_0.to_json_schema(const_0)