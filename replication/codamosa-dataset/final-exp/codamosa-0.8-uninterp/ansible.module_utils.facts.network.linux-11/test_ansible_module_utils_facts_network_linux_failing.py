# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.linux as module_0

def test_case_0():
    try:
        bytes_0 = b'\xae;\xb3\xa3\xb0\x0bH\xeb\xfc\x9c4=\xb4#'
        linux_network_0 = module_0.LinuxNetwork(bytes_0)
        var_0 = linux_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'I@=!q\x0bQC#kbf'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_default_interfaces(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Y"_\x0bSZ2!;+W?$3S`T'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        int_0 = 3099
        var_0 = linux_network_0.get_interfaces_info(str_0, int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = None
        str_0 = 'CzQrp\\H8&zvG<m'
        linux_network_0 = module_0.LinuxNetwork(str_0)
        var_0 = linux_network_0.get_ethtool_data(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = set()
        float_0 = -3401.014
        linux_network_0 = module_0.LinuxNetwork(float_0)
        var_0 = linux_network_0.get_default_interfaces(set_0)
    except BaseException:
        pass