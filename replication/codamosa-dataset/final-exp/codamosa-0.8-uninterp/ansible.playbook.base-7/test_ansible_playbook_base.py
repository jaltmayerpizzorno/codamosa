# Automatically generated by Pynguin.
import ansible.playbook.base as module_0

def test_case_0():
    pass

def test_case_1():
    base_0 = module_0.Base()
    var_0 = base_0.get_search_path()

def test_case_2():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.dump_me()

def test_case_3():
    base_0 = module_0.Base()
    var_0 = base_0.get_path()
    int_0 = 2027
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_1 = field_attribute_base_0.preprocess_data(int_0)

def test_case_4():
    dict_0 = {}
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.load_data(dict_0)
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_1 = field_attribute_base_1.dump_me()

def test_case_5():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_ds()

def test_case_6():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()
    var_1 = field_attribute_base_0.get_variable_manager()
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_2 = field_attribute_base_1.serialize()
    var_3 = field_attribute_base_1.validate()

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
    var_0 = field_attribute_base_0.serialize()

def test_case_11():
    str_0 = None
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.from_attrs(dict_0)
    base_0 = module_0.Base()
    field_attribute_base_1 = module_0.FieldAttributeBase()

def test_case_12():
    var_0 = dict()
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_1 = field_attribute_base_0.deserialize(var_0)

def test_case_13():
    int_0 = -360
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.squash()
    set_0 = {int_0, int_0, int_0, int_0}
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_1 = field_attribute_base_1.validate(set_0)
    field_attribute_base_2 = module_0.FieldAttributeBase()
    var_2 = field_attribute_base_1.validate()
    var_3 = field_attribute_base_1.dump_attrs()