# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.fields as module_1
import builtins as module_2

def test_case_0():
    try:
        str_0 = 'Schema'
        reference_0 = module_0.Reference(str_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        module_0.set_definitions(reference_0, schema_definitions_0)
        any_0 = schema_definitions_0.__getitem__(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        iterator_0 = schema_definitions_0.__iter__()
        schema_0 = module_0.Schema()
        str_0 = schema_0.__repr__()
        schema_definitions_1 = module_0.SchemaDefinitions()
        schema_definitions_1.__delitem__(iterator_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'SV,+4j9kl)VQ.'
        dict_0 = {str_0: str_0, str_0: str_0}
        schema_0 = module_0.Schema(**dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        schema_0 = module_0.Schema()
        any_0 = schema_0.__getitem__(schema_0)
    except BaseException:
        pass

def test_case_4():
    try:
        schema_0 = module_0.Schema()
        str_0 = schema_0.__repr__()
        schema_1 = module_0.Schema()
        reference_0 = module_0.Reference(str_0)
        any_0 = schema_1.__getitem__(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        str_0 = '{1.c_(fb{H \x0cN/KC~!'
        reference_0 = module_0.Reference(str_0)
        type_0 = None
        reference_1 = module_0.Reference(type_0)
    except BaseException:
        pass

def test_case_6():
    try:
        schema_definitions_0 = module_0.SchemaDefinitions()
        iterator_0 = schema_definitions_0.__iter__()
        list_0 = [schema_definitions_0, schema_definitions_0, iterator_0]
        schema_0 = module_0.Schema(*list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Mark'
        reference_0 = module_0.Reference(str_0)
        any_0 = reference_0.validate(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Schema'
        reference_0 = module_0.Reference(str_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        module_0.set_definitions(reference_0, schema_definitions_0)
        bool_0 = False
        any_0 = reference_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'jinja2.Markup'
        reference_0 = module_0.Reference(str_0)
        type_0 = None
        bool_0 = False
        any_0 = reference_0.validate(type_0, strict=bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        iterator_0 = None
        str_0 = 'L%:Eg]'
        field_0 = module_1.Field(description=str_0, default=iterator_0)
        schema_definitions_0 = None
        module_0.set_definitions(field_0, schema_definitions_0)
        list_0 = [iterator_0]
        str_1 = 'b~;\tB zrW6u\t['
        dict_0 = {str_1: str_1}
        reference_0 = module_0.Reference(str_1, dict_0)
        any_0 = reference_0.validate(list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        schema_0 = module_0.Schema()
        str_0 = schema_0.__repr__()
        bool_0 = schema_0.__eq__(schema_0)
        int_0 = schema_0.__len__()
        schema_definitions_0 = module_0.SchemaDefinitions()
        schema_definitions_0.__setitem__(str_0, bool_0)
        iterator_0 = schema_0.__iter__()
        str_1 = schema_0.__repr__()
        bool_1 = schema_0.__eq__(str_1)
        schema_definitions_0.__setitem__(str_1, str_1)
    except BaseException:
        pass

def test_case_12():
    try:
        schema_0 = module_0.Schema()
        bool_0 = schema_0.__eq__(schema_0)
        str_0 = schema_0.__repr__()
        int_0 = schema_0.__len__()
        list_0 = [int_0]
        str_1 = 'r'
        dict_0 = {str_1: bool_0, str_1: schema_0}
        schema_1 = module_0.Schema(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        schema_0 = module_0.Schema()
        bool_0 = schema_0.__eq__(schema_0)
        list_0 = [schema_0]
        schema_1 = module_0.Schema(*list_0)
        int_0 = schema_1.__len__()
        bool_1 = schema_0.__eq__(bool_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        schema_definitions_0.__setitem__(bool_1, schema_definitions_0)
        str_0 = 'jinja2.Markup'
        iterator_0 = schema_0.__iter__()
        reference_0 = module_0.Reference(str_0)
        type_0 = module_2.type(*list_0)
        reference_1 = module_0.Reference(str_0, type_0)
        any_0 = reference_1.validate(reference_1)
    except BaseException:
        pass

def test_case_14():
    try:
        schema_0 = module_0.Schema()
        bool_0 = schema_0.__eq__(schema_0)
        bool_1 = schema_0.__eq__(schema_0)
        list_0 = [schema_0]
        schema_1 = module_0.Schema(*list_0)
        int_0 = schema_1.__len__()
        bool_2 = schema_0.__eq__(bool_0)
        schema_definitions_0 = module_0.SchemaDefinitions()
        schema_definitions_0.__setitem__(bool_2, schema_definitions_0)
        str_0 = 'jinja2.Markup'
        iterator_0 = schema_0.__iter__()
        iterator_1 = schema_1.__iter__()
        reference_0 = module_0.Reference(str_0)
        type_0 = module_2.type(*list_0)
        reference_1 = module_0.Reference(str_0, type_0)
        any_0 = reference_1.validate(schema_0)
        bool_3 = False
        any_1 = reference_1.validate(list_0, strict=bool_3)
    except BaseException:
        pass