# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.darwin as module_0

def test_case_0():
    try:
        str_0 = 'A{'
        darwin_network_0 = module_0.DarwinNetwork(str_0)
        bytes_0 = b'a\x8d\xaf\xa4\xd8\xb3ez\xcc_\xb1\x9ca'
        var_0 = darwin_network_0.parse_media_line(bytes_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1986.0693
        bytes_0 = b'\xe3\xc7'
        bool_0 = True
        float_1 = 1123.906
        darwin_network_0 = module_0.DarwinNetwork(bool_0, float_1)
        darwin_network_collector_0 = module_0.DarwinNetworkCollector()
        bool_1 = True
        darwin_network_collector_1 = None
        dict_0 = {darwin_network_collector_1: darwin_network_0, float_0: darwin_network_collector_1}
        int_0 = -1518
        var_0 = darwin_network_0.parse_media_line(bytes_0, dict_0, int_0)
        var_1 = darwin_network_0.parse_media_line(float_1, bool_1, darwin_network_collector_1)
    except BaseException:
        pass