# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.fields as module_1

def test_case_0():
    pass

def test_case_1():
    schema_definitions_0 = module_0.SchemaDefinitions()

def test_case_2():
    schema_0 = module_0.Schema()
    schema_definitions_0 = module_0.SchemaDefinitions()
    iterator_0 = schema_definitions_0.__iter__()
    bool_0 = schema_0.__eq__(schema_0)
    int_0 = schema_0.__len__()
    schema_definitions_1 = module_0.SchemaDefinitions()

def test_case_3():
    str_0 = 'Q._J]~RG^D,5yq+z*mM>'
    str_1 = 'n8$.]Bpwoc#mFZ.U'
    dict_0 = {str_1: str_1, str_1: str_1}
    schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
    schema_definitions_0.__setitem__(str_0, str_0)

def test_case_4():
    schema_definitions_0 = module_0.SchemaDefinitions()
    str_0 = '-il{zF*'
    field_0 = module_1.Field(title=str_0, default=schema_definitions_0)
    module_0.set_definitions(field_0, schema_definitions_0)

def test_case_5():
    schema_0 = module_0.Schema()

def test_case_6():
    str_0 = '\\!Q=\ng0oa\x0b~&g-s0B]f'
    list_0 = [str_0, str_0]
    list_1 = [list_0]
    schema_0 = module_0.Schema(*list_1)

def test_case_7():
    schema_0 = module_0.Schema()
    str_0 = schema_0.__repr__()

def test_case_8():
    schema_0 = module_0.Schema()
    bool_0 = schema_0.__eq__(schema_0)

def test_case_9():
    schema_0 = module_0.Schema()
    str_0 = schema_0.__repr__()
    bool_0 = schema_0.__eq__(schema_0)
    iterator_0 = schema_0.__iter__()
    iterator_1 = schema_0.__iter__()
    int_0 = schema_0.__len__()
    bool_1 = schema_0.__eq__(iterator_1)
    iterator_2 = schema_0.__iter__()
    str_1 = 'anyOf'
    field_0 = module_1.Field(title=str_1)
    schema_definitions_0 = module_0.SchemaDefinitions()
    module_0.set_definitions(field_0, schema_definitions_0)
    iterator_3 = schema_0.__iter__()

def test_case_10():
    schema_0 = module_0.Schema()
    var_0 = list(schema_0)

def test_case_11():
    schema_0 = module_0.Schema()
    int_0 = schema_0.__len__()

def test_case_12():
    dict_0 = {}
    list_0 = [dict_0]
    schema_0 = module_0.Schema(*list_0)
    str_0 = schema_0.__repr__()
    int_0 = schema_0.__len__()
    iterator_0 = schema_0.__iter__()

def test_case_13():
    str_0 = 'F'
    reference_0 = module_0.Reference(str_0)
    str_1 = '_target'
    field_0 = module_1.Field()
    field_1 = {str_0: field_0}
    module_0.set_definitions(reference_0, field_1)
    reference_1 = module_0.Reference(str_0)
    var_0 = hasattr(reference_1, str_1)
    field_2 = module_1.Field()
    var_1 = hasattr(reference_1, str_1)

def test_case_14():
    str_0 = '~o'
    reference_0 = module_0.Reference(str_0)
    field_0 = module_1.Field()
    var_0 = reference_0.definitions
    module_0.set_definitions(reference_0, var_0)
    reference_1 = module_0.Reference(str_0)
    array_0 = module_1.Array(reference_1)
    var_1 = hasattr(reference_1, str_0)
    field_1 = module_1.Field()
    module_0.set_definitions(array_0, str_0)
    var_2 = hasattr(reference_1, str_0)
    field_2 = module_1.Field()
    var_3 = array_0

def test_case_15():
    str_0 = 'h]'
    list_0 = [str_0]
    schema_0 = module_0.Schema(*list_0)
    str_1 = schema_0.__repr__()
    dict_0 = {str_1: schema_0}
    int_0 = schema_0.__len__()
    field_0 = module_1.Field(title=str_1, description=str_1)
    reference_0 = module_0.Reference(str_1, dict_0)
    any_0 = reference_0.validate(schema_0)