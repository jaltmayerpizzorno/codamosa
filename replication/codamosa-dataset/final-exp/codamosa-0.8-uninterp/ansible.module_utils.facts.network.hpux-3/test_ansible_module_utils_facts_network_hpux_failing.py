# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hpux as module_0

def test_case_0():
    try:
        tuple_0 = ()
        h_p_u_x_network_0 = module_0.HPUXNetwork(tuple_0)
        var_0 = h_p_u_x_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -344.5708
        h_p_u_x_network_0 = module_0.HPUXNetwork(float_0)
        var_0 = h_p_u_x_network_0.get_default_interfaces()
    except BaseException:
        pass

def test_case_2():
    try:
        h_p_u_x_network_collector_0 = module_0.HPUXNetworkCollector()
        list_0 = [h_p_u_x_network_collector_0]
        h_p_u_x_network_0 = module_0.HPUXNetwork(list_0)
        h_p_u_x_network_1 = module_0.HPUXNetwork(h_p_u_x_network_collector_0)
        var_0 = h_p_u_x_network_1.get_interfaces_info()
    except BaseException:
        pass