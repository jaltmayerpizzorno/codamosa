# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.darwin as module_0

def test_case_0():
    dict_0 = {}
    str_0 = 'kwN11\x0b'
    int_0 = 413
    darwin_network_0 = module_0.DarwinNetwork(int_0)
    var_0 = darwin_network_0.parse_media_line(str_0, dict_0, dict_0)

def test_case_1():
    var_0 = {}
    str_0 = '<unknown'
    str_1 = 'type>'
    str_2 = [str_0, str_0, str_1]
    var_1 = {}
    str_3 = '/sbin/ifconfig'
    darwin_network_0 = module_0.DarwinNetwork(str_3)
    var_2 = darwin_network_0.parse_media_line(str_2, var_0, var_1)

def test_case_2():
    var_0 = {}
    str_0 = 'b6"'
    str_1 = '<unknown'
    str_2 = 'explicit_requirement_{name!s}'
    str_3 = [str_0, str_1, str_2]
    var_1 = {}
    str_4 = '/sbin/ifconfig'
    darwin_network_0 = module_0.DarwinNetwork(str_4)
    var_2 = darwin_network_0.parse_media_line(str_3, var_0, var_1)