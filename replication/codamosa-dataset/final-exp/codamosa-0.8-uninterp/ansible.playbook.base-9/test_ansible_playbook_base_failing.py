# Automatically generated by Pynguin.
import ansible.playbook.base as module_0

def test_case_0():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.dump_attrs()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_1.copy()
        dict_0 = None
        str_0 = 'media_select'
        var_2 = field_attribute_base_1.load_data(dict_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        base_0 = module_0.Base()
        str_0 = 'gE9{|\rSx4#'
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.load_data(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = None
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        int_0 = -874
        list_0 = [int_0, dict_0]
        list_1 = [float_0, dict_0, dict_0, int_0]
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.get_validated_value(dict_0, int_0, list_0, list_1)
    except BaseException:
        pass

def test_case_3():
    try:
        base_0 = module_0.Base()
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.post_validate(base_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xb7\xa0\xfd\xef\xae\x8d\xb1a\xb6'
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.deserialize(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.get_ds()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_1.copy()
        base_0 = module_0.Base()
        var_2 = field_attribute_base_1.dump_me(field_attribute_base_1)
    except BaseException:
        pass

def test_case_6():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.get_ds()
        var_1 = field_attribute_base_0.dump_attrs()
        str_0 = '1TVI8'
        dict_0 = {str_0: var_0}
        var_2 = field_attribute_base_0.from_attrs(dict_0)
        var_3 = field_attribute_base_0.serialize()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_4 = field_attribute_base_1.dump_me()
        var_5 = field_attribute_base_0.squash()
        base_0 = module_0.Base()
        var_6 = base_0.get_path()
        set_0 = set()
        var_7 = field_attribute_base_1.load_data(set_0)
        var_8 = field_attribute_base_1.get_variable_manager()
        var_9 = field_attribute_base_0.validate()
        var_10 = field_attribute_base_1.copy()
        str_1 = 'MRKRp\x0c7D'
        str_2 = '\nW&G 8}'
        dict_1 = {str_1: var_1, str_2: field_attribute_base_1}
        list_0 = [field_attribute_base_1, dict_1, dict_1]
        base_meta_0 = module_0.BaseMeta(*list_0)
    except BaseException:
        pass