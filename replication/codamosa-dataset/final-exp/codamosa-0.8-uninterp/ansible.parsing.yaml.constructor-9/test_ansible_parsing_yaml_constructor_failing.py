# Automatically generated by Pynguin.
import ansible.parsing.yaml.constructor as module_0
import yaml.nodes as module_1
import ansible.parsing.yaml.objects as module_2

def test_case_0():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_mapping(ansible_constructor_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '8m'
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_str(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_vault_encrypted_unicode(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        vault_lib_0 = None
        var_0 = ansible_constructor_0.construct_yaml_unsafe(vault_lib_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1805
        str_0 = 'uujk-|F\\8'
        set_0 = {str_0, str_0}
        ansible_constructor_0 = module_0.AnsibleConstructor(str_0, set_0)
        var_0 = ansible_constructor_0.construct_yaml_unsafe(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        str_0 = 'tag:yaml.org,2002:map'
        var_0 = []
        mapping_node_0 = module_1.MappingNode(str_0, var_0)
        var_1 = ansible_constructor_0.construct_mapping(mapping_node_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = None
        str_0 = ':myTm&'
        ansible_constructor_0 = module_0.AnsibleConstructor(str_0)
        var_0 = ansible_constructor_0.construct_yaml_seq(bytes_0)
        tuple_0 = ()
        bool_0 = False
        mapping_node_0 = module_1.MappingNode(bool_0, tuple_0, bool_0)
        list_0 = [var_0]
        ansible_mapping_0 = module_2.AnsibleMapping(*list_0)
    except BaseException:
        pass