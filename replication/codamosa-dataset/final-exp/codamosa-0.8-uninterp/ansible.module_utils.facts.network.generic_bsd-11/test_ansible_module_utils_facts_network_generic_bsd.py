# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -743
    bool_0 = True
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
    list_0 = []
    tuple_0 = (list_0,)
    str_0 = 'auth_url'
    dict_0 = {str_0: str_0, int_0: tuple_0}
    var_0 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
    var_1 = generic_bsd_ifconfig_network_0.parse_unknown_line(tuple_0, tuple_0, int_0)

def test_case_2():
    str_0 = 'dftH56TH}b;| ;&af'
    bool_0 = False
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
    var_0 = generic_bsd_ifconfig_network_1.parse_interface_line(str_0)

def test_case_3():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    str_0 = ' :J`E}dFGb'
    float_0 = -91.6
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
    var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(dict_0, str_0, str_0)

def test_case_4():
    str_0 = '5]$l'
    bool_0 = False
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)
    str_1 = '>+<Z[ehA]~d:3\x0bwPb&'
    var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(str_1, str_1, generic_bsd_ifconfig_network_0)
    var_2 = generic_bsd_ifconfig_network_0.get_options(str_1)

def test_case_5():
    tuple_0 = ()
    str_0 = "a!'G|P+t9G\tf\n785 gB"
    dict_0 = {tuple_0: tuple_0}
    bool_0 = True
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0, bool_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_media_line(str_0, dict_0, dict_0)
    str_1 = '5<uG?a6%zZ'
    bool_1 = True
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(bool_1)
    var_1 = generic_bsd_ifconfig_network_1.parse_interface_line(str_1)
    bytes_0 = None
    generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bytes_0)
    list_0 = [tuple_0, generic_bsd_ifconfig_network_2]
    str_2 = 'Z0-eY#'
    str_3 = 'T'
    var_2 = generic_bsd_ifconfig_network_2.merge_default_interface(str_2, str_3, generic_bsd_ifconfig_network_2)
    generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(list_0)
    generic_bsd_ifconfig_network_4 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_2, generic_bsd_ifconfig_network_3)

def test_case_6():
    var_0 = None
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0)
    str_0 = '<UP,LOOPBACK>'
    var_1 = generic_bsd_ifconfig_network_0.get_options(str_0)
    str_1 = '<LOOPBACK>'
    var_2 = generic_bsd_ifconfig_network_0.get_options(str_1)
    str_2 = '<>'
    var_3 = generic_bsd_ifconfig_network_0.get_options(str_2)
    str_3 = '<RUNNING>'
    var_4 = generic_bsd_ifconfig_network_0.get_options(str_3)
    str_4 = '<HELLO,GOODBYE>'
    var_5 = generic_bsd_ifconfig_network_0.get_options(str_4)
    str_5 = 'HELLO,GOODBYE>'
    var_6 = generic_bsd_ifconfig_network_0.get_options(str_5)
    str_6 = '<HELLO,GOODBYE'
    var_7 = generic_bsd_ifconfig_network_0.get_options(str_6)

def test_case_7():
    var_0 = None
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0)
    str_0 = 'interface'
    str_1 = 'address'
    str_2 = 'lo0'
    str_3 = {str_0: str_2, str_1: str_1}
    str_4 = 'ipv4'
    str_5 = 'ipv6'
    str_6 = {str_1: str_2}
    str_7 = [str_6]
    str_8 = [str_3]
    str_9 = {str_4: str_7, str_5: str_8}
    str_10 = {str_2: str_9}
    var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(str_3, str_10, str_4)

def test_case_8():
    var_0 = None
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0)
    str_0 = 'interface'
    str_1 = 'address'
    str_2 = 'lo0'
    str_3 = '0.0.0.0'
    str_4 = {str_0: str_2, str_1: str_3}
    str_5 = 'ipv4'
    str_6 = 'ipv6'
    str_7 = {str_1: str_3}
    str_8 = [str_7]
    str_9 = '::1'
    str_10 = {str_1: str_9}
    str_11 = [str_10]
    str_12 = {str_5: str_8, str_6: str_11}
    str_13 = {str_2: str_12}
    var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(str_4, str_13, str_5)
    var_2 = generic_bsd_ifconfig_network_0.merge_default_interface(str_4, str_13, str_6)

def test_case_9():
    var_0 = None
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0)
    str_0 = 'interface'
    str_1 = 'address'
    str_2 = '0.0.0.0'
    str_3 = {str_0: str_0, str_1: str_2}
    str_4 = 'ipv6'
    str_5 = [str_3]
    str_6 = '::1'
    str_7 = {str_1: str_6}
    str_8 = [str_7]
    str_9 = {str_4: str_5, str_4: str_8}
    str_10 = {str_4: str_9}
    var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(str_3, str_10, str_10)
    var_2 = generic_bsd_ifconfig_network_0.merge_default_interface(str_3, str_10, str_4)