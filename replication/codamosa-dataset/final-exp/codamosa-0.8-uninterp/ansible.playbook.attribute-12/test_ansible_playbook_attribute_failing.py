# Automatically generated by Pynguin.
import ansible.playbook.attribute as module_0

def test_case_0():
    try:
        int_0 = 411
        tuple_0 = ()
        attribute_0 = module_0.Attribute(tuple_0)
        var_0 = attribute_0.__eq__(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Not a valid network hostname: %s'
        bytes_0 = b'\x91'
        tuple_0 = (str_0, bytes_0)
        str_1 = 'Low Profile Desktop'
        attribute_0 = module_0.Attribute(tuple_0, tuple_0, str_1)
        int_0 = 466
        var_0 = attribute_0.__ne__(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '?-7lcw'
        bytes_0 = b'_T\x88O\\G\x96e'
        int_0 = 2540
        tuple_0 = (str_0, bytes_0, int_0, int_0)
        field_attribute_0 = module_0.FieldAttribute(tuple_0)
        bool_0 = True
        str_1 = '}%b#gF\x0cJkL\t"*!-a~;j'
        list_0 = [bool_0, int_0, int_0, bytes_0]
        str_2 = 'zl'
        set_0 = {str_1, int_0, str_2}
        attribute_0 = module_0.Attribute(bytes_0, tuple_0, list_0, set_0, set_0, bool_0)
        bytes_1 = b'\x13.7 \xce\xc4\xcd\xdf\x9cc\xc9\x90\x8f'
        var_0 = attribute_0.__lt__(bytes_1)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -1121.5685
        set_0 = set()
        attribute_0 = module_0.Attribute(float_0, set_0)
        var_0 = attribute_0.__gt__(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1846
        set_0 = set()
        attribute_0 = module_0.Attribute(set_0, set_0)
        var_0 = attribute_0.__le__(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '4.'
        bytes_0 = b'\xde\xaf\x9aZ\xd8s\xdcz\xe9\xbe'
        str_1 = 'VB2\x0b#~mtQNfa'
        bool_0 = True
        attribute_0 = module_0.Attribute(bytes_0, str_1, bool_0)
        var_0 = attribute_0.__ge__(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        bool_0 = True
        str_0 = '@S|R\x0b9cgUk=_N'
        field_attribute_0 = module_0.FieldAttribute(dict_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'list'
        bool_0 = True
        attribute_0 = module_0.Attribute(str_0, bool_0, bool_0, bool_0)
    except BaseException:
        pass