# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hpux as module_0

def test_case_0():
    try:
        int_0 = 498
        h_p_u_x_network_0 = module_0.HPUXNetwork(int_0)
        var_0 = h_p_u_x_network_0.populate(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        h_p_u_x_network_0 = module_0.HPUXNetwork(list_0)
        var_0 = h_p_u_x_network_0.get_default_interfaces()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 498
        h_p_u_x_network_0 = module_0.HPUXNetwork(int_0)
        var_0 = h_p_u_x_network_0.get_interfaces_info()
    except BaseException:
        pass