# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.darwin as module_0

def test_case_0():
    try:
        bytes_0 = b'\x01\xab\x9a\xfeF\x7f\xccN('
        darwin_network_0 = module_0.DarwinNetwork(bytes_0)
        dict_0 = {}
        str_0 = '\ts'
        darwin_network_collector_0 = module_0.DarwinNetworkCollector(str_0)
        bool_0 = True
        var_0 = darwin_network_0.parse_media_line(str_0, dict_0, bool_0)
        darwin_network_collector_1 = module_0.DarwinNetworkCollector()
        float_0 = -4645.491465
        str_1 = '4H`'
        darwin_network_1 = module_0.DarwinNetwork(float_0)
        int_0 = 2996
        var_1 = darwin_network_1.parse_media_line(str_1, dict_0, int_0)
        darwin_network_2 = module_0.DarwinNetwork(bool_0)
        set_0 = {darwin_network_2, darwin_network_0, darwin_network_2, darwin_network_collector_1}
        str_2 = None
        complex_0 = None
        var_2 = darwin_network_1.parse_media_line(set_0, str_2, complex_0)
    except BaseException:
        pass