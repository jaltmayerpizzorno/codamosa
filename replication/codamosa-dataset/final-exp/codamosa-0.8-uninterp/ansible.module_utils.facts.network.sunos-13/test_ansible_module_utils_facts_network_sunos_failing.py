# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.sunos as module_0

def test_case_0():
    try:
        float_0 = -1725.22
        list_0 = [float_0, float_0, float_0, float_0]
        str_0 = 'zq)\x0c\\'
        dict_0 = {str_0: str_0, str_0: str_0}
        sun_o_s_network_0 = module_0.SunOSNetwork(dict_0)
        var_0 = sun_o_s_network_0.get_interfaces_info(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        list_0 = []
        bytes_0 = b':\xd8\xd9-\xf6\xe8\xceo\x95| x[\x8a'
        sun_o_s_network_0 = module_0.SunOSNetwork(bytes_0)
        sun_o_s_network_collector_0 = module_0.SunOSNetworkCollector()
        sun_o_s_network_collector_1 = module_0.SunOSNetworkCollector(sun_o_s_network_collector_0)
        var_0 = sun_o_s_network_0.parse_ether_line(bool_0, set_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 451
        sun_o_s_network_collector_0 = module_0.SunOSNetworkCollector(int_0)
        bytes_0 = b'#\x93Zj\xab\x1b\x95\x9d\xb5\xd6}\xdd\xc9.\xcc,'
        sun_o_s_network_0 = module_0.SunOSNetwork(bytes_0)
        int_1 = -383
        str_0 = 'oF'
        tuple_0 = (sun_o_s_network_0, int_1, str_0)
        list_0 = [tuple_0, str_0, int_1, sun_o_s_network_0]
        str_1 = '!\rh'
        dict_0 = {str_1: str_1}
        sun_o_s_network_1 = module_0.SunOSNetwork(dict_0)
        var_0 = sun_o_s_network_1.parse_ether_line(list_0, tuple_0, int_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\x0c|M\\NQeiMU`3u-Jr5>:'
        sun_o_s_network_collector_0 = module_0.SunOSNetworkCollector()
        sun_o_s_network_0 = module_0.SunOSNetwork(sun_o_s_network_collector_0, sun_o_s_network_collector_0)
        tuple_0 = (sun_o_s_network_0, str_0)
        str_1 = ''
        dict_0 = {str_1: str_0, str_1: str_1, sun_o_s_network_collector_0: str_0}
        sun_o_s_network_1 = module_0.SunOSNetwork(str_0)
        var_0 = sun_o_s_network_1.parse_interface_line(str_0, tuple_0, dict_0)
    except BaseException:
        pass