# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.darwin as module_0

def test_case_0():
    darwin_network_collector_0 = module_0.DarwinNetworkCollector()

def test_case_1():
    str_0 = 'pkg_mgr'
    dict_0 = {}
    bytes_0 = b'\xb2\xd4'
    darwin_network_0 = module_0.DarwinNetwork(str_0)
    var_0 = darwin_network_0.parse_media_line(str_0, dict_0, bytes_0)
    list_0 = []
    darwin_network_collector_0 = module_0.DarwinNetworkCollector(list_0)
    darwin_network_1 = module_0.DarwinNetwork(darwin_network_collector_0)

def test_case_2():
    str_0 = 'kern.boottime'
    darwin_network_collector_0 = module_0.DarwinNetworkCollector(str_0)
    list_0 = [darwin_network_collector_0, darwin_network_collector_0]
    dict_0 = {str_0: str_0, darwin_network_collector_0: str_0}
    bool_0 = True
    bytes_0 = b'RH\xe7/,\x95^\x04\xe2\xdb9\xdci([7\x8b\xb7*'
    bytes_1 = b'\x07\xfe\xcaB\xfb\x9d\xbcI`)\xa6\xe2Z\x16\xf1bg'
    darwin_network_0 = module_0.DarwinNetwork(bytes_0, bytes_1)
    var_0 = darwin_network_0.parse_media_line(list_0, dict_0, bool_0)

def test_case_3():
    str_0 = 'a0:99:9b:74:d4:9f'
    str_1 = 'macaddress'
    str_2 = {str_1: str_0}
    bool_0 = False
    darwin_network_0 = module_0.DarwinNetwork(bool_0, str_2)
    str_3 = 'media:'
    str_4 = 'autoselect'
    str_5 = '(none)'
    str_6 = 'status:'
    str_7 = [str_3, str_4, str_5, str_6, str_3]
    str_8 = ''
    var_0 = darwin_network_0.parse_media_line(str_7, str_2, str_8)
    str_9 = '<unknown'
    str_10 = 'type>'
    str_11 = [str_3, str_9, str_10, str_6, str_6]
    var_1 = darwin_network_0.parse_media_line(str_11, str_2, str_8)

def test_case_4():
    str_0 = 'a0:99:9b:74:d4:9f'
    darwin_network_collector_0 = module_0.DarwinNetworkCollector()
    str_1 = 'macaddress'
    str_2 = {str_1: str_0}
    str_3 = 'media:'
    str_4 = 'autoseb}lect'
    dict_0 = {str_1: str_1, str_4: str_2}
    darwin_network_0 = module_0.DarwinNetwork(dict_0, dict_0)
    str_5 = '(none)'
    str_6 = 'status:'
    str_7 = 'inactive'
    str_8 = [str_3, str_4, str_5, str_6, str_7]
    str_9 = ''
    var_0 = darwin_network_0.parse_media_line(str_8, str_2, str_9)
    str_10 = '<unknown'
    str_11 = [str_3, str_10, str_4, str_6, str_7]
    var_1 = darwin_network_0.parse_media_line(str_11, str_2, str_9)