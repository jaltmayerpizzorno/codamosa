# Automatically generated by Pynguin.
import ansible.playbook.base as module_0
import ansible.errors as module_1
import ansible.playbook.attribute as module_2

def test_case_0():
    pass

def test_case_1():
    base_0 = module_0.Base()

def test_case_2():
    field_attribute_base_0 = module_0.FieldAttributeBase()

def test_case_3():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_me()

def test_case_4():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_ds()

def test_case_5():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_loader()

def test_case_6():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_variable_manager()

def test_case_7():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.validate()

def test_case_8():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.squash()

def test_case_9():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.copy()

def test_case_10():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_attrs()

def test_case_11():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_variable_manager()
    base_0 = module_0.Base()
    dict_0 = {base_0: field_attribute_base_0}
    var_1 = field_attribute_base_0.from_attrs(dict_0)

def test_case_12():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()

def test_case_13():
    base_0 = module_0.Base()
    var_0 = base_0.get_search_path()

def test_case_14():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    dict_0 = {}
    var_0 = field_attribute_base_0.validate(dict_0)

def test_case_15():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    dict_0 = {}
    var_0 = field_attribute_base_0.load_data(dict_0)

def test_case_16():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_me()
    var_1 = field_attribute_base_0.validate()
    base_0 = module_0.Base()
    var_2 = base_0.get_dep_chain()
    var_3 = field_attribute_base_0.validate()
    str_0 = 'barfoo'
    var_4 = field_attribute_base_0.squash()
    var_5 = field_attribute_base_0.serialize()
    var_6 = field_attribute_base_0.copy()
    int_0 = 463
    str_1 = '=f: j{/'
    var_7 = base_0.get_search_path()
    ansible_parser_error_0 = module_1.AnsibleParserError(field_attribute_base_0)
    base_1 = module_0.Base()
    var_8 = ansible_parser_error_0.__str__()
    var_9 = field_attribute_base_0.get_loader()
    field_attribute_0 = module_2.FieldAttribute(str_0, str_1, ansible_parser_error_0, base_1)
    var_10 = field_attribute_base_0.squash()
    var_11 = base_1.get_dep_chain()
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_12 = field_attribute_base_1.get_validated_value(int_0, field_attribute_0, field_attribute_0, str_1)

def test_case_17():
    str_0 = 'F@oP_X'
    str_1 = 'c'
    int_0 = 463
    field_attribute_base_0 = module_0.FieldAttributeBase()
    ansible_parser_error_0 = module_1.AnsibleParserError(field_attribute_base_0)
    base_0 = module_0.Base()
    field_attribute_0 = module_2.FieldAttribute(str_0, str_1, ansible_parser_error_0, base_0)
    var_0 = base_0.get_dep_chain()
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_1 = field_attribute_base_1.get_validated_value(int_0, field_attribute_0, field_attribute_0, str_0)