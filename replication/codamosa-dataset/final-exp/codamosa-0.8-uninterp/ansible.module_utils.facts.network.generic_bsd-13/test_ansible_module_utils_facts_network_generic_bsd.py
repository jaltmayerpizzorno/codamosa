# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0
import ansible.module_utils.facts.network.base as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '"gH4_+}[Qy?a\tBY'
    int_0 = -2567
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)

def test_case_2():
    int_0 = 250000
    str_0 = 'km/viU<C=^`n$}'
    tuple_0 = (int_0, str_0)
    dict_0 = {tuple_0: int_0, str_0: str_0}
    list_0 = [int_0, str_0]
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0, tuple_0)
    int_1 = -151
    network_0 = module_1.Network(int_1)
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(network_0)
    var_0 = generic_bsd_ifconfig_network_1.parse_media_line(tuple_0, dict_0, generic_bsd_ifconfig_network_0)

def test_case_3():
    set_0 = set()
    str_0 = ')Uo8Jx'
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
    var_0 = generic_bsd_ifconfig_network_1.detect_type_media(set_0)

def test_case_4():
    var_0 = {}
    var_1 = {}
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0, var_1)
    str_0 = 'options=3<RXCSUM,TXCSUM,VLAN_MTU>'
    var_2 = generic_bsd_ifconfig_network_0.get_options(str_0)
    str_1 = 'options=3'
    var_3 = generic_bsd_ifconfig_network_0.get_options(str_1)
    str_2 = 'options=3<>'
    var_4 = generic_bsd_ifconfig_network_0.get_options(str_2)
    str_3 = 'options=<>'
    var_5 = generic_bsd_ifconfig_network_0.get_options(str_3)