# Automatically generated by Pynguin.
import ansible.playbook.base as module_0
import ansible.errors as module_1
import ansible.playbook.attribute as module_2

def test_case_0():
    try:
        bytes_0 = b'\xd2\xb8'
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.load_data(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.validate()
        list_0 = None
        int_0 = 867
        var_1 = field_attribute_base_0.load_data(list_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        base_0 = module_0.Base()
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.get_ds()
        var_1 = base_0.get_dep_chain()
        var_2 = field_attribute_base_0.dump_me()
        str_0 = 'tnuO3v?<'
        set_0 = {base_0}
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_3 = field_attribute_base_1.copy()
        field_attribute_base_2 = module_0.FieldAttributeBase()
        float_0 = -3766.0
        field_attribute_base_3 = module_0.FieldAttributeBase()
        var_4 = field_attribute_base_3.get_validated_value(str_0, set_0, field_attribute_base_2, float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        base_0 = module_0.Base()
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.serialize()
        var_1 = field_attribute_base_0.dump_attrs()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_2 = field_attribute_base_1.serialize()
        var_3 = field_attribute_base_0.get_variable_manager()
        var_4 = field_attribute_base_1.copy()
        list_0 = None
        var_5 = field_attribute_base_0.post_validate(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 600
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.from_attrs(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        tuple_0 = ()
        dict_0 = {field_attribute_base_0: field_attribute_base_0, field_attribute_base_0: field_attribute_base_0, tuple_0: field_attribute_base_0}
        var_0 = field_attribute_base_0.deserialize(dict_0)
        var_1 = field_attribute_base_0.dump_attrs()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_2 = field_attribute_base_1.squash()
        var_3 = field_attribute_base_1.dump_me(field_attribute_base_0)
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = ()
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.deserialize(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.validate()
        var_1 = field_attribute_base_0.validate()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        float_0 = 10.0
        var_2 = field_attribute_base_1.preprocess_data(float_0)
        var_3 = field_attribute_base_1.get_ds()
        list_0 = [var_0, field_attribute_base_0]
        var_4 = field_attribute_base_0.preprocess_data(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        base_0 = module_0.Base()
        var_0 = field_attribute_base_0.serialize()
        var_1 = field_attribute_base_0.dump_attrs()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        list_0 = []
        var_2 = field_attribute_base_1.load_data(list_0)
        var_3 = field_attribute_base_1.copy()
        var_4 = base_0.get_search_path()
        var_5 = field_attribute_base_1.dump_attrs()
        var_6 = base_0.get_path()
        str_0 = '4L'
        dict_0 = {str_0: var_0}
        base_meta_0 = module_0.BaseMeta(**dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'F@oP_X'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.from_attrs(dict_0)
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_1.get_ds()
        field_attribute_base_2 = module_0.FieldAttributeBase()
        var_2 = field_attribute_base_2.dump_me()
        var_3 = field_attribute_base_2.validate()
        base_0 = module_0.Base()
        var_4 = base_0.get_dep_chain()
        var_5 = field_attribute_base_2.validate()
        str_1 = 'barfoo'
        var_6 = field_attribute_base_2.squash()
        var_7 = field_attribute_base_2.serialize()
        var_8 = field_attribute_base_2.copy()
        int_0 = 463
        str_2 = '=f: j{/'
        var_9 = base_0.get_search_path()
        ansible_parser_error_0 = module_1.AnsibleParserError(field_attribute_base_2)
        var_10 = field_attribute_base_2.get_loader()
        field_attribute_0 = module_2.FieldAttribute(str_1, str_2, ansible_parser_error_0, base_0)
        var_11 = base_0.get_path()
        var_12 = field_attribute_base_2.get_validated_value(int_0, field_attribute_0, field_attribute_0, str_2)
        str_3 = 'ansible_discovered_interpreter_'
        float_0 = -55.51298
        var_13 = field_attribute_base_2.load_data(str_3, float_0, base_0)
    except BaseException:
        pass