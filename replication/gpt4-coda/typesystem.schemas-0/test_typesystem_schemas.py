# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.fields as module_1

def test_case_0():
    pass

def test_case_1():
    schema_definitions_0 = module_0.SchemaDefinitions()

def test_case_2():
    list_0 = []
    schema_definitions_0 = module_0.SchemaDefinitions(*list_0)
    iterator_0 = schema_definitions_0.__iter__()
    schema_0 = module_0.Schema()

def test_case_3():
    schema_definitions_0 = module_0.SchemaDefinitions()
    int_0 = schema_definitions_0.__len__()

def test_case_4():
    str_0 = '$%^ssqJZd(U*HpJ(\x0b'
    schema_0 = module_0.Schema()
    iterator_0 = schema_0.__iter__()
    schema_1 = module_0.Schema()
    str_1 = schema_1.__repr__()
    str_2 = schema_1.__repr__()
    schema_definitions_0 = module_0.SchemaDefinitions()
    schema_definitions_0.__setitem__(str_0, str_0)
    reference_0 = module_0.Reference(str_2)

def test_case_5():
    field_0 = module_1.Field()
    schema_definitions_0 = module_0.SchemaDefinitions()
    module_0.set_definitions(field_0, schema_definitions_0)

def test_case_6():
    schema_0 = module_0.Schema()

def test_case_7():
    schema_0 = module_0.Schema()
    str_0 = schema_0.__repr__()

def test_case_8():
    schema_0 = module_0.Schema()
    bool_0 = schema_0.__eq__(schema_0)

def test_case_9():
    dict_0 = {}
    schema_0 = module_0.Schema(**dict_0)
    str_0 = schema_0.__repr__()
    bool_0 = schema_0.__eq__(str_0)
    list_0 = []
    schema_1 = module_0.Schema(*list_0, **dict_0)
    str_1 = schema_1.__repr__()
    int_0 = schema_1.__len__()
    schema_2 = module_0.Schema(*list_0, **dict_0)

def test_case_10():
    schema_0 = module_0.Schema()
    list_0 = [schema_0]
    str_0 = "f=J,'8(p\n-?[~3zOck"
    dict_0 = {str_0: schema_0}
    schema_definitions_0 = module_0.SchemaDefinitions(*list_0, **dict_0)

def test_case_11():
    schema_0 = module_0.Schema()
    int_0 = schema_0.__len__()

def test_case_12():
    str_0 = 'yFk>3AC'
    reference_0 = module_0.Reference(str_0)

def test_case_13():
    dict_0 = {}
    list_0 = [dict_0]
    schema_0 = module_0.Schema(*list_0)
    schema_1 = module_0.Schema()
    int_0 = schema_1.__len__()

def test_case_14():
    schema_definitions_0 = module_0.SchemaDefinitions()
    list_0 = [schema_definitions_0]
    schema_0 = module_0.Schema(*list_0)

def test_case_15():
    schema_definitions_0 = module_0.SchemaDefinitions()
    bool_0 = None
    str_0 = 'oKuDXw[Z\t3cQ'
    reference_0 = module_0.Reference(str_0)
    any_0 = reference_0.serialize(bool_0)
    str_1 = '%n(1>\\[>b;}.eQ<{+'
    field_0 = module_1.Field(title=str_1)

def test_case_16():
    schema_definitions_0 = module_0.SchemaDefinitions()
    str_0 = '9c]\r<kK_cF'
    reference_0 = module_0.Reference(str_0)
    module_0.set_definitions(reference_0, schema_definitions_0)

def test_case_17():
    schema_definitions_0 = module_0.SchemaDefinitions()
    str_0 = 'Person'
    reference_0 = module_0.Reference(str_0)
    array_0 = module_1.Array(reference_0)
    module_0.set_definitions(array_0, schema_definitions_0)

def test_case_18():
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.Field()
    str_0 = 'SimpleSchema'
    reference_0 = module_0.Reference(str_0)
    module_0.set_definitions(reference_0, schema_definitions_0)
    reference_1 = module_0.Reference(str_0, schema_definitions_0)
    module_0.set_definitions(reference_1, schema_definitions_0)

def test_case_19():
    schema_definitions_0 = module_0.SchemaDefinitions()
    str_0 = 'Person'
    reference_0 = module_0.Reference(str_0)
    module_0.set_definitions(reference_0, schema_definitions_0)
    reference_1 = module_0.Reference(str_0)
    reference_2 = None
    array_0 = module_1.Array(reference_2)
    int_0 = schema_definitions_0.__len__()
    module_0.set_definitions(array_0, schema_definitions_0)
    var_0 = array_0.items

def test_case_20():
    schema_definitions_0 = module_0.SchemaDefinitions()
    field_0 = module_1.Field()
    str_0 = 'Person'
    reference_0 = module_0.Reference(str_0)
    reference_1 = module_0.Reference(str_0)
    reference_2 = module_0.Reference(str_0)
    reference_3 = [reference_1, reference_2]
    array_0 = module_1.Array(reference_3)
    str_1 = 'person'
    reference_4 = module_0.Reference(str_0)
    reference_5 = {str_1: reference_4}
    object_0 = module_1.Object(properties=reference_5)
    module_0.set_definitions(reference_0, schema_definitions_0)
    module_0.set_definitions(array_0, schema_definitions_0)