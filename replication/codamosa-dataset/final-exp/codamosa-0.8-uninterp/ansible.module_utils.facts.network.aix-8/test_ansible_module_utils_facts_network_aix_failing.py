# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.aix as module_0

def test_case_0():
    try:
        int_0 = 401
        float_0 = 1068.98
        a_i_x_network_0 = module_0.AIXNetwork(float_0)
        var_0 = a_i_x_network_0.get_default_interfaces(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        a_i_x_network_collector_0 = module_0.AIXNetworkCollector()
        a_i_x_network_collector_1 = module_0.AIXNetworkCollector(a_i_x_network_collector_0)
        float_0 = -2786.45612
        float_1 = 0.001
        a_i_x_network_0 = module_0.AIXNetwork(float_1)
        var_0 = a_i_x_network_0.get_interfaces_info(float_0)
    except BaseException:
        pass