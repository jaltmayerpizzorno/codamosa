# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.fields as module_1
import builtins as module_2

def test_case_0():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        any_0 = schema_definitions_0.__getitem__(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        field_0 = module_1.Field()
        union_0 = field_0.__or__(field_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        schema_0 = module_0.Schema()
        iterator_0 = schema_0.__iter__()
        int_0 = schema_definitions_0.__len__()
        schema_definitions_0.__setitem__(union_0, iterator_0)
        list_0 = [iterator_0]
        str_0 = schema_0.__repr__()
        int_1 = schema_0.__len__()
        reference_0 = module_0.Reference(str_0)
        bool_0 = schema_0.__eq__(int_1)
        schema_1 = module_0.Schema(*list_0)
        bool_1 = schema_1.__eq__(schema_1)
        any_0 = reference_0.serialize(schema_1)
        schema_2 = module_0.Schema()
        schema_3 = module_0.Schema()
        schema_definitions_0.__delitem__(iterator_0)
    except BaseException:
        pass

def test_case_2():
    try:
        schema_0 = module_0.Schema()
        iterator_0 = schema_0.__iter__()
        str_0 = schema_0.__repr__()
        str_1 = "*XO%T';~\x0buLaX"
        int_0 = schema_0.__len__()
        str_2 = "O4\t'\roPF4}jo"
        dict_0 = {str_2: iterator_0, str_1: schema_0, str_1: str_2, str_2: iterator_0, str_2: str_0}
        schema_1 = module_0.Schema(**dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        schema_0 = module_0.Schema()
        dict_0 = {}
        schema_1 = module_0.Schema(**dict_0)
        bool_1 = schema_1.__eq__(bool_0)
        schema_2 = module_0.Schema(**dict_0)
        any_0 = schema_2.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        bool_0 = False
        str_0 = 'T;Ocp'
        schema_0 = module_0.Schema()
        reference_0 = module_0.Reference(str_0, schema_0)
        any_0 = reference_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = None
        reference_0 = module_0.Reference(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '9? {'
        str_1 = '{[d+;3,tm|\x0bh'
        reference_0 = module_0.Reference(str_1)
        any_0 = reference_0.serialize(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = None
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = 'p Z0@d3>w\t/E&'
        reference_0 = module_0.Reference(str_0)
        any_0 = reference_0.validate(set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 2
        str_0 = 'n%G%'
        reference_0 = module_0.Reference(str_0)
        any_0 = reference_0.validate(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '@YNG`X\x0ck.yUts+\t'
        list_0 = [str_0, str_0, str_0, str_0]
        schema_0 = module_0.Schema(*list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        schema_0 = module_0.Schema()
        iterator_0 = schema_0.__iter__()
        list_0 = []
        str_0 = schema_0.__repr__()
        str_1 = 'j\x0c)*t$'
        str_2 = 'ET\x0c!oht~`ewQ}YbGR,'
        field_0 = module_1.Field(description=str_1, default=schema_0)
        dict_0 = {str_2: str_0, str_2: str_2}
        schema_definitions_0 = module_0.SchemaDefinitions(*list_0, **dict_0)
        module_0.set_definitions(field_0, schema_definitions_0)
        int_0 = schema_definitions_0.__len__()
        any_0 = schema_0.__getitem__(schema_0)
    except BaseException:
        pass

def test_case_11():
    try:
        field_0 = module_1.Field()
        union_0 = field_0.__or__(field_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        module_0.set_definitions(field_0, schema_definitions_0)
        schema_0 = module_0.Schema()
        iterator_0 = schema_0.__iter__()
        iterator_1 = schema_0.__iter__()
        list_0 = [iterator_0]
        str_0 = schema_0.__repr__()
        str_1 = 'ET\x0c!oht~`ewQ}YbGR,'
        str_2 = '[aS'
        int_0 = schema_0.__len__()
        set_0 = set()
        reference_0 = module_0.Reference(str_2, set_0)
        str_3 = "2I\r'[,l7gf-cQAbjDu"
        dict_0 = {str_3: list_0, str_0: field_0, str_3: str_1, str_1: list_0}
        schema_1 = module_0.Schema(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        field_0 = module_1.Field()
        union_0 = field_0.__or__(field_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        module_0.set_definitions(field_0, schema_definitions_0)
        schema_definitions_0.__setitem__(union_0, field_0)
        schema_0 = module_0.Schema()
        iterator_0 = schema_0.__iter__()
        int_0 = schema_definitions_0.__len__()
        schema_definitions_0.__setitem__(union_0, iterator_0)
    except BaseException:
        pass

def test_case_13():
    try:
        field_0 = module_1.Field()
        union_0 = field_0.__or__(field_0)
        list_0 = [field_0]
        type_0 = module_2.type(*list_0)
        reference_0 = module_0.Reference(type_0)
    except BaseException:
        pass

def test_case_14():
    try:
        field_0 = module_1.Field()
        union_0 = field_0.__or__(field_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        module_0.set_definitions(field_0, schema_definitions_0)
        schema_0 = module_0.Schema()
        int_0 = schema_definitions_0.__len__()
        int_1 = schema_definitions_0.__len__()
        str_0 = schema_0.__repr__()
        int_2 = schema_0.__len__()
        any_0 = field_0.get_default_value()
        reference_0 = module_0.Reference(str_0)
        bool_0 = schema_0.__eq__(int_2)
        any_1 = reference_0.serialize(any_0)
        any_2 = reference_0.validate(any_0)
    except BaseException:
        pass