# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = {}
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0)
    str_0 = 'eth0'
    str_1 = 'media'
    str_2 = 'Ethernet autoselect'
    str_3 = {str_1: str_2}
    str_4 = {str_0: str_3}
    var_1 = generic_bsd_ifconfig_network_0.detect_type_media(str_4)

def test_case_2():
    str_0 = ')'
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
    str_1 = '%9C9+[1@~~'
    var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_1)

def test_case_3():
    bool_0 = False
    float_0 = 0.0
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: float_0, float_0: float_0}
    float_1 = -4325.222047
    int_0 = -1502
    dict_1 = {}
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_1)
    var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(dict_0, float_1, int_0)

def test_case_4():
    str_0 = '~#TEa7\x0b'
    int_0 = -2657
    str_1 = '6Ar&x2'
    float_0 = -2057.093889219267
    tuple_0 = ()
    set_0 = {int_0, tuple_0, int_0}
    dict_0 = {tuple_0: set_0, float_0: int_0, tuple_0: int_0}
    dict_1 = {float_0: str_1, float_0: int_0, float_0: str_0}
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_1)
    var_0 = generic_bsd_ifconfig_network_0.parse_media_line(str_1, dict_0, tuple_0)