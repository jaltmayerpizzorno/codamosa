# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        list_0 = None
        schema_definitions_0 = module_0.SchemaDefinitions()
        any_0 = schema_definitions_0.__getitem__(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        schema_definitions_0 = module_0.SchemaDefinitions()
        int_0 = schema_definitions_0.__len__()
        schema_0 = module_0.Schema(*list_0)
        iterator_0 = schema_0.__iter__()
        int_1 = schema_0.__len__()
        str_0 = '1xeNL!}C@'
        reference_0 = module_0.Reference(str_0)
        any_0 = reference_0.serialize(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'U+(|$KO@@$'
        schema_definitions_0 = module_0.SchemaDefinitions()
        iterator_0 = schema_definitions_0.__iter__()
        reference_0 = module_0.Reference(str_0)
        list_0 = [reference_0, str_0]
        str_1 = 'aW?{rOP<C&pE\n#u5c/g'
        dict_0 = {str_0: list_0, str_1: str_1}
        schema_definitions_0.__delitem__(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "EtGZD'/9br2VT2\x0bz%\n}^"
        field_0 = None
        str_1 = 'gamfwdh6CR8\x0cty18;at'
        dict_0 = {str_0: field_0, str_0: field_0, str_1: str_1}
        schema_0 = module_0.Schema(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -638
        schema_0 = module_0.Schema()
        any_0 = schema_0.__getitem__(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = None
        reference_0 = module_0.Reference(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n    test __setitem__ of class SchemaDefinitions\n    '
        reference_0 = module_0.Reference(str_0)
        any_0 = reference_0.validate(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0]
        schema_0 = module_0.Schema(*list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '\nD;v>=U:Ry,'
        dict_0 = {}
        reference_0 = module_0.Reference(str_0, **dict_0)
        list_0 = [dict_0]
        schema_0 = module_0.Schema(*list_0)
        any_0 = schema_0.__getitem__(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        list_0 = [schema_definitions_0]
        str_0 = 'May not contain additional items.'
        dict_0 = {str_0: list_0, str_0: list_0, str_0: schema_definitions_0}
        schema_0 = module_0.Schema(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        any_0 = None
        schema_0 = module_0.Schema()
        bool_0 = schema_0.__eq__(any_0)
        list_0 = [any_0]
        int_0 = schema_0.__len__()
        schema_1 = module_0.Schema(*list_0)
        iterator_0 = schema_1.__iter__()
        str_0 = schema_1.__repr__()
        schema_2 = module_0.Schema(*list_0)
        reference_0 = module_0.Reference(str_0)
        any_1 = reference_0.validate(any_0)
    except BaseException:
        pass

def test_case_11():
    try:
        set_0 = set()
        list_0 = []
        schema_definitions_0 = module_0.SchemaDefinitions()
        int_0 = schema_definitions_0.__len__()
        schema_0 = module_0.Schema(*list_0)
        iterator_0 = schema_0.__iter__()
        bool_0 = True
        bool_1 = None
        field_0 = module_1.Field(allow_null=bool_1)
        module_0.set_definitions(field_0, schema_definitions_0)
        int_1 = schema_0.__len__()
        str_0 = '1xeNL!}C@'
        field_1 = module_1.Field(title=str_0, default=bool_0)
        bool_2 = False
        bool_3 = True
        dict_0 = {str_0: set_0}
        reference_0 = module_0.Reference(str_0, dict_0)
        any_0 = reference_0.validate(bool_2, strict=bool_3)
    except BaseException:
        pass

def test_case_12():
    try:
        any_0 = None
        list_0 = [any_0]
        schema_0 = module_0.Schema(*list_0)
        iterator_0 = schema_0.__iter__()
        str_0 = schema_0.__repr__()
        schema_1 = module_0.Schema(*list_0)
        reference_0 = module_0.Reference(str_0)
        any_1 = reference_0.validate(any_0)
    except BaseException:
        pass

def test_case_13():
    try:
        set_0 = set()
        str_0 = '\nD;v>=U:Ry,'
        dict_0 = {}
        reference_0 = module_0.Reference(str_0, **dict_0)
        any_0 = reference_0.serialize(set_0)
        str_1 = ' for '
        any_1 = reference_0.serialize(any_0)
        list_0 = [str_1]
        schema_0 = module_0.Schema(*list_0)
        bool_0 = schema_0.__eq__(set_0)
        str_2 = schema_0.__repr__()
        bytes_0 = None
        reference_1 = module_0.Reference(str_2, bytes_0)
        list_1 = []
        schema_definitions_0 = module_0.SchemaDefinitions()
        int_0 = schema_definitions_0.__len__()
        schema_1 = module_0.Schema(*list_1)
        iterator_0 = schema_1.__iter__()
        field_0 = module_1.Field(allow_null=bool_0)
        int_1 = schema_1.__len__()
        module_0.set_definitions(field_0, schema_definitions_0)
        any_2 = reference_0.serialize(iterator_0)
        str_3 = "?'^\x0bEq6Fq.M5aqI!"
        reference_2 = module_0.Reference(str_3)
        dict_1 = {}
        any_3 = reference_0.serialize(bytes_0)
        reference_3 = module_0.Reference(str_3, **dict_1)
        any_4 = schema_1.__getitem__(schema_1)
    except BaseException:
        pass

def test_case_14():
    try:
        set_0 = set()
        str_0 = '\nD;v>=U:Ry,'
        dict_0 = {str_0: set_0}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
        schema_definitions_0.__setitem__(str_0, str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'Target'
        reference_0 = module_0.Reference(str_0)
        str_1 = 'field_1'
        reference_1 = {str_1: reference_0}
        object_0 = module_1.Object(properties=reference_1)
        module_0.set_definitions(object_0, schema_definitions_0)
        array_0 = module_1.Array(reference_0)
        module_0.set_definitions(array_0, schema_definitions_0)
        reference_2 = module_0.Reference(str_0)
        object_1 = module_1.Object(properties=str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'fi1ld_@'
        reference_0 = module_0.Reference(str_0)
        module_0.set_definitions(reference_0, schema_definitions_0)
        object_0 = module_1.Object(properties=str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'Target'
        reference_0 = module_0.Reference(str_0)
        str_1 = 'field_1'
        reference_1 = {str_1: reference_0}
        object_0 = module_1.Object(properties=reference_1)
        array_0 = module_1.Array(reference_0)
        module_0.set_definitions(array_0, schema_definitions_0)
        reference_2 = module_0.Reference(str_0)
        object_1 = module_1.Object(properties=str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        set_0 = set()
        str_0 = '\nD;v>=U:Ry,'
        dict_0 = {}
        reference_0 = module_0.Reference(str_0, **dict_0)
        any_0 = reference_0.serialize(set_0)
        list_0 = [any_0]
        schema_0 = module_0.Schema(*list_0)
        str_1 = ' for '
        any_1 = reference_0.serialize(any_0)
        list_1 = [str_1]
        schema_1 = module_0.Schema()
        str_2 = schema_1.__repr__()
        schema_2 = module_0.Schema(*list_1)
        str_3 = 'uuid'
        field_0 = module_1.Field()
        dict_1 = {str_3: field_0}
        object_0 = module_1.Object(pattern_properties=dict_1, additional_properties=field_0)
        list_2 = [object_0, any_1, schema_2, any_0]
        schema_metaclass_0 = module_0.SchemaMetaclass(*list_2)
    except BaseException:
        pass