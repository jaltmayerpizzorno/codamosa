# Automatically generated by Pynguin.
import ansible.playbook.attribute as module_0

def test_case_0():
    try:
        str_0 = 'dict'
        attribute_0 = module_0.Attribute(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        str_0 = 'removed'
        bool_0 = None
        dict_0 = {str_0: bool_0}
        field_attribute_0 = module_0.FieldAttribute(str_0, dict_0, dict_0)
        str_1 = '{e&qV3\x0coa;'
        attribute_0 = module_0.Attribute(field_attribute_0, str_1)
        var_0 = attribute_0.__eq__(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        str_0 = 't\t%bS'
        int_0 = 846
        set_0 = set()
        str_1 = '2BdW.'
        attribute_0 = module_0.Attribute(str_0, int_0, set_0, str_1)
        var_0 = attribute_0.__ne__(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -1352.4
        str_0 = '34U2\'<-WSV="KsncH'
        dict_0 = {str_0: str_0}
        str_1 = 'u'
        float_1 = -997.5732
        float_2 = 0.0001
        attribute_0 = module_0.Attribute(str_0, dict_0, str_1, float_1, float_2)
        var_0 = attribute_0.__lt__(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'removed'
        bool_0 = None
        dict_0 = {str_0: bool_0}
        field_attribute_0 = module_0.FieldAttribute(str_0, dict_0, dict_0)
        str_1 = '{e&qV3\x0coa;'
        attribute_0 = module_0.Attribute(field_attribute_0, str_1)
        bytes_0 = b'\xcd\xd1\x12c'
        var_0 = attribute_0.__gt__(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        float_0 = 1.0
        float_1 = None
        tuple_0 = (float_0, float_1)
        list_0 = [float_0, float_1, tuple_0, float_0]
        attribute_0 = module_0.Attribute(tuple_0, list_0)
        var_0 = attribute_0.__le__(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = None
        str_0 = 'removed'
        bool_0 = None
        dict_0 = {str_0: bool_0}
        field_attribute_0 = module_0.FieldAttribute(str_0, dict_0, dict_0)
        str_1 = '{e&qV3\x0coa;'
        attribute_0 = module_0.Attribute(field_attribute_0, str_1)
        var_0 = attribute_0.__ge__(int_0)
    except BaseException:
        pass