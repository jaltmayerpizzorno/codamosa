# Automatically generated by Pynguin.
import ansible.playbook.attribute as module_0

def test_case_0():
    float_0 = -443.24
    int_0 = -1082
    list_0 = [int_0]
    set_0 = set()
    bool_0 = False
    str_0 = '"\' }P'
    tuple_0 = (set_0, float_0, str_0)
    float_1 = -2836.11911
    bool_1 = True
    str_1 = 'UFkOI\rs'
    field_attribute_0 = module_0.FieldAttribute(str_1, bool_0, list_0)
    attribute_0 = module_0.Attribute(bool_1, field_attribute_0, set_0)
    tuple_1 = (tuple_0, float_1, str_1, attribute_0)
    attribute_1 = module_0.Attribute(tuple_0, tuple_1)
    var_0 = attribute_1.__eq__(attribute_0)

def test_case_1():
    str_0 = 'li'
    bool_0 = False
    bool_1 = False
    attribute_0 = module_0.Attribute(str_0, bool_1, bool_1, str_0, bool_0)