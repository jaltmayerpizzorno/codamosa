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
        str_0 = '5E(j>Yx^.TF}V9;'
        bytes_0 = b'\xcd$\x9cs\x96]\x1b\xee\x91\xa8\xd8\x93\x1f.\xa2\x01'
        int_0 = 727
        list_0 = []
        bytes_1 = b'\xa3\xd8\xd3\xb5'
        float_0 = 100.0
        bool_0 = False
        tuple_0 = (list_0, bytes_1, float_0, bool_0)
        set_0 = set()
        attribute_0 = module_0.Attribute(bytes_0, int_0, tuple_0, float_0, bytes_0, set_0)
        var_0 = attribute_0.__ne__(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'p8U,iaxjNe\nY'
        set_0 = {str_0, str_0, str_0, str_0}
        bytes_0 = b'\x03\xf2\xb2\x0e\xda4\xdfK\xfe\x1a'
        attribute_0 = module_0.Attribute(str_0, str_0, str_0, set_0, bytes_0)
        var_0 = attribute_0.__lt__(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        int_0 = -631
        float_0 = 0.0001
        list_0 = [float_0]
        field_attribute_0 = module_0.FieldAttribute(bool_0, int_0, float_0, list_0)
        bytes_0 = b"S\xaa\x99'B\x0f)Q\xe3\x8a\xc8"
        tuple_0 = (bytes_0,)
        attribute_0 = module_0.Attribute(bool_0)
        var_0 = attribute_0.__le__(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'dieSct'
        bool_0 = False
        attribute_0 = module_0.Attribute(str_0, bool_0, bool_0)
        bool_1 = False
        var_0 = attribute_0.__ge__(bool_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'dict'
        bool_0 = True
        list_0 = [str_0, str_0]
        attribute_0 = module_0.Attribute(list_0)
        bool_1 = False
        attribute_1 = module_0.Attribute(str_0, bool_0, bool_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dict'
        bool_0 = False
        attribute_0 = module_0.Attribute()
        int_0 = -368
        attribute_1 = module_0.Attribute(int_0, str_0)
        var_0 = attribute_1.__gt__(attribute_0)
        attribute_2 = module_0.Attribute(str_0, bool_0, bool_0)
    except BaseException:
        pass