# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.aix as module_0

def test_case_0():
    try:
        list_0 = None
        bool_0 = False
        a_i_x_network_0 = module_0.AIXNetwork(bool_0)
        var_0 = a_i_x_network_0.get_default_interfaces(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = None
        float_0 = -1399.2
        set_0 = {bool_0, bool_0, float_0}
        set_1 = set()
        a_i_x_network_0 = module_0.AIXNetwork(set_1)
        var_0 = a_i_x_network_0.get_interfaces_info(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        a_i_x_network_collector_0 = None
        a_i_x_network_collector_1 = module_0.AIXNetworkCollector()
        a_i_x_network_0 = module_0.AIXNetwork(a_i_x_network_collector_1)
        a_i_x_network_1 = module_0.AIXNetwork(a_i_x_network_0)
        var_0 = a_i_x_network_1.parse_interface_line(a_i_x_network_collector_0)
    except BaseException:
        pass