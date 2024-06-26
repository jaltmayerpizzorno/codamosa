# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2
import typesystem.composites as module_3

def test_case_0():
    pass

def test_case_1():
    schema_definitions_0 = module_0.SchemaDefinitions()
    str_0 = 'A'
    field_0 = module_1.from_json_schema(str_0, schema_definitions_0)

def test_case_2():
    bool_0 = False
    field_0 = module_1.from_json_schema(bool_0)

def test_case_3():
    dict_0 = {}
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.from_json_schema(dict_0)

def test_case_4():
    dict_0 = {}
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)

def test_case_5():
    str_0 = 'oneOf'
    str_1 = {str_0: str_0}
    str_2 = 'string'
    str_3 = {str_0: str_2}
    str_4 = [str_1, str_3]
    str_5 = {str_0: str_4}
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.one_of_from_json_schema(str_5, schema_definitions_0)
    bool_0 = False
    float_0 = module_2.Float()
    string_0 = module_2.String()

def test_case_6():
    int_0 = -4
    string_0 = module_2.String(max_length=int_0)
    var_0 = module_1.to_json_schema(string_0)

def test_case_7():
    dict_0 = {}
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.from_json_schema(dict_0)
    field_1 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
    var_0 = module_1.to_json_schema(field_1)

def test_case_8():
    str_0 = 'anyOf'
    str_1 = 'type'
    str_2 = 'string'
    str_3 = {str_1: str_2}
    str_4 = 'integer'
    str_5 = {str_1: str_4}
    str_6 = [str_3, str_5]
    str_7 = {str_0: str_6}
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.any_of_from_json_schema(str_7, schema_definitions_0)

def test_case_9():
    int_0 = 5
    string_0 = module_2.String(max_length=int_0)
    var_0 = module_1.to_json_schema(string_0)
    field_0 = module_1.from_json_schema(var_0)

def test_case_10():
    str_0 = 'Should be fail'
    var_0 = AssertionError(str_0)
    str_1 = 'enum'
    str_2 = 'one'
    str_3 = 'two'
    str_4 = 'three'
    str_5 = [str_2, str_3, str_4]
    str_6 = {str_1: str_5}
    var_1 = {}
    field_0 = module_1.enum_from_json_schema(str_6, var_1)

def test_case_11():
    str_0 = 'const'
    str_1 = 'test'
    str_2 = {str_0: str_1}
    var_0 = None
    field_0 = module_1.const_from_json_schema(str_2, var_0)

def test_case_12():
    str_0 = 'if'
    str_1 = 'then'
    str_2 = 'string'
    str_3 = {str_0: str_2}
    str_4 = {str_2: str_2}
    str_5 = 'number'
    str_6 = {str_5: str_5}
    str_7 = {str_0: str_3, str_1: str_4, str_2: str_6}
    var_0 = {}
    field_0 = module_1.if_then_else_from_json_schema(str_7, var_0)

def test_case_13():
    str_0 = 'if'
    str_1 = 'then'
    str_2 = 'else'
    str_3 = 'type'
    str_4 = 'string'
    str_5 = {str_3: str_4}
    str_6 = {str_3: str_4}
    str_7 = 'number'
    str_8 = {str_3: str_7}
    str_9 = {str_0: str_5, str_1: str_6, str_2: str_8}
    var_0 = {}
    field_0 = module_1.if_then_else_from_json_schema(str_9, var_0)

def test_case_14():
    integer_0 = module_2.Integer()
    optional_0 = None
    var_0 = module_1.to_json_schema(integer_0, optional_0)

def test_case_15():
    str_0 = 'type'
    str_1 = 'properties'
    str_2 = 'object'
    str_3 = 'not_property'
    str_4 = 'not'
    str_5 = 'string'
    str_6 = {str_0: str_5}
    str_7 = {str_4: str_6}
    str_8 = {str_3: str_7}
    str_9 = {str_0: str_2, str_1: str_8}
    field_0 = module_1.from_json_schema(str_9)

def test_case_16():
    bool_0 = False
    never_match_0 = module_3.NeverMatch()
    field_0 = module_1.from_json_schema(bool_0)
    any_0 = module_2.Any()
    str_0 = 'type'
    str_1 = 'integer'
    str_2 = {str_0: str_1}
    field_1 = module_1.from_json_schema(str_2)
    integer_0 = module_2.Integer()
    str_3 = []
    str_4 = {str_0: str_3}
    field_2 = module_1.from_json_schema(str_4)
    string_0 = module_2.String()
    integer_1 = module_2.Integer()
    var_0 = string_0 | integer_1
    str_5 = 'enum'
    int_0 = 2
    var_1 = [bool_0, int_0]
    var_2 = {str_5: var_1}
    field_3 = module_1.from_json_schema(var_2)
    var_3 = (bool_0, int_0)
    choice_0 = module_2.Choice(choices=var_3)
    var_4 = module_1.to_json_schema(field_3)
    str_6 = integer_1.get_error_text(str_0)

