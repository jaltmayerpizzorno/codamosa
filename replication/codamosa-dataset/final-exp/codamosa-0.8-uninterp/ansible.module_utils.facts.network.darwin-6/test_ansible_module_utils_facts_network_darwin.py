# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.darwin as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 1205
    dict_0 = {int_0: int_0, int_0: int_0}
    str_0 = '}nNP'
    set_0 = {str_0}
    darwin_network_0 = module_0.DarwinNetwork(int_0)
    var_0 = darwin_network_0.parse_media_line(str_0, dict_0, set_0)

def test_case_2():
    int_0 = 1181
    dict_0 = {int_0: int_0, int_0: int_0}
    str_0 = '}nP'
    set_0 = {str_0, str_0, str_0}
    bool_0 = False
    darwin_network_0 = module_0.DarwinNetwork(bool_0)
    var_0 = darwin_network_0.parse_media_line(str_0, dict_0, set_0)

def test_case_3():
    str_0 = 'ens33'
    darwin_network_0 = module_0.DarwinNetwork(str_0)
    var_0 = {}
    var_1 = {}
    str_1 = 'media:'
    str_2 = 'autoselect'
    str_3 = '(1000baseT)'
    str_4 = [str_1, str_2, str_3]
    var_2 = darwin_network_0.parse_media_line(str_4, var_0, var_1)
    str_5 = '<unknown'
    str_6 = 'type>'
    str_7 = [str_1, str_5, str_6]
    var_3 = darwin_network_0.parse_media_line(str_7, var_0, var_1)

def test_case_4():
    str_0 = 'ens33'
    darwin_network_0 = module_0.DarwinNetwork(str_0)
    var_0 = {}
    str_1 = 'media:'
    str_2 = 'autoselect'
    str_3 = '(1000baseT)'
    str_4 = [str_1, str_2, str_3]
    var_1 = darwin_network_0.parse_media_line(str_4, var_0, var_0)
    str_5 = '<unknown'
    str_6 = [str_1, str_5, str_3]
    var_2 = darwin_network_0.parse_media_line(str_6, var_0, str_2)