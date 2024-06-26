# Automatically generated by Pynguin.
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2
import decimal as module_3

def test_case_0():
    pass

def test_case_1():
    int_0 = 1198
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    field_0 = module_0.from_json_schema(dict_0)

def test_case_2():
    str_0 = 'b([I'
    bool_0 = False
    dict_0 = {str_0: str_0}
    schema_definitions_0 = module_1.SchemaDefinitions(**dict_0)
    field_0 = module_0.from_json_schema(bool_0, schema_definitions_0)

def test_case_3():
    dict_0 = {}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)

def test_case_4():
    validation_result_0 = None
    dict_0 = {validation_result_0: validation_result_0, validation_result_0: validation_result_0}
    tuple_0 = module_0.get_valid_types(dict_0)

def test_case_5():
    str_0 = '$ref'
    str_1 = '#/definitions/my_reference'
    str_2 = {str_0: str_1}
    var_0 = {}
    field_0 = module_0.ref_from_json_schema(str_2, var_0)

def test_case_6():
    schema_0 = module_1.Schema()
    bool_0 = True
    boolean_0 = module_2.Boolean(default=schema_0, allow_null=bool_0)
    var_0 = module_0.to_json_schema(schema_0, boolean_0)

def test_case_7():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_8():
    str_0 = 'not'
    str_1 = 'type'
    str_2 = 'string'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    var_0 = {}
    field_0 = module_0.not_from_json_schema(str_4, var_0)

def test_case_9():
    str_0 = 'type'
    str_1 = 'properties'
    str_2 = 'definitions'
    str_3 = 'object'
    str_4 = 'id'
    str_5 = '#/definitions/id'
    str_6 = {str_4: str_5}
    str_7 = 'title'
    str_8 = 'ID'
    str_9 = 'integer'
    str_10 = {str_7: str_8, str_0: str_9}
    str_11 = {str_4: str_10}
    str_12 = {str_0: str_3, str_1: str_6, str_2: str_11}
    field_0 = module_0.from_json_schema(str_12)

def test_case_10():
    str_0 = 'allOf'
    str_1 = 'type'
    str_2 = 'integer'
    str_3 = {str_1: str_2}
    str_4 = 'maximum'
    int_0 = 2
    int_1 = {str_4: int_0}
    var_0 = [str_3, int_1]
    var_1 = {str_0: var_0}
    var_2 = None
    field_0 = module_0.all_of_from_json_schema(var_1, var_2)

def test_case_11():
    str_0 = 'if'
    str_1 = 'then'
    str_2 = 'type'
    str_3 = 'const'
    str_4 = 'boolean'
    bool_0 = True
    var_0 = {str_2: str_4, str_3: bool_0}
    str_5 = 'number'
    str_6 = {str_2: str_5}
    var_1 = {str_0: var_0, str_1: str_6}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.if_then_else_from_json_schema(var_1, schema_definitions_0)

def test_case_12():
    str_0 = 'if'
    str_1 = 'then'
    str_2 = 'else'
    str_3 = 'type'
    str_4 = 'string'
    str_5 = {str_3: str_4}
    str_6 = 'boolean'
    str_7 = {str_3: str_6}
    str_8 = 'integer'
    str_9 = {str_3: str_8}
    var_0 = None
    var_1 = {str_0: str_5, str_1: str_7, str_2: str_9, str_4: var_0}
    field_0 = module_0.if_then_else_from_json_schema(var_1, var_0)
    var_2 = field_0.if_clause
    var_3 = field_0.else_clause

def test_case_13():
    str_0 = 'anyOf'
    str_1 = 'type'
    str_2 = 'boolean'
    str_3 = {str_1: str_2}
    str_4 = 'enum'
    str_5 = 'closed'
    str_6 = {str_4: str_5}
    str_7 = [str_3, str_6]
    str_8 = {str_0: str_7}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.any_of_from_json_schema(str_8, schema_definitions_0)

def test_case_14():
    str_0 = 'oneOf'
    str_1 = 'type'
    str_2 = 'integer'
    str_3 = {str_1: str_2}
    str_4 = 'string'
    str_5 = {str_1: str_4}
    str_6 = [str_3, str_5]
    str_7 = {str_0: str_6}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.one_of_from_json_schema(str_7, schema_definitions_0)

def test_case_15():
    string_0 = module_2.String()
    string_1 = module_2.String()
    str_0 = 'field2'
    string_2 = {str_0: string_0, str_0: string_1}
    object_0 = module_2.Object(properties=string_2)
    var_0 = module_0.to_json_schema(object_0)

def test_case_16():
    decimal_0 = module_3.Decimal()
    dict_0 = {decimal_0: decimal_0, decimal_0: decimal_0}
    bool_0 = False
    int_0 = -2038
    str_0 = ' N'
    string_0 = module_2.String(allow_blank=bool_0, trim_whitespace=bool_0, min_length=int_0, format=str_0)
    var_0 = module_0.to_json_schema(string_0, dict_0)

def test_case_17():
    str_0 = 'type'
    str_1 = 'properties'
    str_2 = 'object'
    str_3 = 'a'
    str_4 = 'b'
    str_5 = 'const'
    str_6 = 'foo'
    str_7 = {str_5: str_6}
    str_8 = 'if'
    str_9 = 'then'
    str_10 = 'else'
    str_11 = 'required'
    str_12 = [str_3]
    str_13 = {str_11: str_12}
    str_14 = 'bar'
    str_15 = {str_5: str_14}
    str_16 = 'baz'
    str_17 = {str_5: str_16}
    str_18 = {str_8: str_13, str_9: str_15, str_10: str_17}
    str_19 = {str_3: str_7, str_4: str_18}
    str_20 = {str_0: str_2, str_1: str_19}
    field_0 = module_0.from_json_schema(str_20)