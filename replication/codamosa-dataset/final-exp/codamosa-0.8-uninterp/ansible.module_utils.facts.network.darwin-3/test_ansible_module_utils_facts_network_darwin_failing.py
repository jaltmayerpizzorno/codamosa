# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.darwin as module_0

def test_case_0():
    try:
        str_0 = '-i'
        set_0 = {str_0, str_0, str_0, str_0}
        darwin_network_collector_0 = module_0.DarwinNetworkCollector()
        bytes_0 = b'hvy\xf9F0'
        float_0 = 1028.0
        darwin_network_0 = module_0.DarwinNetwork(float_0)
        var_0 = darwin_network_0.parse_media_line(set_0, darwin_network_collector_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 448
        dict_0 = {int_0: int_0, int_0: int_0}
        bool_0 = None
        float_0 = -3275.02
        darwin_network_0 = module_0.DarwinNetwork(float_0)
        tuple_0 = (bool_0,)
        float_1 = 2886.07
        str_0 = ' ?(:|：) ?'
        darwin_network_1 = module_0.DarwinNetwork(float_1, str_0)
        var_0 = darwin_network_1.parse_media_line(int_0, dict_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        darwin_network_collector_0 = module_0.DarwinNetworkCollector()
        str_0 = '<unknown'
        dict_0 = {}
        bytes_0 = b'\xe0\x8eX{d\xae\n\x17\xf1SBO\xc0\t>\xdci\xca?\x0c'
        bool_0 = False
        tuple_0 = (darwin_network_collector_0, bool_0, darwin_network_collector_0)
        str_1 = 'NuG?[\rrca;Vqu\\`e2'
        darwin_network_0 = module_0.DarwinNetwork(tuple_0, str_1)
        var_0 = darwin_network_0.parse_media_line(str_0, dict_0, bytes_0)
        darwin_network_1 = module_0.DarwinNetwork(darwin_network_collector_0)
        darwin_network_collector_1 = module_0.DarwinNetworkCollector()
        tuple_1 = ()
        var_1 = darwin_network_0.parse_media_line(bytes_0, tuple_1, tuple_0)
    except BaseException:
        pass