def test_case_17():
    bool_0 = False
    field_0 = module_1.from_json_schema(bool_0)
    bool_1 = True
    field_1 = module_1.from_json_schema(bool_1)
    str_0 = 'type'
    str_1 = 'number'
    str_2 = {str_0: str_1}
    field_2 = module_1.from_json_schema(str_2)
    str_3 = 'enum'
    int_0 = 2
    var_0 = [bool_1, int_0]
    var_1 = {str_3: var_0}
    field_3 = module_1.from_json_schema(var_1)
    str_4 = 'const'
    str_5 = 'one'
    str_6 = {str_4: str_5}
    field_4 = module_1.from_json_schema(str_6)
    str_7 = 'allOf'
    str_8 = {str_0: str_1}
    str_9 = [str_8]
    str_10 = {str_7: str_9}
    field_5 = module_1.from_json_schema(str_10)
    str_11 = 'anyOf'
    str_12 = {str_0: str_1}
    str_13 = [str_12]
    str_14 = {str_11: str_13}
    field_6 = module_1.from_json_schema(str_14)

def test_case_18():
    str_0 = 'type'
    str_1 = 'properties'
    str_2 = 'object'
    str_3 = 'not_property'
    str_4 = 'string'
    str_5 = {str_0: str_4}
    str_6 = {str_2: str_5}
    str_7 = {str_3: str_6}
    str_8 = {str_0: str_2, str_1: str_7}
    field_0 = module_1.from_json_schema(str_8)

def test_case_19():
    str_0 = '$ref'
    str_1 = '#/definitions/foo'
    str_2 = {str_0: str_1}
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.ref_from_json_schema(str_2, schema_definitions_0)

def test_case_20():
    str_0 = '$schema'
    str_1 = 'allOf'
    str_2 = 'type'
    str_3 = 'properties'
    str_4 = 'required'
    str_5 = 'object'
    str_6 = 'a'
    str_7 = 'minimum'
    str_8 = 'integer'
    int_0 = 5
    var_0 = {str_2: str_8, str_7: int_0}
    var_1 = {str_6: var_0}
    str_9 = [str_6]
    var_2 = {str_2: str_5, str_3: var_1, str_4: str_9}
    str_10 = 'b'
    str_11 = 'minLength'
    str_12 = 'string'
    int_1 = 1
    var_3 = {str_2: str_12, str_11: int_1}
    var_4 = {str_10: var_3}
    str_13 = [str_10]
    var_5 = {str_2: str_5, str_3: var_4, str_4: str_13}
    var_6 = [var_2, var_5]
    var_7 = {str_0: str_13, str_1: var_6}
    var_8 = {}
    field_0 = module_1.all_of_from_json_schema(var_7, var_8)

def test_case_21():
    str_0 = '(I*OLmW'
    dict_0 = {str_0: str_0}
    choice_0 = module_2.Choice()
    var_0 = module_1.to_json_schema(choice_0, dict_0)
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.from_json_schema(dict_0, schema_definitions_0)
    dict_1 = {str_0: str_0, str_0: str_0, str_0: str_0}
    field_1 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
    var_1 = module_1.to_json_schema(field_1, dict_1)

def test_case_22():
    bool_0 = True
    field_0 = module_1.from_json_schema(bool_0)
    bool_1 = False
    field_1 = module_1.from_json_schema(bool_1)
    field_2 = module_1.from_json_schema(bool_1)
    str_0 = 'type'
    str_1 = 'null'
    str_2 = {str_0: str_1}
    field_3 = module_1.from_json_schema(str_2)
    str_3 = {str_0: str_1}
    field_4 = module_1.from_json_schema(str_3)
    str_4 = {str_0: str_1}
    field_5 = module_1.from_json_schema(str_4)
    str_5 = 'integer'
    str_6 = {str_0: str_5}
    field_6 = module_1.from_json_schema(str_6)
    str_7 = {str_0: str_5}
    field_7 = module_1.from_json_schema(str_7)

def test_case_23():
    int_0 = -4
    string_0 = module_2.String(max_length=int_0)
    str_0 = 'nOlAoz\t2wd%KL"iJH'
    bool_0 = True
    boolean_0 = module_2.Boolean(title=str_0, allow_null=bool_0)
    var_0 = module_1.to_json_schema(boolean_0)
    field_0 = module_1.from_json_schema(bool_0)

def test_case_24():
    int_0 = 4463
    string_0 = module_2.String(max_length=int_0)
    dict_0 = {int_0: int_0}
    schema_definitions_0 = module_0.SchemaDefinitions()
    str_0 = "m7`4'\r^"
    boolean_0 = module_2.Boolean(title=str_0)
    var_0 = module_1.to_json_schema(boolean_0)
    str_1 = 'y!wxK d2-wjvM.T;\nR.W'
    const_0 = module_2.Const(str_1)
    var_1 = module_1.to_json_schema(const_0, dict_0)
    field_0 = module_1.from_json_schema(dict_0)

def test_case_25():
    str_0 = 'age'
    int_0 = 0
    schema_definitions_0 = module_0.SchemaDefinitions()
    int_1 = 4
    object_0 = module_2.Object(properties=schema_definitions_0, min_properties=int_1)
    var_0 = module_1.to_json_schema(object_0)
    int_2 = 100
    integer_0 = module_2.Integer(minimum=int_0, maximum=int_2)
    integer_1 = {str_0: integer_0}
    object_1 = module_2.Object(properties=integer_1)
    array_0 = module_2.Array(object_1)
    integer_2 = module_2.Integer(minimum=int_0, maximum=int_2)
    any_0 = module_2.Any()
    bool_0 = False
    string_0 = module_2.String(trim_whitespace=bool_0)