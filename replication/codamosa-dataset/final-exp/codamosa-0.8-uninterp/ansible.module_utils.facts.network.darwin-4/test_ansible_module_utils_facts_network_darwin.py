# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.darwin as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = None
    darwin_network_0 = module_0.DarwinNetwork(float_0)
    dict_0 = {}
    darwin_network_collector_0 = module_0.DarwinNetworkCollector()
    str_0 = 'K-/st.}\rbx,t\x0b'
    bool_0 = None
    var_0 = darwin_network_0.parse_media_line(str_0, dict_0, bool_0)

def test_case_2():
    var_0 = {}
    var_1 = None
    darwin_network_0 = module_0.DarwinNetwork(var_0, var_1)
    var_2 = {}
    str_0 = 'media:'
    str_1 = 'auto'
    str_2 = 'select'
    str_3 = '(none)'
    str_4 = [str_0, str_1, str_2, str_3]
    var_3 = []
    var_4 = darwin_network_0.parse_media_line(str_4, var_2, var_3)
    var_5 = {}
    str_5 = '<unknown'
    str_6 = 'type>'
    str_7 = [str_0, str_5, str_6]
    var_6 = []
    var_7 = darwin_network_0.parse_media_line(str_7, var_5, var_6)