# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.linux as module_0

def test_case_0():
    try:
        str_0 = '?*V*XD9ep3;|x`v\\'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        str_0 = 'MS-p?\n Rm#r(4M9?F3'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_default_interfaces(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'I>tSdc_~,'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_interfaces_info(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -744.0
        tuple_0 = (float_0,)
        tuple_1 = (tuple_0,)
        linux_network_collector_0 = module_0.LinuxNetworkCollector()
        str_0 = '5XZ'
        linux_network_0 = module_0.LinuxNetwork(linux_network_collector_0, str_0)
        var_0 = linux_network_0.get_ethtool_data(tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 2085
        dict_0 = {int_0: int_0, int_0: int_0}
        list_0 = []
        linux_network_0 = module_0.LinuxNetwork(list_0)
        var_0 = linux_network_0.get_default_interfaces(int_0, dict_0)
    except BaseException:
        pass