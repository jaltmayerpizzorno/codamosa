# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.darwin as module_0

def test_case_0():
    darwin_network_collector_0 = module_0.DarwinNetworkCollector()

def test_case_1():
    bytes_0 = b'{V\xbbZ0h\x173\xa4`\x97\xfc'
    darwin_network_0 = module_0.DarwinNetwork(bytes_0)
    str_0 = 'Append a new error to ``self.errors``.\n\n        Only :class:`AnsibleValidationError` should be added.\n        '
    float_0 = 0.5
    dict_0 = {str_0: str_0, str_0: bytes_0, str_0: float_0}
    var_0 = darwin_network_0.parse_media_line(str_0, dict_0, float_0)

def test_case_2():
    var_0 = None
    darwin_network_0 = module_0.DarwinNetwork(var_0)
    str_0 = 'ifname'
    str_1 = 'bridge0'
    str_2 = {str_0: str_1}
    str_3 = '<unknown'
    str_4 = 'type>'
    str_5 = '('
    str_6 = 'automatic'
    str_7 = ')'
    str_8 = [str_5, str_3, str_4, str_5, str_6, str_7]
    var_1 = []
    var_2 = darwin_network_0.parse_media_line(str_8, str_2, var_1)

def test_case_3():
    var_0 = None
    darwin_network_0 = module_0.DarwinNetwork(var_0)
    str_0 = 'ifname'
    str_1 = 'bridge0'
    str_2 = {str_0: str_1}
    str_3 = '<unknown'
    str_4 = 'type\\>'
    str_5 = 'automatic'
    str_6 = ')'
    str_7 = [str_3, str_3, str_4, str_1, str_5, str_6]
    var_1 = []
    var_2 = darwin_network_0.parse_media_line(str_7, str_2, var_1)