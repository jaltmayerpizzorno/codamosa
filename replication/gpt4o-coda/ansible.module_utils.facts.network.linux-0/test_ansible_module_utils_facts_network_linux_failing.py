# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.linux as module_0

def test_case_0():
    try:
        bytes_0 = b']!|\xc5\xf7\xbas'
        set_0 = {bytes_0}
        str_0 = '3A\nQRBM*'
        linux_network_collector_0 = module_0.LinuxNetworkCollector(str_0)
        linux_network_collector_1 = module_0.LinuxNetworkCollector()
        linux_network_0 = module_0.LinuxNetwork(set_0)
        var_0 = linux_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 1048
        linux_network_0 = module_0.LinuxNetwork(int_0)
        var_0 = linux_network_0.get_default_interfaces(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xfd\x1a'
        linux_network_0 = module_0.LinuxNetwork(bytes_0)
        var_0 = linux_network_0.get_interfaces_info(bytes_0, bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xcd\xe4\xe5%\x8e\xf9\x9b\xe7\x8d\xa5\x0b\xd2#'
        linux_network_collector_0 = module_0.LinuxNetworkCollector(bytes_0)
        int_0 = -1896
        tuple_0 = (int_0, bytes_0, bytes_0)
        str_0 = 'FYhHAx)Bg-\t\rxU'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_ethtool_data(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1303
        linux_network_0 = module_0.LinuxNetwork(int_0)
        var_0 = linux_network_0.get_default_interfaces(int_0, linux_network_0)
    except BaseException:
        pass