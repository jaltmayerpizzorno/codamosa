# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.linux as module_0

def test_case_0():
    try:
        str_0 = '-_9bFg(sdlR-'
        str_1 = 'x1z`UE'
        set_0 = {str_1, str_1, str_1}
        str_2 = None
        tuple_0 = (set_0, str_1, str_2)
        linux_network_0 = module_0.LinuxNetwork(tuple_0)
        var_0 = linux_network_0.populate(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_default_interfaces(linux_network_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        linux_network_0 = module_0.LinuxNetwork(str_0)
        int_0 = -1375
        var_0 = linux_network_0.get_interfaces_info(str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        linux_network_collector_0 = module_0.LinuxNetworkCollector(bool_0)
        list_0 = [linux_network_collector_0, bool_0, bool_0, linux_network_collector_0]
        str_0 = 'Qm"!'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_ethtool_data(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -2048.985
        linux_network_0 = module_0.LinuxNetwork(float_0)
        set_0 = set()
        str_0 = '\x0c\r\\'
        var_0 = linux_network_0.get_default_interfaces(set_0, str_0)
    except BaseException:
        pass