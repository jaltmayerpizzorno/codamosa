# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.aix as module_0

def test_case_0():
    try:
        bool_0 = True
        float_0 = 3474.6
        a_i_x_network_0 = module_0.AIXNetwork(float_0)
        var_0 = a_i_x_network_0.get_default_interfaces(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'N5RIheKA'
        str_1 = '%s has a documentation formatting error'
        a_i_x_network_0 = module_0.AIXNetwork(str_1)
        var_0 = a_i_x_network_0.get_interfaces_info(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        a_i_x_network_0 = None
        float_0 = 512.0
        a_i_x_network_1 = module_0.AIXNetwork(float_0)
        var_0 = a_i_x_network_1.parse_interface_line(a_i_x_network_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ',wS"Q<<'
        int_0 = 1576
        a_i_x_network_0 = module_0.AIXNetwork(int_0)
        var_0 = a_i_x_network_0.parse_interface_line(str_0)
        str_1 = '4e-'
        var_1 = a_i_x_network_0.parse_interface_line(str_1)
        a_i_x_network_collector_0 = module_0.AIXNetworkCollector()
        a_i_x_network_1 = module_0.AIXNetwork(a_i_x_network_collector_0)
        list_0 = []
        var_2 = a_i_x_network_1.get_interfaces_info(int_0, list_0)
    except BaseException:
        pass