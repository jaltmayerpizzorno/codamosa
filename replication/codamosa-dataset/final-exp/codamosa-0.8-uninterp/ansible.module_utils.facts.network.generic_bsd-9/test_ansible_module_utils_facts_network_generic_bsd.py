# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xb2\xbc\xd8\xdd\x1f\xa7\xe9'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    str_0 = ''
    float_0 = 1297.9661
    int_0 = 2219
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0, int_0)
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
    var_0 = generic_bsd_ifconfig_network_1.parse_ether_line(bytes_0, dict_0, str_0)

def test_case_2():
    str_0 = 'changes'
    bool_0 = False
    bytes_0 = b''
    str_1 = '7F1>:ke8S'
    str_2 = 'Qb<&jgSSX,wT@'
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1, str_2)
    var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, bool_0, bytes_0)

def test_case_3():
    dict_0 = {}
    float_0 = 1910.91205
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
    var_0 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)

def test_case_4():
    str_0 = 'g\tv{'
    str_1 = 'Ce$%'
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1)
    var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)

def test_case_5():
    str_0 = '/bin'
    var_0 = dict(bin_dir=str_0)
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0)
    str_1 = '<LOOPBACK,UP,LOWER_UP>'
    var_1 = generic_bsd_ifconfig_network_0.get_options(str_1)