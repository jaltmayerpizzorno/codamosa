# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'prefixlen'
    bool_0 = False
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)

def test_case_2():
    str_0 = 'h.#W[Nf+)X<'
    int_0 = True
    int_1 = 1340
    tuple_0 = ()
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0)
    var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, int_0, int_1)