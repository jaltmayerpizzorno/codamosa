# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.sunos as module_0

def test_case_0():
    try:
        float_0 = -218.733
        sun_o_s_network_0 = module_0.SunOSNetwork(float_0)
        list_0 = [sun_o_s_network_0, sun_o_s_network_0]
        bool_0 = True
        bool_1 = None
        float_1 = 1265.59
        set_0 = {float_1}
        list_1 = [bool_1, set_0, bool_1, set_0]
        tuple_0 = (bool_0, bool_1, float_1, list_1)
        str_0 = 'u|"5p\x0c'
        sun_o_s_network_1 = module_0.SunOSNetwork(tuple_0, str_0)
        var_0 = sun_o_s_network_1.get_interfaces_info(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'runlevel'
        bool_0 = None
        dict_0 = {str_0: bool_0, bool_0: bool_0}
        sun_o_s_network_collector_0 = module_0.SunOSNetworkCollector(dict_0)
        bytes_0 = b'\x01\xd9\xdb\xb6\x8aM/\xe67\xd8\x915'
        sun_o_s_network_0 = module_0.SunOSNetwork(bytes_0)
        var_0 = sun_o_s_network_0.parse_ether_line(str_0, sun_o_s_network_collector_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        sun_o_s_network_collector_0 = module_0.SunOSNetworkCollector()
        sun_o_s_network_collector_1 = module_0.SunOSNetworkCollector(sun_o_s_network_collector_0)
        tuple_0 = None
        bool_0 = True
        int_0 = 3186
        sun_o_s_network_0 = module_0.SunOSNetwork(int_0)
        str_0 = 'path_filter'
        dict_0 = None
        sun_o_s_network_1 = module_0.SunOSNetwork(tuple_0)
        tuple_1 = (sun_o_s_network_0, str_0, dict_0, int_0)
        int_1 = 1715
        sun_o_s_network_2 = module_0.SunOSNetwork(dict_0)
        tuple_2 = (tuple_1, int_1)
        sun_o_s_network_3 = module_0.SunOSNetwork(bool_0, tuple_2)
        str_1 = 'b+g{+ NHI"u+P#gf'
        float_0 = 584.7782
        str_2 = 'Bu<ZO$'
        var_0 = sun_o_s_network_0.parse_interface_line(str_1, float_0, str_2)
    except BaseException:
        pass