# Automatically generated by Pynguin.
import ansible.parsing.yaml.constructor as module_0
import ansible.parsing.vault as module_1
import yaml.nodes as module_2
import ansible.parsing.yaml.objects as module_3

def test_case_0():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_mapping(ansible_constructor_0)
    except BaseException:
        pass

def test_case_1():
    try:
        ansible_constructor_0 = module_0.AnsibleConstructor()
        int_0 = 1393
        ansible_constructor_1 = module_0.AnsibleConstructor(int_0)
        var_0 = ansible_constructor_1.construct_yaml_str(ansible_constructor_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'bootstrap_wrapper.ps1'
        ansible_constructor_0 = module_0.AnsibleConstructor(str_0)
        ansible_constructor_1 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_1.construct_vault_encrypted_unicode(ansible_constructor_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 99
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_unsafe(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = set()
        str_0 = 'xa'
        vault_lib_0 = module_1.VaultLib(set_0)
        ansible_constructor_0 = module_0.AnsibleConstructor(str_0, vault_lib_0)
        int_0 = 32
        var_0 = ansible_constructor_0.construct_mapping(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x1f\xc2)@\xe7\x16\x8f\xcb\xc3R%'
        str_0 = 'Ggs7ZD_W%I-'
        ansible_constructor_0 = module_0.AnsibleConstructor()
        int_0 = -312
        tuple_0 = ()
        list_0 = [bytes_0, str_0, tuple_0, str_0]
        mapping_node_0 = module_2.MappingNode(list_0, int_0, int_0)
        var_0 = ansible_constructor_0.construct_yaml_unsafe(mapping_node_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'GSs7ZD_W%I}'
        str_1 = 'QH+`Qu4'
        str_2 = 'OF2q]'
        str_3 = 'RrtGtPOuq\t9Q(J@,(R6'
        dict_0 = {str_1: str_1, str_2: str_0, str_3: str_3}
        ansible_mapping_0 = module_3.AnsibleMapping(**dict_0)
        dict_1 = {}
        mapping_node_0 = module_2.MappingNode(dict_1, dict_1)
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_unsafe(mapping_node_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 699
        ansible_constructor_0 = module_0.AnsibleConstructor()
        var_0 = ansible_constructor_0.construct_yaml_seq(int_0)
        list_0 = None
        ansible_constructor_1 = module_0.AnsibleConstructor(list_0)
        list_1 = [var_0]
        str_0 = '{(.*)}'
        dict_0 = {str_0: ansible_constructor_1}
        ansible_sequence_0 = module_3.AnsibleSequence(*list_1, **dict_0)
    except BaseException:
        pass