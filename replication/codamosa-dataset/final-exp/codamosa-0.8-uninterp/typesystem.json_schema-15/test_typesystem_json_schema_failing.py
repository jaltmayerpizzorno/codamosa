# Automatically generated by Pynguin.
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2
import typesystem.composites as module_3

def test_case_0():
    try:
        bool_0 = None
        field_0 = module_0.from_json_schema(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.enum_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'C)B'
        dict_0 = {str_0: str_0}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.from_json_schema(dict_0)
        field_1 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_0.to_json_schema(field_1)
        schema_definitions_1 = module_1.SchemaDefinitions()
        field_2 = module_0.const_from_json_schema(dict_0, schema_definitions_1)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = None
        dict_0 = {var_0: var_0, var_0: var_0}
        dict_1 = {var_0: var_0, var_0: var_0, var_0: var_0, var_0: dict_0}
        tuple_0 = module_0.get_valid_types(dict_1)
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.all_of_from_json_schema(dict_1, schema_definitions_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'C)B'
        dict_0 = {str_0: str_0}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.from_json_schema(dict_0)
        field_1 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_0.to_json_schema(field_1)
        schema_definitions_1 = module_1.SchemaDefinitions()
        field_2 = module_0.any_of_from_json_schema(dict_0, schema_definitions_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'M+uNf$c@1PzWs1x7t)V'
        dict_0 = {str_0: str_0, str_0: str_0}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.one_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_6():
    try:
        string_0 = module_2.String()
        schema_definitions_0 = module_1.SchemaDefinitions()
        dict_0 = {}
        field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        field_1 = module_0.not_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Hu\rM_U4Oa'
        str_1 = 'l)B'
        dict_0 = {str_1: str_1, str_0: str_0}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.from_json_schema(dict_0)
        field_1 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_0.to_json_schema(field_1)
        schema_definitions_1 = module_1.SchemaDefinitions()
        field_2 = module_0.if_then_else_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = None
        var_1 = module_0.to_json_schema(var_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'anyOf'
        str_1 = 'type'
        str_2 = {str_1: str_1}
        str_3 = 'integer'
        str_4 = {str_1: str_3}
        str_5 = [str_2, str_4]
        str_6 = {str_0: str_5}
        var_0 = None
        field_0 = module_0.any_of_from_json_schema(str_6, var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        schema_definitions_0 = module_1.SchemaDefinitions()
        dict_0 = {}
        field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_0.to_json_schema(field_0, dict_0)
        schema_definitions_1 = module_1.SchemaDefinitions()
        str_0 = 'y0lK"$V'
        bool_0 = False
        field_1 = module_2.Field(title=str_0, allow_null=bool_0)
        var_1 = module_0.to_json_schema(field_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'C)B'
        dict_0 = {str_0: str_0}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.from_json_schema(dict_0)
        field_1 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_0.to_json_schema(field_0)
        schema_definitions_1 = module_1.SchemaDefinitions()
        field_2 = module_0.not_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'if'
        dict_0 = {str_0: str_0, str_0: str_0}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\n    Build a typed field from a JSON schema reference object.\n    '
        reference_0 = module_1.Reference(str_0)
        str_1 = '$ref'
        str_2 = {str_1: str_1}
        reference_1 = {str_1: reference_0}
        field_0 = module_0.ref_from_json_schema(str_2, reference_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'if'
        str_1 = 'const'
        float_0 = 1164.218223
        set_0 = {float_0, str_0}
        dict_0 = {float_0: str_0, str_0: set_0, str_1: set_0, str_0: str_0}
        str_2 = '%Egq{rEE_AU4:e'
        str_3 = 'OGK)a\n'
        dict_1 = {str_2: str_2, str_2: str_0, str_3: dict_0}
        schema_definitions_0 = module_1.SchemaDefinitions(**dict_1)
        field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
        any_0 = module_2.Any()
        union_0 = any_0.__or__(field_0)
        field_1 = module_0.const_from_json_schema(dict_0, schema_definitions_0)
        object_0 = module_2.Object(properties=float_0, property_names=field_0, required=union_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'e\x0bco'
        bool_0 = True
        bool_1 = {str_0: bool_0}
        schema_definitions_0 = module_1.SchemaDefinitions()
        int_0 = schema_definitions_0.__len__()
        schema_definitions_0.__setitem__(int_0, bool_1)
        var_0 = module_0.to_json_schema(schema_definitions_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'type'
        str_1 = 'string'
        str_2 = {str_0: str_1}
        field_0 = module_0.from_json_schema(str_2)
        string_0 = module_2.String()
        str_3 = 'a'
        str_4 = [str_3]
        str_5 = {str_0: str_1, str_1: str_4}
        field_1 = module_0.from_json_schema(str_5)
        str_6 = [str_3]
        choice_0 = module_2.Choice(choices=str_6)
        str_7 = 'const'
        str_8 = {str_0: str_1, str_7: str_3}
        field_2 = module_0.from_json_schema(str_8)
        const_0 = module_2.Const(str_3)
        str_9 = '$ref'
        str_10 = '#/foo'
        str_11 = {str_9: str_10}
        field_3 = module_0.from_json_schema(str_11)
        reference_0 = module_1.Reference(str_10)
        str_12 = 'allOf'
        str_13 = {str_9: str_10}
        str_14 = [str_13]
        str_15 = {str_0: str_1, str_12: str_14}
        field_4 = module_0.from_json_schema(str_15)
        string_1 = module_2.String()
        var_0 = [reference_0, string_1]
        all_of_0 = module_3.AllOf(var_0)
        str_16 = 'anyOf'
        str_17 = {str_9: str_10}
        str_18 = [str_17]
        str_19 = {str_0: str_1, str_16: str_18}
        field_5 = module_0.from_json_schema(str_19)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'type'
        str_1 = 'string'
        str_2 = {str_0: str_1}
        field_0 = module_0.from_json_schema(str_2)
        string_0 = module_2.String()
        str_3 = 'enum'
        str_4 = 'a'
        str_5 = [str_4]
        str_6 = {str_0: str_1, str_3: str_5}
        field_1 = module_0.from_json_schema(str_6)
        str_7 = [str_4]
        choice_0 = module_2.Choice(choices=str_7)
        str_8 = 'const'
        str_9 = {str_0: str_1, str_8: str_4}
        field_2 = module_0.from_json_schema(str_9)
        const_0 = module_2.Const(str_4)
        str_10 = '$ref'
        str_11 = '#/foo'
        str_12 = {str_10: str_11}
        field_3 = module_0.from_json_schema(str_12)
        reference_0 = module_1.Reference(str_11)
        str_13 = 'allOf'
        str_14 = {str_10: str_11}
        str_15 = [str_14]
        str_16 = {str_0: str_1, str_13: str_15}
        field_4 = module_0.from_json_schema(str_16)
        reference_1 = module_1.Reference(str_11)
        string_1 = module_2.String()
        var_0 = [reference_1, string_1]
        all_of_0 = module_3.AllOf(var_0)
        str_17 = 'anyOf'
        str_18 = {str_10: str_11}
        str_19 = [str_18]
        str_20 = {str_0: str_1, str_17: str_19}
        field_5 = module_0.from_json_schema(str_20)
    except BaseException:
        pass

def test_case_18():
    try:
        dict_0 = None
        schema_definitions_0 = module_1.SchemaDefinitions()
        str_0 = 'b.pkATf-2G$d\t<j/{O\ri'
        reference_0 = module_1.Reference(str_0)
        var_0 = module_0.to_json_schema(reference_0, dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'oneOf'
        str_1 = 'default'
        str_2 = 'type'
        str_3 = 'string'
        str_4 = {str_3: str_0, str_0: str_0}
        str_5 = '+umbem'
        str_6 = {str_2: str_5}
        str_7 = [str_4, str_6]
        str_8 = 'Default string value'
        str_9 = {str_0: str_7, str_1: str_8}
        schema_definitions_0 = module_1.SchemaDefinitions()
        field_0 = module_0.one_of_from_json_schema(str_9, schema_definitions_0)
    except BaseException:
        pass

def test_case_20():
    try:
        string_0 = module_2.String()
        array_0 = module_2.Array(string_0)
        str_0 = "'1VSf'\\\t\nfR3xUcx("
        var_0 = module_0.to_json_schema(array_0)
        bool_0 = True
        bool_1 = False
        int_0 = 5
        string_1 = module_2.String(allow_blank=bool_0, trim_whitespace=bool_1, max_length=int_0, format=str_0)
        str_1 = 'y$X\x0b"z4:4m'
        var_1 = module_0.to_json_schema(str_1)
    except BaseException:
        pass