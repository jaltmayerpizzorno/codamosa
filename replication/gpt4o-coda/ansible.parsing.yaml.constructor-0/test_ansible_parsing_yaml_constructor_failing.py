# Automatically generated by Pynguin.
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1

def test_case_0():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_mapping(ansible_constructor_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        int_0 = 755
        tuple_0 = (set_0, int_0, set_0)
        bytes_0 = b'fXvY\xd4\xd7q]'
        ansible_constructor_0 = module_0.AnsibleConstructor(bytes_0)
        var_0 = ansible_constructor_0.construct_yaml_seq(tuple_0)
        ansible_constructor_1 = module_0.AnsibleConstructor()
        int_1 = -824
        var_1 = ansible_constructor_1.construct_yaml_str(int_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "o'MJ3"
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_vault_encrypted_unicode(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_unsafe(ansible_constructor_0)
    except BaseException:
        pass

def test_case_4():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        str_0 = '/u%je!*if].a.V9c9z7'
        list_0 = [str_0]
        str_1 = 'I=4iIqnppP2MZ'
        ansible_constructor_1 = module_0.AnsibleConstructor(list_0, str_1)
        var_0 = ansible_constructor_1.construct_mapping(ansible_constructor_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '1-r}>!<g=U'
        ansible_constructor_0 = module_0.AnsibleConstructor()
        str_1 = "RWoFF?.k<_@Ha'c"
        ansible_constructor_1 = None
        list_0 = [str_0, str_1, ansible_constructor_1]
        bytes_0 = b'\xfc'
        mapping_node_0 = module_1.MappingNode(str_1, list_0, bytes_0)
        var_0 = ansible_constructor_0.construct_mapping(mapping_node_0, mapping_node_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '1o_-r}>d!<g=U'
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_seq(str_0)
        set_0 = set()
        mapping_node_0 = module_1.MappingNode(ansible_constructor_0, set_0)
        var_1 = ansible_constructor_0.construct_yaml_unsafe(mapping_node_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '1o_-r}>d!<g=U'
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_seq(str_0)
        var_1 = ansible_constructor_0.construct_yaml_seq(str_0)
        bool_0 = True
        var_2 = ansible_constructor_0.construct_yaml_seq(bool_0)
        int_0 = None
        list_0 = [var_2, str_0]
        float_0 = 87.4
        mapping_node_0 = module_1.MappingNode(int_0, list_0, list_0, float_0)
        var_3 = ansible_constructor_0.construct_yaml_unsafe(mapping_node_0)
    except BaseException:
        pass