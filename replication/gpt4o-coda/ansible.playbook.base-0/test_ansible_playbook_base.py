# Automatically generated by Pynguin.
import ansible.playbook.base as module_0

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
    set_0 = set()
    var_0 = field_attribute_base_0.load_data(set_0)

def test_case_5():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_ds()

def test_case_6():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_loader()

def test_case_7():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.get_ds()
    var_1 = field_attribute_base_0.dump_attrs()
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_2 = field_attribute_base_0.get_variable_manager()
    var_3 = field_attribute_base_0.copy()
    var_4 = field_attribute_base_1.validate()

def test_case_8():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.validate()

def test_case_9():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.squash()

def test_case_10():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.copy()

def test_case_11():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()

def test_case_12():
    dict_0 = {}
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.deserialize(dict_0)
    base_0 = module_0.Base()
    var_1 = base_0.get_dep_chain()
    field_attribute_base_1 = module_0.FieldAttributeBase()

def test_case_13():
    base_0 = module_0.Base()
    var_0 = base_0.get_path()

def test_case_14():
    base_0 = module_0.Base()
    var_0 = base_0.get_dep_chain()

def test_case_15():
    base_0 = module_0.Base()
    var_0 = base_0.get_search_path()

def test_case_16():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.squash()
    var_1 = field_attribute_base_0.dump_me()
    var_2 = field_attribute_base_0.validate()
    list_0 = []
    var_3 = field_attribute_base_0.load_data(list_0)

def test_case_17():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()
    str_0 = '.aE.l%[mjB!c'
    dict_0 = {str_0: var_0}
    var_1 = field_attribute_base_0.deserialize(dict_0)
    field_attribute_base_1 = module_0.FieldAttributeBase()
    var_2 = field_attribute_base_1.serialize()
    var_3 = field_attribute_base_1.get_variable_manager()
    var_4 = field_attribute_base_1.validate(dict_0)
    field_attribute_base_2 = module_0.FieldAttributeBase()
    field_attribute_base_3 = module_0.FieldAttributeBase()

def test_case_18():
    str_0 = '?*b4}~)=66H=z(M='
    str_1 = 'X\'zDvHv\x0cQy\tqZZ0O"S!'
    dict_0 = {str_0: str_0, str_1: str_1}
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.from_attrs(dict_0)

def test_case_19():
    field_attribute_base_0 = module_0.FieldAttributeBase()
    var_0 = field_attribute_base_0.serialize()
    field_attribute_base_1 = module_0.FieldAttributeBase()
    dict_0 = {}
    str_0 = 'ok: [%s]'
    var_1 = field_attribute_base_1.load_data(dict_0, str_0)
    var_2 = field_attribute_base_1.dump_me()
    var_3 = field_attribute_base_1.validate()
    var_4 = field_attribute_base_1.copy()
    var_5 = field_attribute_base_1.get_variable_manager()
    list_0 = [field_attribute_base_1, str_0]
    str_1 = 'v;Gl#w6;$\x0cB=Q-*H'
    dict_1 = {str_0: list_0, str_1: str_0}
    var_6 = field_attribute_base_0.squash()
    var_7 = field_attribute_base_1.deserialize(dict_1)