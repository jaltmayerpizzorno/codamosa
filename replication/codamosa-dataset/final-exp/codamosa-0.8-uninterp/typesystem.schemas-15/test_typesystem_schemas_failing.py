# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        float_0 = 152.2322
        str_0 = '{\r0b;'
        dict_0 = {str_0: str_0}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
        any_0 = schema_definitions_0.__getitem__(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "\n    Doesn't ever match.\n    "
        str_1 = 'hd'
        field_0 = module_1.Field()
        schema_0 = module_0.Schema()
        schema_definitions_0 = module_0.SchemaDefinitions()
        bool_0 = False
        reference_0 = module_0.Reference(str_1)
        list_0 = [schema_definitions_0, str_0, schema_definitions_0, bool_0]
        schema_metaclass_0 = module_0.SchemaMetaclass(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        iterator_0 = None
        schema_0 = module_0.Schema()
        schema_definitions_0 = module_0.SchemaDefinitions()
        schema_definitions_0.__delitem__(iterator_0)
    except BaseException:
        pass

def test_case_3():
    try:
        schema_0 = module_0.Schema()
        str_0 = 'Dm}#gB'
        reference_0 = module_0.Reference(str_0)
        dict_0 = {str_0: str_0}
        schema_1 = module_0.Schema(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        schema_0 = module_0.Schema(*list_0)
        str_0 = schema_0.__repr__()
        str_1 = schema_0.__repr__()
        bool_0 = True
        any_0 = schema_0.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        reference_0 = module_0.Reference(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        validation_result_0 = None
        str_0 = 'Dm}#gB'
        reference_0 = module_0.Reference(str_0)
        any_0 = reference_0.serialize(validation_result_0)
        dict_0 = {str_0: str_0}
        schema_0 = module_0.Schema(**dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'sub'
        list_0 = [str_0, str_0]
        schema_0 = module_0.Schema(*list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = 1347.022
        list_0 = [float_0]
        str_0 = 'AQ"E}k1 p.v]\rF'
        str_1 = 'ccIo]0^\x0cqY]\r5T'
        dict_0 = {str_0: str_0, str_1: str_1}
        schema_0 = module_0.Schema(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = []
        schema_0 = module_0.Schema(*list_0)
        schema_1 = module_0.Schema()
        any_0 = schema_1.__getitem__(schema_0)
    except BaseException:
        pass

def test_case_10():
    try:
        list_0 = []
        str_0 = "\n    Doesn't ever match.\n    "
        str_1 = 'hd'
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.Field()
        schema_0 = module_0.Schema(*list_0)
        bool_0 = schema_0.__eq__(schema_definitions_0)
        schema_1 = module_0.Schema()
        str_2 = schema_1.__repr__()
        schema_definitions_1 = module_0.SchemaDefinitions()
        bool_1 = False
        reference_0 = module_0.Reference(str_1)
        list_1 = [schema_definitions_0, str_0, schema_definitions_1, bool_1]
        schema_metaclass_0 = module_0.SchemaMetaclass(*list_1)
    except BaseException:
        pass

def test_case_11():
    try:
        tuple_0 = ()
        str_0 = '\n^*g<33\\CRb1&:ib'
        reference_0 = module_0.Reference(str_0, str_0)
        any_0 = reference_0.validate(tuple_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '}S*cAKVD'
        reference_0 = module_0.Reference(str_0)
        bool_0 = False
        any_0 = reference_0.validate(reference_0, strict=bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = None
        str_0 = '#JjNR49uEM^U#Y}'
        dict_0 = {}
        reference_0 = module_0.Reference(str_0, **dict_0)
        any_0 = reference_0.validate(bool_0, strict=bool_0)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = []
        str_0 = "\n    Doesn't ever match.\n    "
        str_1 = 'hd'
        dict_0 = {str_0: list_0, str_1: list_0}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
        bool_0 = False
        schema_definitions_0.__setitem__(str_0, bool_0)
    except BaseException:
        pass

def test_case_15():
    try:
        list_0 = []
        str_0 = "\n    Doesn't ever match.\n    "
        str_1 = 'hd'
        dict_0 = {str_0: list_0, str_1: list_0}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
        schema_definitions_1 = module_0.SchemaDefinitions()
        field_0 = module_1.Field()
        module_0.set_definitions(field_0, schema_definitions_1)
        schema_0 = module_0.Schema(*list_0)
        iterator_0 = schema_0.__iter__()
        str_2 = schema_0.__repr__()
        schema_definitions_2 = module_0.SchemaDefinitions(**dict_0)
        reference_0 = module_0.Reference(str_1, schema_definitions_0)
        schema_definitions_3 = module_0.SchemaDefinitions(*list_0)
        any_0 = reference_0.serialize(schema_0)
        any_1 = reference_0.validate(schema_definitions_2)
    except BaseException:
        pass

def test_case_16():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'person'
        str_1 = 'Person'
        reference_0 = module_0.Reference(str_1)
        str_2 = 'people'
        str_3 = 'children'
        str_4 = 'Child'
        var_0 = schema_definitions_0.keys()
        schema_0 = module_0.Schema()
        bool_0 = schema_0.__eq__(str_2)
        reference_1 = module_0.Reference(str_4)
        reference_2 = None
        array_0 = module_1.Array(reference_2, bool_0)
        bool_1 = reference_1.has_default()
        str_5 = 'object'
        reference_3 = module_0.Reference(str_1)
        reference_4 = {str_0: reference_3}
        object_0 = module_1.Object(properties=reference_4)
        str_6 = 'nested'
        array_1 = module_1.Array(object_0)
        module_0.set_definitions(reference_0, schema_definitions_0)
        int_0 = schema_0.__len__()
        module_0.set_definitions(array_0, schema_definitions_0)
        str_7 = '\n    Must match all of the sub-items.\n\n    You should use custom validation instead.\n    '
        bool_2 = False
        field_0 = module_1.Field(title=str_7, allow_null=bool_2)
        module_0.set_definitions(field_0, schema_definitions_0)
        any_0 = reference_1.validate(field_0)
    except BaseException:
        pass

def test_case_17():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'Person'
        var_0 = schema_definitions_0.keys()
        reference_0 = module_0.Reference(str_0)
        str_1 = "5'"
        str_2 = 'children'
        str_3 = 'Child'
        schema_0 = module_0.Schema()
        bool_0 = schema_0.__eq__(str_1)
        reference_1 = module_0.Reference(str_3)
        array_0 = module_1.Array(reference_1)
        bool_1 = reference_1.has_default()
        str_4 = schema_0.__repr__()
        str_5 = 'object'
        reference_2 = module_0.Reference(str_0)
        reference_3 = {str_3: reference_2}
        object_0 = module_1.Object(properties=reference_3)
        array_1 = module_1.Array(object_0)
        module_0.set_definitions(reference_0, schema_definitions_0)
        int_0 = schema_0.__len__()
        module_0.set_definitions(array_0, schema_definitions_0)
        int_1 = schema_definitions_0.__len__()
        bool_2 = array_0.has_default()
        list_0 = [reference_1, int_1, reference_3]
        schema_metaclass_0 = module_0.SchemaMetaclass(*list_0)
    except BaseException:
        pass