# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.aix as module_0

def test_case_0():
    try:
        str_0 = '\x0bd7EGW/,\t"Gxyr<iQ'
        a_i_x_network_0 = module_0.AIXNetwork(str_0)
        str_1 = '(IGL%?!t3+r'
        var_0 = a_i_x_network_0.get_default_interfaces(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"6P\xf6'\xf0\x1bI\xd2\xb0\xba\x18\xc8\xa5\xa6\xffQ89\xde\xb9"
        float_0 = 56.37
        a_i_x_network_0 = module_0.AIXNetwork(float_0)
        a_i_x_network_1 = module_0.AIXNetwork(a_i_x_network_0)
        tuple_0 = (a_i_x_network_1,)
        dict_0 = {bytes_0: bytes_0}
        float_1 = 1139.30894
        a_i_x_network_2 = module_0.AIXNetwork(dict_0, float_1)
        var_0 = a_i_x_network_2.get_interfaces_info(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        a_i_x_network_collector_0 = None
        a_i_x_network_0 = module_0.AIXNetwork(a_i_x_network_collector_0)
        str_0 = None
        float_0 = 1568.062
        a_i_x_network_collector_1 = module_0.AIXNetworkCollector(float_0)
        dict_0 = {str_0: str_0, a_i_x_network_0: a_i_x_network_collector_0, a_i_x_network_collector_0: a_i_x_network_collector_1}
        var_0 = a_i_x_network_0.parse_interface_line(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = None
        a_i_x_network_collector_0 = None
        str_0 = 'mJ\rc6HY'
        set_0 = set()
        float_0 = -1234.1
        a_i_x_network_0 = module_0.AIXNetwork(set_0, float_0)
        var_0 = a_i_x_network_0.parse_interface_line(str_0)
        set_1 = set()
        a_i_x_network_collector_1 = module_0.AIXNetworkCollector(set_1)
        a_i_x_network_1 = module_0.AIXNetwork(tuple_0, a_i_x_network_collector_1)
        var_1 = a_i_x_network_1.get_default_interfaces(a_i_x_network_collector_0)
    except BaseException:
        pass