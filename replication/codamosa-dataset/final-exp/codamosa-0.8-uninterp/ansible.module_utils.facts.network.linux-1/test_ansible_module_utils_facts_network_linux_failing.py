# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.linux as module_0

def test_case_0():
    try:
        bool_0 = True
        int_0 = 1148
        linux_network_0 = module_0.LinuxNetwork(bool_0, int_0)
        var_0 = linux_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b't'
        linux_network_0 = module_0.LinuxNetwork(bytes_0)
        var_0 = linux_network_0.get_default_interfaces(linux_network_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b't'
        linux_network_0 = module_0.LinuxNetwork(bytes_0)
        var_0 = linux_network_0.get_interfaces_info(linux_network_0, bytes_0, linux_network_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'mS/p\x0cj\\U\n})zhaZug'
        str_1 = 'bH:j.A2X>GeR(KcV'
        str_2 = 'iGE]ufT"*H4R>\\}8'
        linux_network_0 = module_0.LinuxNetwork(str_1, str_2)
        var_0 = linux_network_0.get_ethtool_data(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\x01\x80_\xe7\xc1\x19\xa8\x7f\xee\x15'
        linux_network_0 = module_0.LinuxNetwork(bytes_0)
        list_0 = [bytes_0, bytes_0, bytes_0]
        int_0 = 893
        var_0 = linux_network_0.get_default_interfaces(list_0, int_0)
    except BaseException:
        pass