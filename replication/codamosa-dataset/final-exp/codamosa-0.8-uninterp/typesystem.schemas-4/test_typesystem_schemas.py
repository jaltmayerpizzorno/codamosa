# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.fields as module_1

def test_case_0():
    pass

def test_case_1():
    schema_definitions_0 = module_0.SchemaDefinitions()

def test_case_2():
    schema_definitions_0 = module_0.SchemaDefinitions()
    iterator_0 = schema_definitions_0.__iter__()
    schema_0 = module_0.Schema()
    int_0 = schema_0.__len__()

def test_case_3():
    list_0 = []
    str_0 = 'Jq=s&E-@D2TLe'
    dict_0 = {str_0: list_0, str_0: str_0}
    schema_definitions_0 = module_0.SchemaDefinitions(*list_0, **dict_0)
    schema_definitions_1 = module_0.SchemaDefinitions(*list_0)
    int_0 = schema_definitions_1.__len__()

def test_case_4():
    schema_definitions_0 = module_0.SchemaDefinitions()
    str_0 = 'TestReference'
    reference_0 = module_0.Reference(str_0)
    array_0 = module_1.Array(reference_0)
    module_0.set_definitions(array_0, schema_definitions_0)
    schema_definitions_0.__setitem__(str_0, schema_definitions_0)
    schema_definitions_1 = module_0.SchemaDefinitions()
    module_0.set_definitions(array_0, schema_definitions_1)

def test_case_5():
    field_0 = module_1.Field()
    schema_definitions_0 = None
    module_0.set_definitions(field_0, schema_definitions_0)

def test_case_6():
    schema_0 = module_0.Schema()

def test_case_7():
    str_0 = 'str'
    list_0 = [str_0]
    schema_0 = module_0.Schema(*list_0)

def test_case_8():
    schema_0 = module_0.Schema()
    str_0 = schema_0.__repr__()

def test_case_9():
    schema_0 = module_0.Schema()
    bool_0 = schema_0.__eq__(schema_0)

def test_case_10():
    schema_0 = module_0.Schema()
    int_0 = schema_0.__len__()

def test_case_11():
    schema_0 = module_0.Schema()
    var_0 = tuple(schema_0)

def test_case_12():
    dict_0 = {}
    list_0 = [dict_0]
    schema_definitions_0 = module_0.SchemaDefinitions()
    schema_0 = module_0.Schema(*list_0)

def test_case_13():
    str_0 = 'TestReference'
    reference_0 = module_0.Reference(str_0)
    array_0 = module_1.Array(reference_0)
    schema_definitions_0 = module_0.SchemaDefinitions()
    module_0.set_definitions(array_0, schema_definitions_0)

def test_case_14():
    schema_definitions_0 = module_0.SchemaDefinitions()
    str_0 = 'TestReference'
    reference_0 = module_0.Reference(str_0)
    array_0 = module_1.Array(reference_0)
    module_0.set_definitions(array_0, schema_definitions_0)
    schema_definitions_1 = module_0.SchemaDefinitions()
    module_0.set_definitions(array_0, schema_definitions_1)