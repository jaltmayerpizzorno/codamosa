# Automatically generated by Pynguin.
import ansible.playbook.base as module_0
import ansible.playbook.attribute as module_1

def test_case_0():
    pass

def test_case_1():
    base_0 = module_0.Base()

def test_case_2():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_me()

def test_case_3():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_ds()

def test_case_4():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()
    var_1 = field_attribute_base_0.squash()
    base_0 = module_0.Base()
    var_2 = field_attribute_base_0.get_loader()

def test_case_5():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_variable_manager()
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_1 = field_attribute_base_1.squash()

def test_case_6():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.validate()

def test_case_7():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.squash()

def test_case_8():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.copy()

def test_case_9():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    bool_0 = True
    var_0 = None
    str_0 = 'G?dint'
    int_0 = 99
    field_attribute_0 = module_1.FieldAttribute(str_0, int_0, bool_0)
    var_1 = field_attribute_base_0.get_validated_value(str_0, field_attribute_0, str_0, var_0)

def test_case_10():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_attrs()

def test_case_11():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    set_0 = None
    str_0 = None
    dict_0 = {str_0: set_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = field_attribute_base_0.from_attrs(dict_0)
    var_1 = field_attribute_base_0.dump_me()

def test_case_12():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()

def test_case_13():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    bytes_0 = b'\xc0\xf1r\xe2Tmb\x9b\\\xe2'
    var_0 = field_attribute_base_0.validate(bytes_0)
    dict_0 = {bytes_0: var_0, var_0: field_attribute_base_0, field_attribute_base_0: var_0, var_0: field_attribute_base_0, var_0: field_attribute_base_0}
    var_1 = field_attribute_base_0.deserialize(dict_0)

def test_case_14():
    base_0 = module_0.Base()
    var_0 = base_0.get_search_path()

def test_case_15():
    base_0 = module_0.Base()
    var_0 = base_0.get_dep_chain()

def test_case_16():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_loader()
    str_0 = 'name_1'
    str_1 = 'strin_'
    var_1 = field_attribute_base_0.squash()
    bool_0 = True
    field_attribute_0 = module_1.FieldAttribute(str_1, str_1, bool_0)
    var_2 = None
    var_3 = field_attribute_base_0.get_validated_value(str_0, field_attribute_0, str_0, var_2)
    var_4 = field_attribute_base_0.squash()
    str_2 = 'name_2'
    str_3 = '\n\\$'
    int_0 = -350
    field_attribute_1 = module_1.FieldAttribute(str_3, int_0, bool_0)
    str_4 = '123(%'
    var_5 = field_attribute_base_0.get_validated_value(str_2, field_attribute_1, str_4, var_2)
    var_6 = field_attribute_base_0.dump_me()
    var_7 = field_attribute_base_0.copy()
    var_8 = field_attribute_base_0.validate()

def test_case_17():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    set_0 = set()
    dict_0 = {}
    var_0 = field_attribute_base_0.load_data(set_0, dict_0)
    var_1 = field_attribute_base_0.serialize()

def test_case_18():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    bool_0 = True
    var_0 = None
    str_0 = 'G?dint'
    int_0 = 99
    str_1 = 'strimg'
    str_2 = '8dHM=E6LJ!'
    dict_0 = {str_1: field_attribute_base_0, str_2: int_0}
    var_1 = field_attribute_base_0.validate(dict_0)
    field_attribute_0 = module_1.FieldAttribute(str_0, int_0, bool_0)
    var_2 = field_attribute_base_0.get_validated_value(str_0, field_attribute_0, str_0, var_0)
    var_3 = field_attribute_base_0.validate(field_attribute_base_0)

def test_case_19():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    str_0 = 'name_1'
    str_1 = 'string'
    str_2 = 'placeholder'
    bool_0 = True
    field_attribute_0 = module_1.FieldAttribute(str_1, str_2, bool_0)
    str_3 = 'value'
    var_0 = None
    var_1 = field_attribute_base_0.get_validated_value(str_0, field_attribute_0, str_3, var_0)
    str_4 = 'name_2'
    str_5 = 'int'
    int_0 = 99
    field_attribute_1 = module_1.FieldAttribute(str_5, int_0, bool_0)
    str_6 = '123'
    var_2 = field_attribute_base_0.get_validated_value(str_4, field_attribute_1, str_6, var_0)
    var_3 = field_attribute_base_0.validate()

def test_case_20():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    str_0 = 'name_1'
    str_1 = 'string'
    str_2 = 'placeholder'
    bool_0 = True
    field_attribute_0 = module_1.FieldAttribute(str_1, str_2, bool_0)
    str_3 = 'value'
    var_0 = None
    var_1 = field_attribute_base_0.get_validated_value(str_0, field_attribute_0, str_3, var_0)
    str_4 = 'name_2'
    str_5 = 'int'
    int_0 = 99
    field_attribute_1 = module_1.FieldAttribute(str_5, int_0, bool_0)
    str_6 = '123'
    var_2 = field_attribute_base_0.get_validated_value(str_4, field_attribute_1, str_6, var_0)
    str_7 = 'name_3'
    str_8 = 'float'
    float_0 = 4.4
    field_attribute_2 = module_1.FieldAttribute(str_8, float_0, bool_0)
    str_9 = '12.3'
    var_3 = field_attribute_base_0.get_validated_value(str_7, field_attribute_2, str_9, var_0)