# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.fields as module_1

def test_case_0():
    pass

def test_case_1():
    schema_definitions_0 = module_0.SchemaDefinitions()

def test_case_2():
    bool_0 = False
    field_0 = module_1.Field(allow_null=bool_0)
    schema_0 = module_0.Schema()
    list_0 = [schema_0]
    int_0 = schema_0.__len__()
    schema_definitions_0 = module_0.SchemaDefinitions(*list_0)
    iterator_0 = schema_definitions_0.__iter__()
    int_1 = schema_0.__len__()
    str_0 = schema_0.__repr__()

def test_case_3():
    list_0 = []
    schema_definitions_0 = module_0.SchemaDefinitions(*list_0)
    int_0 = schema_definitions_0.__len__()

def test_case_4():
    tuple_0 = ()
    schema_definitions_0 = module_0.SchemaDefinitions()
    schema_definitions_0.__setitem__(tuple_0, tuple_0)

def test_case_5():
    field_0 = module_1.Field()
    schema_definitions_0 = module_0.SchemaDefinitions()
    module_0.set_definitions(field_0, schema_definitions_0)

def test_case_6():
    schema_0 = module_0.Schema()

def test_case_7():
    bytes_0 = b'\x1c5PU\xa2\x0c5'
    list_0 = [bytes_0]
    schema_0 = module_0.Schema(*list_0)
    str_0 = schema_0.__repr__()

def test_case_8():
    schema_0 = module_0.Schema()
    str_0 = schema_0.__repr__()

def test_case_9():
    schema_0 = module_0.Schema()
    bool_0 = schema_0.__eq__(schema_0)

def test_case_10():
    bool_0 = False
    field_0 = module_1.Field(allow_null=bool_0)
    schema_0 = module_0.Schema()
    list_0 = [schema_0]
    schema_definitions_0 = module_0.SchemaDefinitions(*list_0)
    str_0 = schema_0.__repr__()

def test_case_11():
    schema_0 = module_0.Schema()
    var_0 = len(schema_0)

def test_case_12():
    tuple_0 = ()
    str_0 = 'P=%INO0{6!C'
    reference_0 = module_0.Reference(str_0)
    any_0 = reference_0.serialize(tuple_0)

def test_case_13():
    dict_0 = {}
    list_0 = [dict_0]
    schema_definitions_0 = module_0.SchemaDefinitions(*list_0)
    schema_0 = module_0.Schema(*list_0, **dict_0)
    iterator_0 = schema_0.__iter__()
    iterator_1 = schema_0.__iter__()
    schema_1 = module_0.Schema()
    int_0 = schema_1.__len__()
    schema_2 = module_0.Schema()
    str_0 = schema_2.__repr__()
    reference_0 = module_0.Reference(str_0, schema_definitions_0, **dict_0)
    schema_definitions_0.__setitem__(str_0, schema_2)
    int_1 = schema_definitions_0.__len__()
    iterator_2 = schema_definitions_0.__iter__()
    schema_3 = module_0.Schema(**dict_0)
    bool_0 = schema_3.__eq__(iterator_2)
    bool_1 = schema_3.__eq__(int_0)
    reference_1 = module_0.Reference(str_0, **dict_0)
    any_0 = reference_0.validate(dict_0)

def test_case_14():
    bool_0 = False
    field_0 = module_1.Field(allow_null=bool_0)
    dict_0 = {}
    schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
    list_0 = [dict_0]
    schema_0 = module_0.Schema(*list_0, **dict_0)
    module_0.set_definitions(field_0, schema_definitions_0)
    schema_1 = module_0.Schema()
    dict_1 = {field_0: schema_1}
    bool_1 = schema_1.__eq__(dict_1)
    list_1 = [schema_1]
    int_0 = schema_0.__len__()
    schema_definitions_1 = module_0.SchemaDefinitions(*list_1)
    iterator_0 = schema_definitions_0.__iter__()
    schema_2 = module_0.Schema(*list_1, **dict_0)
    iterator_1 = schema_1.__iter__()
    iterator_2 = schema_2.__iter__()
    schema_3 = module_0.Schema()
    int_1 = schema_3.__len__()
    schema_4 = module_0.Schema()
    str_0 = schema_4.__repr__()
    reference_0 = module_0.Reference(str_0, schema_definitions_0, **dict_0)
    schema_definitions_0.__setitem__(str_0, schema_0)
    bool_2 = schema_1.__eq__(schema_1)
    int_2 = schema_definitions_0.__len__()
    bool_3 = schema_2.__eq__(iterator_0)
    schema_definitions_2 = module_0.SchemaDefinitions(*list_1)
    schema_5 = module_0.Schema(**dict_0)
    bool_4 = schema_2.__eq__(iterator_1)
    bool_5 = schema_5.__eq__(int_2)
    bool_6 = True
    any_0 = reference_0.validate(dict_0, strict=bool_6)