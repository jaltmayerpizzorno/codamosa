# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.linux as module_0

def test_case_0():
    try:
        linux_network_collector_0 = module_0.LinuxNetworkCollector()
        int_0 = 1919
        linux_network_0 = module_0.LinuxNetwork(int_0)
        var_0 = linux_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x0bS\xc7\x94y\xe0'
        str_0 = 'Ik'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_default_interfaces(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'jb'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_interfaces_info(str_0, str_0, linux_network_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        bytes_0 = None
        linux_network_collector_0 = module_0.LinuxNetworkCollector(bytes_0)
        set_0 = {linux_network_collector_0, bytes_0}
        linux_network_0 = module_0.LinuxNetwork(set_0)
        var_0 = linux_network_0.get_ethtool_data(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'p9c[(5B8,)<9{'
        dict_0 = {str_0: str_0, str_0: str_0}
        int_0 = 32
        linux_network_0 = module_0.LinuxNetwork(int_0)
        var_0 = linux_network_0.get_default_interfaces(str_0, dict_0)
    except BaseException:
        pass