# Automatically generated by Pynguin.
import ansible.playbook.attribute as module_0

def test_case_0():
    attribute_0 = module_0.Attribute()

def test_case_1():
    bytes_0 = b'\xd0\x12\xd3\r6\xb7'
    bytes_1 = b'\x18\x10'
    set_0 = None
    str_0 = 'Used ps output to match service name and determine it is up, this is very unreliable'
    attribute_0 = module_0.Attribute(bytes_0, bytes_1, set_0, str_0)
    str_1 = "%i'"
    int_0 = 1570
    attribute_1 = module_0.Attribute(str_1, int_0)
    var_0 = attribute_1.__lt__(attribute_0)

def test_case_2():
    float_0 = 1447.75
    str_0 = '"urJX|E\tmag,I?-?'
    attribute_0 = module_0.Attribute(float_0, str_0, str_0)