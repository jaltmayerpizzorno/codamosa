# Automatically generated by Pynguin.
import typesystem.json_schema as module_0
import typesystem.fields as module_1
import typesystem.schemas as module_2
import typesystem.composites as module_3

def test_case_0():
    pass

def test_case_1():
    str_0 = 'eQ'
    str_1 = {str_0: str_0}
    field_0 = module_0.from_json_schema(str_1)

def test_case_2():
    str_0 = '\nfq]z'
    bool_0 = False
    field_0 = module_1.Field(description=str_0, allow_null=bool_0)
    dict_0 = module_0.get_standard_properties(field_0)
    bool_1 = True
    field_1 = module_0.from_json_schema(bool_1)

def test_case_3():
    dict_0 = {}
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)

def test_case_4():
    str_0 = 'enum'
    str_1 = 'type'
    str_2 = 'foo'
    int_0 = 2
    float_0 = 3.14
    var_0 = None
    bool_0 = True
    bool_1 = False
    str_3 = 'xyz'
    str_4 = '123'
    str_5 = '0'
    var_1 = [str_2, int_0, float_0, var_0, bool_0, bool_1, str_3, str_4, str_5]
    str_6 = 'number'
    var_2 = {str_0: var_1, str_1: str_6}
    field_0 = module_0.from_json_schema(var_2)

def test_case_5():
    str_0 = '\nfq]z'
    bool_0 = False
    field_0 = module_1.Field(description=str_0, allow_null=bool_0)
    dict_0 = module_0.get_standard_properties(field_0)

def test_case_6():
    str_0 = 'not'
    str_1 = 'type'
    str_2 = 'string'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    var_0 = None
    field_0 = module_0.not_from_json_schema(str_4, var_0)

def test_case_7():
    dict_0 = {}
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_8():
    str_0 = 'properties'
    str_1 = 'description'
    str_2 = {str_0: str_1}
    str_3 = {str_0: str_1, str_0: str_2}
    field_0 = module_0.from_json_schema(str_3)
    var_0 = module_0.to_json_schema(field_0)

def test_case_9():
    str_0 = ''
    str_1 = 'pattern'
    str_2 = {str_0: str_0, str_1: str_0, str_1: str_1}
    field_0 = module_0.from_json_schema(str_2)
    var_0 = module_0.to_json_schema(field_0)

def test_case_10():
    str_0 = 'allOf'
    str_1 = 'oneOf'
    str_2 = 'osp'
    str_3 = 'test2'
    str_4 = {str_2: str_3}
    str_5 = {str_1: str_3}
    str_6 = [str_4, str_5]
    str_7 = {str_0: str_6}
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_0.all_of_from_json_schema(str_7, schema_definitions_0)

def test_case_11():
    str_0 = 'if'
    str_1 = 'then'
    str_2 = 'string'
    str_3 = 'const'
    str_4 = 'Yes!'
    str_5 = {str_3: str_4}
    str_6 = {str_0: str_2, str_1: str_5}
    var_0 = {}
    field_0 = module_0.if_then_else_from_json_schema(str_6, var_0)

def test_case_12():
    any_0 = module_1.Any()
    bool_0 = False
    field_0 = module_0.from_json_schema(bool_0)
    str_0 = 'string'
    str_1 = {str_0: str_0}
    field_1 = module_0.from_json_schema(str_1)
    string_0 = module_1.String()
    str_2 = 'patternProperties'
    str_3 = 'additionalProperties'
    str_4 = 'object'
    str_5 = 'number'
    str_6 = {str_0: str_5}
    str_7 = {str_5: str_6}
    var_0 = {str_3: str_4, str_2: str_7, str_3: bool_0}
    field_2 = module_0.from_json_schema(var_0)

def test_case_13():
    str_0 = 'anyOf'
    str_1 = 'default'
    str_2 = 'type'
    str_3 = 'integer'
    str_4 = {str_2: str_3}
    str_5 = 'string'
    str_6 = {str_2: str_5}
    str_7 = [str_4, str_6]
    int_0 = 5
    var_0 = {str_0: str_7, str_1: int_0}
    var_1 = {}
    field_0 = module_0.any_of_from_json_schema(var_0, var_1)

def test_case_14():
    str_0 = '$ref'
    str_1 = '#/definitions/test'
    str_2 = {str_0: str_1}
    field_0 = module_0.from_json_schema(str_2)

def test_case_15():
    bool_0 = True
    field_0 = module_0.from_json_schema(bool_0)
    any_0 = module_1.Any()
    bool_1 = False
    field_1 = module_0.from_json_schema(bool_1)
    never_match_0 = module_3.NeverMatch()
    str_0 = 'string'
    str_1 = {str_0: str_0}
    field_2 = module_0.from_json_schema(str_1)
    string_0 = module_1.String()
    str_2 = 'patternProperties'
    str_3 = 'additionalProperties'
    str_4 = 'object'
    str_5 = 'foo.*'
    str_6 = 'number'
    str_7 = {str_5: str_6}
    str_8 = {str_5: str_7}
    var_0 = {str_3: str_4, str_2: str_8, str_3: bool_1}
    field_3 = module_0.from_json_schema(var_0)
    float_0 = module_1.Float()
    var_1 = module_0.to_json_schema(field_1)

