# Automatically generated by Pynguin.
import ansible.playbook.attribute as module_0

def test_case_0():
    try:
        bytes_0 = b'\xcc5#\x0b\x88")F>\x8e\xfd\xa5\xe9\xbe\xc3\x86d'
        bytes_1 = b'\xb3\xfb\x93\xe0h\xbd\x03\xaf%\xfb\x17'
        float_0 = None
        set_0 = {float_0, float_0, float_0, float_0}
        int_0 = 759
        bool_0 = True
        field_attribute_0 = module_0.FieldAttribute(bytes_1, int_0, bool_0, float_0, set_0)
        str_0 = '8Rp!:Q-l\\B9kz%}'
        attribute_0 = module_0.Attribute(bytes_1, set_0, field_attribute_0, str_0)
        var_0 = attribute_0.__eq__(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'str'
        bool_0 = True
        bool_1 = False
        str_1 = 'gs'
        var_0 = None
        attribute_0 = module_0.Attribute(str_0, bool_1, str_1, bool_1, var_0, bool_1, var_0, bool_1, bool_0, var_0, bool_1, bool_1, bool_1)
        str_2 = 'Timeout when waiting for %s:%s to drain'
        var_1 = attribute_0.__ne__(str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'smt'
        bool_0 = True
        str_1 = '=P{D'
        var_0 = None
        attribute_0 = module_0.Attribute(str_0, bool_0, str_1, bool_0, var_0, bool_0, var_0, bool_0, bool_0, var_0, bool_0, bool_0, bool_0)
        float_0 = -2611.0
        var_1 = attribute_0.__lt__(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'smt'
        bool_0 = True
        str_1 = 'eggs'
        attribute_0 = module_0.Attribute(str_0, bool_0, str_1, bool_0, str_0, bool_0, str_0, bool_0, bool_0, str_0, bool_0, bool_0, bool_0)
        bytes_0 = b'=\xfe\xe4]7\n'
        str_2 = ',D~$uf\x0c0'
        attribute_1 = module_0.Attribute(bytes_0, str_2, attribute_0)
        float_0 = 1000.0
        var_0 = attribute_1.__gt__(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        int_0 = -89
        tuple_0 = ()
        bytes_0 = b'E\xed\xfcl\xa1\xc2?\xa3\xc76K\x8c\xc5\xe1\x13O\x1f'
        attribute_0 = module_0.Attribute(int_0, tuple_0, bytes_0, tuple_0)
        var_0 = attribute_0.__ge__(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Hg3"eQ0[6_Q&'
        bool_0 = False
        int_0 = 1277
        str_1 = '/proc/xen/capabilities'
        attribute_0 = module_0.Attribute(int_0, str_1)
        bool_1 = True
        tuple_0 = (bool_1,)
        attribute_1 = module_0.Attribute(str_0, attribute_0, tuple_0, attribute_0)
        var_0 = attribute_1.__le__(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'set'
        bool_0 = False
        field_attribute_0 = module_0.FieldAttribute(str_0, bool_0, bool_0)
    except BaseException:
        pass