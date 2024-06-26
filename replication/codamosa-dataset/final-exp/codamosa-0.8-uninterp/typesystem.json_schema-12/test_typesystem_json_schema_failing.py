# Automatically generated by Pynguin.
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2
import typesystem.composites as module_3

def test_case_0():
    try:
        str_0 = 'type'
        str_1 = 'properties'
        str_2 = 'ba]@se64_data'
        str_3 = 'string'
        str_4 = {str_0: str_2, str_1: str_3}
        field_0 = module_0.from_json_schema(str_4)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'VzLLjqEBb1x'
        dict_0 = {str_0: str_0, str_0: str_0}
        dict_1 = {}
        schema_definitions_0 = module_1.SchemaDefinitions(**dict_1)
        field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        dict_2 = {}
        iterator_0 = schema_definitions_0.__iter__()
        field_1 = module_0.ref_from_json_schema(dict_2, schema_definitions_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'VzLLjq>EBb1x'
        dict_0 = {str_0: str_0, str_0: str_0}
        dict_1 = {}
        schema_definitions_0 = module_1.SchemaDefinitions(**dict_1)
        field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_0.to_json_schema(field_0)
        field_1 = module_0.enum_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        tuple_0 = module_0.get_valid_types(dict_0)
        dict_1 = {}
        schema_definitions_0 = None
        field_0 = module_0.const_from_json_schema(dict_1, schema_definitions_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'allOf'
        str_1 = '$ref'
        str_2 = '#/definitions/Foo'
        str_3 = {str_1: str_2}
        str_4 = 'foo'
        str_5 = [str_3, str_2]
        str_6 = {str_0: str_5}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.all_of_from_json_schema(str_6, schema_definitions_0)
        any_0 = field_0.validate(str_4)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        schema_definitions_0 = None
        field_0 = module_0.any_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.one_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'not'
        str_1 = 'default'
        str_2 = 'type'
        str_3 = {str_2: str_0}
        int_0 = 5
        var_0 = {str_0: str_3, str_1: int_0}
        var_1 = None
        field_0 = module_0.not_from_json_schema(var_0, var_1)
    except BaseException:
        pass

def test_case_8():
    try:
        field_0 = None
        var_0 = module_0.to_json_schema(field_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        field_0 = module_2.Field(default=bool_0)
        var_0 = module_0.to_json_schema(field_0)
    except BaseException:
        pass

def test_case_10():
    try:
        any_0 = module_2.Any()
        var_0 = module_0.to_json_schema(any_0)
        never_match_0 = module_3.NeverMatch()
        var_1 = module_0.to_json_schema(never_match_0)
        bool_0 = True
        int_0 = 0
        int_1 = 100
        integer_0 = module_2.Integer(minimum=int_0, maximum=int_1)
        var_2 = module_0.to_json_schema(integer_0)
        float_0 = module_2.Float()
        var_3 = module_0.to_json_schema(bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'allOf'
        str_1 = '$ref'
        str_2 = '#/definitions/Foo'
        str_3 = {str_1: str_2}
        str_4 = 'const'
        str_5 = 'foo'
        str_6 = {str_4: str_5}
        str_7 = [str_3, str_6]
        str_8 = {str_0: str_7}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.all_of_from_json_schema(str_8, schema_definitions_0)
        any_0 = field_0.validate(str_5)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '$id'
        str_1 = 'allOf'
        str_2 = 'x'
        str_3 = '$ref'
        str_4 = 'y'
        str_5 = {str_3: str_4}
        str_6 = 'type'
        str_7 = 'minimum'
        str_8 = 'exclusiveMinimum'
        str_9 = 'number'
        int_0 = 3
        bool_0 = True
        var_0 = {str_6: str_9, str_7: int_0, str_8: bool_0}
        var_1 = [str_5, var_0]
        var_2 = {str_0: str_2, str_1: var_1}
        str_10 = 'maximum'
        str_11 = 'integer'
        int_1 = 2
        var_3 = {str_0: str_4, str_6: str_11, str_10: int_1}
        var_4 = {str_4: var_3}
        field_0 = module_0.all_of_from_json_schema(var_2, var_4)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'oneOf'
        str_1 = 'type'
        str_2 = 'minLength'
        str_3 = 'string'
        int_0 = 1
        var_0 = {str_1: str_3, str_2: int_0}
        str_4 = {str_1: str_0}
        var_1 = [var_0, str_4]
        var_2 = {str_0: var_1}
        var_3 = None
        field_0 = module_0.one_of_from_json_schema(var_2, var_3)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'allOf'
        str_1 = 'type'
        str_2 = 'number'
        str_3 = {str_1: str_2, str_0: str_1}
        int_0 = 1139
        var_0 = [str_3, int_0]
        var_1 = {str_0: var_0, str_1: int_0}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.all_of_from_json_schema(var_1, schema_definitions_0)
    except BaseException:
        pass

def test_case_15():
    try:
        any_0 = module_2.Any()
        var_0 = module_0.to_json_schema(any_0)
        never_match_0 = module_3.NeverMatch()
        var_1 = module_0.to_json_schema(never_match_0)
        integer_0 = module_2.Integer()
        var_2 = module_0.to_json_schema(integer_0)
        string_0 = module_2.String()
        int_0 = 1
        string_1 = module_2.String(min_length=int_0)
        var_3 = module_0.to_json_schema(string_1)
        str_0 = '\\d+'
        string_2 = module_2.String(pattern=str_0)
        var_4 = module_0.to_json_schema(string_2)
        str_1 = 'ipv4'
        string_3 = module_2.String(format=str_1)
        dict_0 = None
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '$ref'
        str_1 = 'type'
        str_2 = 'definitions'
        str_3 = '#/definitions/Pet'
        str_4 = 'object'
        str_5 = 'name'
        str_6 = 'Tiddles'
        str_7 = {str_5: str_6, str_1: str_2}
        str_8 = 'Fido'
        str_9 = 'Dog'
        str_10 = {str_5: str_8, str_1: str_9}
        str_11 = [str_7, str_10]
        str_12 = 'Pet'
        str_13 = 'properties'
        str_14 = 'string'
        str_15 = {str_1: str_14}
        str_16 = [str_9, str_14]
        str_17 = {str_0: str_16}
        str_18 = {str_5: str_15, str_1: str_17}
        str_19 = {str_1: str_4, str_13: str_18}
        str_20 = {str_12: str_19}
        str_21 = {str_0: str_3, str_1: str_4, str_0: str_11, str_2: str_20}
        field_0 = module_0.from_json_schema(str_21)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'type'
        str_1 = 'properties'
        str_2 = 'object'
        str_3 = 'string'
        str_4 = {str_0: str_2, str_1: str_3}
        field_0 = module_0.from_json_schema(str_4)
    except BaseException:
        pass