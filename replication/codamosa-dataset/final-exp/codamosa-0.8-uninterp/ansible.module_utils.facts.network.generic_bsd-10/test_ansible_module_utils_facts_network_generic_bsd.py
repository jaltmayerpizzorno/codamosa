# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 480
    float_0 = 385.43
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0, float_0)
    str_0 = 'Hasło'
    bytes_0 = b'\x01\x84\x04\xa5\x99\xc8'
    var_0 = generic_bsd_ifconfig_network_0.parse_unknown_line(str_0, str_0, bytes_0)
    dict_0 = {float_0: str_0, var_0: str_0}
    var_1 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
    var_2 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, str_0, str_0)

def test_case_2():
    str_0 = '?9)_4]E#\nW1\t$o^*SC4'
    str_1 = 'v'
    float_0 = -2166.715
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1, float_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)

def test_case_3():
    str_0 = 'fA#06\nKCyS8]'
    list_0 = [str_0]
    bytes_0 = b'\x04\x05\x8b\xaa\x84\x030\x101\xd2\xe9\x0c\x87\xc0!\xb4\xd0\xfa\x86\x1b'
    dict_0 = {str_0: str_0, str_0: bytes_0, bytes_0: bytes_0}
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0, str_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_media_line(str_0, dict_0, list_0)
    int_0 = 480
    var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(dict_0, int_0, str_0)