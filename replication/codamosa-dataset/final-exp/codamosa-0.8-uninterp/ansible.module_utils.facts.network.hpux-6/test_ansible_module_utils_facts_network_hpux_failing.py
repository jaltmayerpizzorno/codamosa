# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hpux as module_0

def test_case_0():
    try:
        bool_0 = False
        str_0 = 'C&sl=SU=^cCr>hOY6]w'
        set_0 = {bool_0, str_0}
        bytes_0 = b'\x92\xe4Z\x94*_\xdf\xe1'
        h_p_u_x_network_0 = module_0.HPUXNetwork(set_0, bytes_0)
        var_0 = h_p_u_x_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -2531.0957
        h_p_u_x_network_collector_0 = module_0.HPUXNetworkCollector(float_0)
        h_p_u_x_network_collector_1 = module_0.HPUXNetworkCollector()
        h_p_u_x_network_0 = module_0.HPUXNetwork(float_0)
        var_0 = h_p_u_x_network_0.get_default_interfaces()
    except BaseException:
        pass

def test_case_2():
    try:
        h_p_u_x_network_collector_0 = module_0.HPUXNetworkCollector()
        set_0 = set()
        float_0 = 534.914829
        int_0 = -6908
        tuple_0 = (set_0, float_0, int_0, int_0)
        bool_0 = True
        h_p_u_x_network_0 = module_0.HPUXNetwork(bool_0)
        list_0 = [h_p_u_x_network_collector_0, tuple_0, h_p_u_x_network_0, set_0]
        h_p_u_x_network_1 = module_0.HPUXNetwork(list_0)
        var_0 = h_p_u_x_network_1.get_interfaces_info()
    except BaseException:
        pass