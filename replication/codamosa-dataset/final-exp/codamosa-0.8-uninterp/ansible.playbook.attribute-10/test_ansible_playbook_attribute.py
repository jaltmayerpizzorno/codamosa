# Automatically generated by Pynguin.
import ansible.playbook.attribute as module_0

def test_case_0():
    attribute_0 = None
    int_0 = 55
    field_attribute_0 = module_0.FieldAttribute(attribute_0, int_0)

def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0]
    bool_0 = False
    str_0 = 'v8'
    int_0 = -1954
    field_attribute_0 = module_0.FieldAttribute(str_0, int_0, list_0, bool_0, int_0)

def test_case_2():
    set_0 = set()
    list_0 = [set_0, set_0]
    tuple_0 = ()
    bool_0 = False
    float_0 = -940.54507
    str_0 = 'v8'
    int_0 = -1954
    field_attribute_0 = module_0.FieldAttribute(str_0, int_0, list_0, bool_0, int_0)
    dict_0 = {tuple_0: list_0, str_0: float_0}
    str_1 = '5/*'
    attribute_0 = module_0.Attribute(tuple_0, dict_0, str_1)
    var_0 = attribute_0.__ne__(field_attribute_0)
    attribute_1 = module_0.Attribute(bool_0, float_0, set_0, set_0, field_attribute_0)