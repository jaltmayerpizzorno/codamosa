# Automatically generated by Pynguin.
import typesystem.fields as module_0
import typesystem.json_schema as module_1
import typesystem.schemas as module_2

def test_case_0():
    boolean_0 = module_0.Boolean()

def test_case_1():
    dict_0 = {}
    field_0 = module_1.from_json_schema(dict_0)

def test_case_2():
    dict_0 = {}
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)

def test_case_3():
    dict_0 = {}
    tuple_0 = module_1.get_valid_types(dict_0)

def test_case_4():
    str_0 = '$ref'
    str_1 = '#/definitions/MyObject'
    str_2 = {str_0: str_1}
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_1.ref_from_json_schema(str_2, schema_definitions_0)
    string_0 = module_0.String()

def test_case_5():
    schema_definitions_0 = module_2.SchemaDefinitions()
    var_0 = module_1.to_json_schema(schema_definitions_0, schema_definitions_0)

def test_case_6():
    schema_definitions_0 = module_2.SchemaDefinitions()
    str_0 = 'oneof'
    float_0 = -2230.075836206166
    dict_0 = {str_0: float_0}
    tuple_0 = module_1.get_valid_types(dict_0)
    field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
    var_0 = module_1.to_json_schema(field_0)

def test_case_7():
    str_0 = 'oneof'
    float_0 = -2255.4189624014293
    dict_0 = {str_0: float_0}
    field_0 = module_1.from_json_schema(dict_0)
    var_0 = module_1.to_json_schema(field_0)

def test_case_8():
    str_0 = 's&ns=.+86\x0byQ'
    field_0 = module_0.Field(title=str_0, default=str_0)
    dict_0 = module_1.get_standard_properties(field_0)

def test_case_9():
    str_0 = 'invalid_key'
    dict_0 = {str_0: str_0, str_0: str_0}
    tuple_0 = module_1.get_valid_types(dict_0)
    float_0 = 2256.27
    tuple_1 = module_1.get_valid_types(dict_0)
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_1.from_json_schema(dict_0, schema_definitions_0)
    dict_1 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    tuple_2 = module_1.get_valid_types(dict_1)
    tuple_3 = module_1.get_valid_types(dict_1)
    var_0 = module_1.to_json_schema(field_0)

def test_case_10():
    str_0 = 'oneof'
    float_0 = -2255.4189624014293
    dict_0 = {str_0: float_0}
    field_0 = module_1.from_json_schema(dict_0)
    tuple_0 = module_1.get_valid_types(dict_0)
    dict_1 = module_1.get_standard_properties(field_0)

def test_case_11():
    bool_0 = False
    float_0 = -1065.33
    dict_0 = {bool_0: float_0}
    tuple_0 = module_1.get_valid_types(dict_0)
    field_0 = module_1.from_json_schema(bool_0)

def test_case_12():
    schema_definitions_0 = module_2.SchemaDefinitions()
    schema_definitions_1 = None
    var_0 = module_1.to_json_schema(schema_definitions_0, schema_definitions_1)

def test_case_13():
    schema_definitions_0 = module_2.SchemaDefinitions()
    int_0 = schema_definitions_0.__len__()
    str_0 = 'oneof'
    float_0 = -2255.4189624014293
    bool_0 = False
    dict_0 = {str_0: float_0}
    field_0 = module_1.from_json_schema(bool_0)
    field_1 = module_1.from_json_schema(dict_0)
    tuple_0 = module_1.get_valid_types(dict_0)
    var_0 = module_1.to_json_schema(field_0, dict_0)

def test_case_14():
    str_0 = 'type'
    str_1 = {str_0: str_0}
    tuple_0 = module_1.get_valid_types(str_1)

def test_case_15():
    str_0 = 'enum'
    str_1 = 'default'
    str_2 = 'red'
    dict_0 = {str_1: str_2, str_0: str_2, str_1: str_0}
    field_0 = module_1.from_json_schema(dict_0)

def test_case_16():
    schema_definitions_0 = module_2.SchemaDefinitions()
    str_0 = 'if'
    str_1 = 'then'
    str_2 = 'type'
    str_3 = 'inimum'
    str_4 = 'number'
    int_0 = 5
    var_0 = {str_2: str_4, str_3: int_0}
    str_5 = 'maximum'
    int_1 = 42
    var_1 = {str_2: str_4, str_5: int_1}
    str_6 = {str_2: str_1}
    var_2 = {str_0: var_0, str_1: var_1, str_4: str_6}
    field_0 = module_1.if_then_else_from_json_schema(var_2, schema_definitions_0)
    var_3 = field_0.then_clause
    var_4 = field_0.else_clause

def test_case_17():
    str_0 = 'type'
    str_1 = 'minLength'
    str_2 = 'string'
    int_0 = 2
    var_0 = {str_0: str_2, str_1: int_0}
    str_3 = 'enum'
    str_4 = 'accepted'
    str_5 = [str_4, str_1]
    str_6 = {str_0: str_2, str_3: str_5}
    str_7 = 'pattern'
    str_8 = '^rejected'
    str_9 = {str_0: str_2, str_7: str_8}
    schema_definitions_0 = module_2.SchemaDefinitions()
    str_10 = 'if'
    str_11 = 'then'
    str_12 = 'else'
    var_1 = {str_10: var_0, str_11: str_6, str_12: str_9}
    field_0 = module_1.if_then_else_from_json_schema(var_1, schema_definitions_0)
    var_2 = field_0.if_clause
    var_3 = field_0.then_clause

def test_case_18():
    str_0 = 'type'
    str_1 = 'minLength'
    str_2 = 'string'
    str_3 = 'enum'
    str_4 = 'accepted'
    str_5 = [str_4, str_1]
    str_6 = {str_0: str_2, str_3: str_5}
    str_7 = 'pattern'
    str_8 = '^rejected'
    str_9 = {str_0: str_2, str_7: str_8}
    schema_definitions_0 = module_2.SchemaDefinitions()
    str_10 = 'if'
    str_11 = 'then'
    str_12 = 'else'
    var_0 = {str_10: str_2, str_11: str_6, str_12: str_9}
    field_0 = module_1.if_then_else_from_json_schema(var_0, schema_definitions_0)
    var_1 = field_0.if_clause

def test_case_19():
    str_0 = 'anyOf'
    str_1 = 'maxLength'
    dict_0 = {str_0: str_0, str_1: str_1, str_0: str_1, str_1: str_1}
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_1.any_of_from_json_schema(dict_0, schema_definitions_0)

def test_case_20():
    any_0 = module_0.Any()
    var_0 = module_1.to_json_schema(any_0)
    str_0 = '5;j8e!/4'
    string_0 = module_0.String()
    string_1 = {str_0: string_0}
    reference_0 = module_2.Reference(str_0, string_1)
    var_1 = {}
    var_2 = module_1.to_json_schema(reference_0, var_1)
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_0.Field(default=var_0)
    dict_0 = module_1.get_standard_properties(field_0)