def test_case_16():
    str_0 = 'items'
    str_1 = 'type'
    str_2 = 'description'
    str_3 = 'string'
    str_4 = {str_2: str_0, str_1: str_3}
    str_5 = 'Number_schema'
    str_6 = 'number'
    str_7 = {str_2: str_5, str_1: str_6}
    str_8 = [str_4, str_7]
    str_9 = 'array'
    str_10 = {str_0: str_8, str_1: str_9}
    str_11 = 'array'
    bool_0 = False
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_0.from_json_schema_type(str_10, str_11, bool_0, schema_definitions_0)
    var_0 = type(field_0)
    var_1 = ()
    array_0 = module_1.Array(var_1)
    var_2 = type(array_0)

def test_case_17():
    dict_0 = {}
    tuple_0 = module_0.get_valid_types(dict_0)
    str_0 = 'type'
    str_1 = 'string'
    str_2 = {str_0: str_1}
    field_0 = module_0.from_json_schema(str_2)
    validation_result_0 = field_0.validate_or_error(dict_0)
    string_0 = module_1.String()
    str_3 = 'enum'
    str_4 = 'foo'
    str_5 = 'bar'
    str_6 = [str_4, str_5]
    str_7 = {str_3: str_6}
    field_1 = module_0.from_json_schema(str_7)
    str_8 = [str_4, str_5]
    choice_0 = module_1.Choice()
    str_9 = 'items'
    str_10 = 'array'
    str_11 = {str_0: str_1}
    str_12 = {str_0: str_10, str_9: str_11}
    field_2 = module_0.from_json_schema(str_12)
    string_1 = module_1.String()
    str_13 = 'allOf'
    str_14 = {str_0: str_1}
    str_15 = 'minLength'
    int_0 = 2
    int_1 = {str_15: int_0}
    var_0 = [str_14, int_1]
    var_1 = {str_13: var_0}
    field_3 = module_0.from_json_schema(var_1)
    string_2 = module_1.String(min_length=int_0)
    string_3 = module_1.String()
    string_4 = [string_2, string_3]
    all_of_0 = module_3.AllOf(string_4)

def test_case_18():
    str_0 = 'allOf'
    str_1 = 'string'
    str_2 = {str_0: str_1}
    str_3 = 'oneOf'
    str_4 = 'osp'
    str_5 = 'test2'
    str_6 = {str_3: str_5}
    str_7 = [str_2, str_2, str_6, str_1, str_4]
    str_8 = {str_0: str_7}
    schema_definitions_0 = module_2.SchemaDefinitions()
    field_0 = module_0.all_of_from_json_schema(str_8, schema_definitions_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_19():
    str_0 = 'foo'
    string_0 = module_1.String()
    integer_0 = module_1.Integer()
    var_0 = [string_0, integer_0]
    all_of_0 = module_3.AllOf(var_0)
    all_of_1 = {str_0: all_of_0}
    reference_0 = module_2.Reference(str_0, all_of_1)
    str_1 = 'bar'
    string_1 = module_1.String()
    array_0 = module_1.Array(string_1)
    array_1 = {str_1: array_0}
    reference_1 = module_2.Reference(str_1, array_1)
    reference_2 = [reference_0, reference_1]
    all_of_2 = module_3.AllOf(reference_2)
    var_1 = module_0.to_json_schema(all_of_2)

def test_case_20():
    str_0 = 'uuid'
    string_0 = module_1.String(format=str_0)
    string_1 = module_1.String(format=str_0)
    integer_0 = module_1.Integer()
    var_0 = [string_0, string_1, integer_0]
    array_0 = module_1.Array(var_0)
    var_1 = module_0.to_json_schema(array_0)

def test_case_21():
    str_0 = 'a'
    integer_0 = module_1.Integer()
    int_0 = 1
    string_0 = module_1.String(min_length=int_0)
    var_0 = [integer_0, string_0]
    union_0 = module_1.Union(var_0)
    union_1 = {str_0: union_0}
    object_0 = module_1.Object(properties=union_1)
    var_1 = module_0.to_json_schema(object_0)

def test_case_22():
    string_0 = module_1.String()
    str_0 = '^[A-Za-z]\\d$'
    string_1 = module_1.String(pattern=str_0)
    var_0 = module_0.to_json_schema(string_1)
    string_2 = module_1.String(format=str_0)
    var_1 = module_0.to_json_schema(string_2)
    int_0 = 5
    string_3 = module_1.String(max_length=int_0)
    var_2 = module_0.to_json_schema(string_3)

def test_case_23():
    str_0 = 'type'
    str_1 = 'boolean'
    str_2 = {str_0: str_1}
    field_0 = module_0.from_json_schema(str_2)
    str_3 = 'string'
    str_4 = {str_0: str_3}
    field_1 = module_0.from_json_schema(str_4)
    str_5 = 'integer'
    str_6 = {str_0: str_5}
    field_2 = module_0.from_json_schema(str_6)
    str_7 = 'number'
    str_8 = {str_0: str_7}
    field_3 = module_0.from_json_schema(str_8)
    str_9 = 'object'
    str_10 = {str_0: str_9}
    field_4 = module_0.from_json_schema(str_10)
    str_11 = 'array'
    str_12 = {str_0: str_11}
    field_5 = module_0.from_json_schema(str_12)
    str_13 = {str_0: str_11}
    field_6 = module_0.from_json_schema(str_13)
    var_0 = field_6.items
    any_0 = module_1.Any()
    str_14 = 'null'
    str_15 = {str_0: str_14}
    field_7 = module_0.from_json_schema(str_15)
    never_match_0 = module_3.NeverMatch()