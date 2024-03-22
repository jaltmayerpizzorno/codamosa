# Automatically generated by Pynguin.
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2
import typesystem.composites as module_3
import re as module_4
import decimal as module_5

def test_case_0():
    pass

def test_case_1():
    tuple_0 = ()
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: tuple_0}
    field_0 = module_0.from_json_schema(dict_0)

def test_case_2():
    bool_0 = True
    field_0 = module_0.from_json_schema(bool_0)

def test_case_3():
    str_0 = '*BwT\x0cvF\\n#mX'
    dict_0 = {str_0: str_0, str_0: str_0}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)

def test_case_4():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0}
    tuple_1 = module_0.get_valid_types(dict_0)

def test_case_5():
    integer_0 = module_2.Integer()
    var_0 = module_0.to_json_schema(integer_0)

def test_case_6():
    bool_0 = True
    field_0 = module_0.from_json_schema(bool_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_7():
    bool_0 = False
    field_0 = module_0.from_json_schema(bool_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_8():
    str_0 = 'not'
    str_1 = 'type'
    str_2 = 'null'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.not_from_json_schema(str_4, schema_definitions_0)
    var_0 = field_0.negated

def test_case_9():
    tuple_0 = ()
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: tuple_0}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_10():
    string_0 = module_2.String()
    var_0 = module_0.to_json_schema(string_0)
    integer_0 = module_2.Integer()

def test_case_11():
    str_0 = 'allOf'
    str_1 = {str_0: str_0}
    str_2 = 'minLength'
    int_0 = 3135
    int_1 = {str_2: int_0}
    var_0 = [str_1, int_1]
    var_1 = {str_0: var_0}
    field_0 = module_0.from_json_schema(var_1)

def test_case_12():
    str_0 = 'if'
    str_1 = 'type'
    str_2 = 'integer'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.if_then_else_from_json_schema(str_4, schema_definitions_0)
    str_5 = 'then'
    str_6 = {str_1: str_2}
    str_7 = 'string'
    str_8 = {str_1: str_7}
    str_9 = {str_0: str_6, str_5: str_8}
    schema_definitions_1 = module_1.SchemaDefinitions()
    field_1 = module_0.if_then_else_from_json_schema(str_9, schema_definitions_1)

def test_case_13():
    str_0 = 'anyOf'
    str_1 = 'type'
    str_2 = 'integer'
    str_3 = {str_1: str_2}
    str_4 = 'string'
    str_5 = {str_1: str_4}
    str_6 = [str_3, str_5]
    str_7 = {str_0: str_6}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.any_of_from_json_schema(str_7, schema_definitions_0)
    int_0 = 0
    schema_definitions_1 = module_1.SchemaDefinitions()
    field_1 = module_0.any_of_from_json_schema(str_7, schema_definitions_1)
    var_0 = field_1.any_of[int_0]
    int_1 = 1
    schema_definitions_2 = module_1.SchemaDefinitions()
    field_2 = module_0.any_of_from_json_schema(str_7, schema_definitions_2)
    var_1 = field_2.any_of[int_1]

def test_case_14():
    str_0 = 'oneOf'
    str_1 = 'minimum'
    str_2 = 'maximum'
    str_3 = 'const'
    str_4 = 'integer'
    int_0 = 5
    int_1 = 10
    var_0 = {str_1: str_4, str_1: int_0, str_2: int_1, str_3: int_0}
    int_2 = 8
    int_3 = 9
    var_1 = {str_4: str_4, str_1: int_2, str_2: int_1, str_3: int_3}
    var_2 = {str_1: str_4, str_1: int_1, str_2: int_1, str_3: int_1}
    var_3 = [var_0, var_1, var_2]
    var_4 = {str_0: var_3}
    var_5 = None
    field_0 = module_0.one_of_from_json_schema(var_4, var_5)
    var_6 = field_0.one_of
    var_7 = len(var_6)

def test_case_15():
    str_0 = 'if'
    str_1 = 'integer'
    str_2 = {str_0: str_1}
    str_3 = {str_0: str_2}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.if_then_else_from_json_schema(str_3, schema_definitions_0)
    schema_definitions_1 = module_1.SchemaDefinitions()
    field_1 = module_0.if_then_else_from_json_schema(str_3, schema_definitions_1)

def test_case_16():
    str_0 = 'if'
    str_1 = 'integer'
    str_2 = {str_0: str_1}
    str_3 = {str_0: str_2}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.if_then_else_from_json_schema(str_3, schema_definitions_0)
    str_4 = 'then'
    str_5 = {str_1: str_1}
    str_6 = 'string'
    str_7 = {str_4: str_6}
    str_8 = {str_0: str_5, str_4: str_7}
    schema_definitions_1 = module_1.SchemaDefinitions()
    field_1 = module_0.if_then_else_from_json_schema(str_8, schema_definitions_1)

def test_case_17():
    str_0 = 'properties'
    str_1 = 'foo'
    str_2 = 'pI<Ker'
    str_3 = 'string'
    var_0 = {str_1: str_3}
    var_1 = {str_2: str_3, str_0: var_0}
    str_4 = 'object'
    bool_0 = False
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.from_json_schema_type(var_1, str_4, bool_0, schema_definitions_0)

def test_case_18():
    str_0 = '$ref'
    str_1 = '#/definitions/my_schema'
    str_2 = {str_0: str_1}
    schema_definitions_0 = module_1.SchemaDefinitions()
    int_0 = -14
    string_0 = module_2.String(min_length=int_0)
    boolean_0 = module_2.Boolean()
    field_0 = module_0.ref_from_json_schema(str_2, schema_definitions_0)

def test_case_19():
    bool_0 = True
    int_0 = 10
    str_0 = 'abc'
    str_1 = 'date'
    str_2 = 'a'
    str_3 = 'string field'
    string_0 = module_2.String(max_length=int_0, min_length=bool_0, pattern=str_0, format=str_1)
    var_0 = module_0.to_json_schema(string_0)
    field_0 = module_0.from_json_schema(var_0)

def test_case_20():
    str_0 = 'properties'
    str_1 = [str_0, str_0, str_0]
    str_2 = 'string'
    var_0 = {str_2: str_2}
    var_1 = {str_2: str_1, str_0: var_0}
    str_3 = 'object'
    bool_0 = False
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.from_json_schema_type(var_1, str_3, bool_0, schema_definitions_0)
    var_2 = module_0.to_json_schema(field_0)

def test_case_21():
    str_0 = 'required'
    str_1 = 'properties'
    str_2 = [str_1, str_1, str_0]
    str_3 = 'string'
    var_0 = {str_0: str_3}
    var_1 = {str_0: str_2, str_1: var_0}
    str_4 = 'object'
    bool_0 = False
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.from_json_schema_type(var_1, str_4, bool_0, schema_definitions_0)
    var_2 = module_0.to_json_schema(field_0)

def test_case_22():
    str_0 = 'rXuired'
    str_1 = 'properties'
    str_2 = 'type'
    str_3 = 'pattern'
    str_4 = 'fma'
    str_5 = 'string'
    int_0 = 0
    str_6 = '$TwQ_%wZ)ve5B'
    var_0 = {str_2: str_5, str_4: int_0, str_0: int_0, str_3: str_5, str_4: str_6}
    var_1 = {str_5: var_0}
    var_2 = {str_0: str_2, str_1: var_1}
    str_7 = 'object'
    bool_0 = True
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.from_json_schema_type(var_2, str_7, bool_0, schema_definitions_0)
    var_3 = module_0.to_json_schema(field_0)

def test_case_23():
    str_0 = 'Test'
    str_1 = 'test'
    int_0 = 10
    string_0 = module_2.String(max_length=int_0)
    string_1 = {str_1: string_0}
    schema_0 = module_1.Schema()
    var_0 = module_0.to_json_schema(schema_0)
    integer_0 = module_2.Integer(maximum=int_0)
    bool_0 = False
    array_0 = module_2.Array(integer_0, bool_0)
    var_1 = module_0.to_json_schema(array_0)
    string_2 = module_2.String(max_length=int_0)

def test_case_24():
    str_0 = 'not'
    str_1 = 'type'
    str_2 = 'null'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.not_from_json_schema(str_4, schema_definitions_0)
    var_0 = field_0.negated
    var_1 = module_0.to_json_schema(field_0)

def test_case_25():
    bool_0 = True
    string_0 = module_2.String(allow_blank=bool_0)
    int_0 = 11
    integer_0 = module_2.Integer(minimum=int_0)
    if_then_else_0 = module_3.IfThenElse(string_0, integer_0, integer_0)
    var_0 = module_0.to_json_schema(if_then_else_0)

def test_case_26():
    string_0 = module_2.String()
    var_0 = module_0.to_json_schema(string_0)
    integer_0 = module_2.Integer()
    var_1 = module_0.to_json_schema(integer_0)
    int_0 = 100
    bool_0 = True
    integer_1 = module_2.Integer(maximum=int_0, exclusive_maximum=bool_0)
    var_2 = module_0.to_json_schema(integer_1)
    str_0 = '^foo.*'
    var_3 = module_4.compile(str_0)
    string_1 = module_2.String()
    int_1 = 0
    integer_2 = module_2.Integer(minimum=int_1)
    int_2 = 10
    integer_3 = module_2.Integer(minimum=int_2)
    if_then_else_0 = module_3.IfThenElse(string_1, integer_2, integer_3)
    var_4 = module_0.to_json_schema(if_then_else_0)

def test_case_27():
    str_0 = 'Test'
    str_1 = 'test'
    int_0 = 10
    string_0 = module_2.String(max_length=int_0)
    string_1 = {str_1: string_0}
    schema_0 = module_1.Schema()
    var_0 = module_0.to_json_schema(schema_0)
    str_2 = '^test\\w+'
    string_2 = module_2.String(max_length=int_0)
    string_3 = {str_2: string_2}
    object_0 = module_2.Object(pattern_properties=string_3)
    var_1 = module_0.to_json_schema(object_0)
    var_2 = var_1

def test_case_28():
    string_0 = module_2.String()
    var_0 = module_0.to_json_schema(string_0)
    integer_0 = module_2.Integer()
    var_1 = module_0.to_json_schema(integer_0)
    int_0 = 100
    bool_0 = True
    integer_1 = module_2.Integer(maximum=int_0, exclusive_maximum=bool_0)
    var_2 = module_0.to_json_schema(integer_1)
    str_0 = '^foo.*'
    var_3 = module_4.compile(str_0)
    string_1 = module_2.String()
    any_0 = integer_1.get_default_value()
    int_1 = 0
    integer_2 = module_2.Integer(minimum=int_1)
    int_2 = 10
    integer_3 = module_2.Integer(minimum=int_2)
    if_then_else_0 = module_3.IfThenElse(string_1, integer_2, integer_3)
    bool_1 = True
    boolean_0 = module_2.Boolean(description=str_0, allow_null=bool_1)
    decimal_0 = module_5.Decimal()
    number_0 = module_2.Number(maximum=decimal_0, precision=str_0)
    var_4 = module_0.to_json_schema(boolean_0, number_0)

def test_case_29():
    str_0 = 'akengt'
    str_1 = 'fma'
    dict_0 = {}
    tuple_0 = module_0.get_valid_types(dict_0)
    str_2 = 'string'
    str_3 = 'Iext'
    str_4 = 'anOf'
    dict_1 = {str_3: str_1, str_4: str_0}
    schema_definitions_0 = module_1.SchemaDefinitions(**dict_1)
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    field_1 = module_0.from_json_schema(dict_0)
    bool_0 = True
    schema_definitions_1 = module_1.SchemaDefinitions()
    schema_definitions_2 = module_1.SchemaDefinitions()
    field_2 = module_0.from_json_schema_type(dict_0, str_2, bool_0, schema_definitions_2)
    var_0 = module_0.to_json_schema(field_2)