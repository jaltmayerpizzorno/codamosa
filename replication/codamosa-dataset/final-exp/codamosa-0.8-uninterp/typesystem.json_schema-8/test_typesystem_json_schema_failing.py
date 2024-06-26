# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2
import typesystem.composites as module_3
import decimal as module_4

def test_case_0():
    try:
        list_0 = []
        schema_definitions_0 = module_0.SchemaDefinitions(*list_0)
        iterator_0 = schema_definitions_0.__iter__()
        dict_0 = {iterator_0: list_0}
        str_0 = '>||'
        bool_0 = None
        field_0 = module_1.from_json_schema_type(dict_0, str_0, bool_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_1():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        iterator_0 = schema_definitions_0.__iter__()
        dict_0 = {iterator_0: iterator_0}
        field_0 = module_1.enum_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'A'
        dict_0 = {str_0: str_0}
        dict_1 = {str_0: dict_0}
        field_0 = module_1.from_json_schema(dict_0)
        dict_2 = module_1.get_standard_properties(field_0)
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_1)
        field_1 = module_1.all_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_3():
    try:
        string_0 = module_2.String()
        boolean_0 = module_2.Boolean()
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        choice_0 = module_2.Choice()
        var_0 = module_1.to_json_schema(choice_0)
        field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        field_1 = module_1.any_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.one_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'not'
        var_0 = {str_0: str_0}
        field_0 = module_1.not_from_json_schema(var_0, var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        var_0 = module_1.to_json_schema(schema_definitions_0)
        str_0 = 'al,ow_blank'
        bool_0 = None
        dict_0 = {}
        dict_1 = {str_0: bool_0}
        field_0 = module_1.from_json_schema(dict_1)
        field_1 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        field_2 = module_1.if_then_else_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -2215
        var_0 = module_1.to_json_schema(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        field_0 = module_1.from_json_schema(dict_0)
        int_0 = -2244
        dict_1 = {int_0: int_0, int_0: int_0, int_0: int_0}
        schema_definitions_0 = None
        field_1 = module_1.type_from_json_schema(dict_1, schema_definitions_0)
        dict_2 = module_1.get_standard_properties(field_1)
        var_0 = module_1.to_json_schema(field_0, dict_0)
        field_2 = None
        var_1 = module_1.to_json_schema(field_2, dict_1)
    except BaseException:
        pass

def test_case_9():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        var_0 = module_1.to_json_schema(list_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'J\x0c'
        field_0 = module_2.Field(description=str_0)
        var_0 = module_1.to_json_schema(field_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'allOf'
        str_1 = 'anyOf'
        str_2 = 'oneOf'
        str_3 = 'default'
        str_4 = 'definitions'
        str_5 = '$ref'
        str_6 = '#/definitions/User'
        str_7 = {str_5: str_6}
        str_8 = 'type'
        str_9 = 'object'
        str_10 = {str_8: str_1}
        str_11 = {str_3: str_10}
        str_12 = {str_8: str_9, str_4: str_11}
        str_13 = [str_7, str_12]
        str_14 = 'string'
        str_15 = {str_8: str_14}
        str_16 = [str_15]
        str_17 = 'additionalProperties'
        var_0 = {}
        bool_0 = True
        var_1 = {str_8: str_9, str_14: var_0, str_17: bool_0}
        str_18 = 'items'
        str_19 = 'array'
        str_20 = '#'
        str_21 = {str_5: str_20}
        str_22 = {str_8: str_19, str_18: str_21}
        var_2 = [var_1, str_22]
        str_23 = 'tim'
        str_24 = 'User'
        var_3 = {}
        var_4 = {str_8: str_9, str_6: var_3}
        var_5 = {str_24: var_4}
        var_6 = {str_0: str_13, str_1: str_16, str_2: var_2, str_3: str_23, str_4: var_5}
        var_7 = None
        field_0 = module_1.one_of_from_json_schema(var_6, var_7)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'type'
        str_1 = 'items'
        str_2 = 'array'
        var_0 = {}
        var_1 = {str_0: str_2, str_1: var_0}
        field_0 = module_1.from_json_schema(var_1)
        field_1 = module_1.from_json_schema(str_2)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '$ref'
        str_1 = {str_0: str_0}
        var_0 = {}
        field_0 = module_1.ref_from_json_schema(str_1, var_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'oneOf'
        str_1 = 'const'
        int_0 = 1
        int_1 = {str_1: int_0}
        int_2 = 2
        int_3 = {str_1: int_2}
        int_4 = [int_1, int_3]
        int_5 = {str_0: int_4}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.one_of_from_json_schema(int_5, schema_definitions_0)
        any_0 = field_0.validate(int_0)
        any_1 = field_0.validate(int_2)
        int_6 = 3
        any_2 = field_0.validate(int_6)
    except BaseException:
        pass

def test_case_15():
    try:
        field_0 = None
        list_0 = [field_0, field_0, field_0]
        all_of_0 = module_3.AllOf(list_0)
        var_0 = module_1.to_json_schema(all_of_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'if'
        str_1 = 'deault'
        str_2 = 'tyXjpe'
        str_3 = 'string'
        str_4 = {str_2: str_3}
        str_5 = {str_2: str_1}
        str_6 = 'c'
        str_7 = {str_0: str_4, str_6: str_4, str_6: str_5, str_1: str_6}
        var_0 = None
        field_0 = module_1.if_then_else_from_json_schema(str_7, var_0)
        var_1 = field_0.if_clause
        var_2 = field_0.then_clause
        str_8 = 'tnf'
        validation_error_0 = field_0.validation_error(str_8)
    except BaseException:
        pass

def test_case_17():
    try:
        list_0 = []
        dict_0 = {}
        decimal_0 = module_4.Decimal(*list_0, **dict_0)
        integer_0 = module_2.Integer(maximum=decimal_0, multiple_of=decimal_0, **dict_0)
        var_0 = module_1.to_json_schema(integer_0)
        str_0 = '3?2Ne>r&hOCqEnP~'
        field_0 = module_2.Field(title=str_0, default=var_0)
        bool_0 = field_0.has_default()
        var_1 = module_1.to_json_schema(field_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = -2224
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_1.to_json_schema(field_0)
        field_1 = module_1.from_json_schema(dict_0)
        dict_1 = module_1.get_standard_properties(field_1)
        list_0 = [field_0, field_1, field_0, field_0]
        all_of_0 = module_3.AllOf(list_0)
        var_1 = module_1.to_json_schema(all_of_0)
        field_2 = module_1.ref_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass