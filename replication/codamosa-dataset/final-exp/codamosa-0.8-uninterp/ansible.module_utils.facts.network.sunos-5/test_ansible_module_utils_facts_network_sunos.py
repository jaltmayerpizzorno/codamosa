# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.sunos as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\nYgTBXuJF'
    list_0 = [str_0]
    bytes_0 = b'\xad\x0c\xad\x1b>\xd5\xc9\xec5\x8d\xa2\xde\x91\xba\xc2\x10^\xbb\xcb\x07'
    sun_o_s_network_0 = module_0.SunOSNetwork(bytes_0)
    var_0 = sun_o_s_network_0.parse_interface_line(str_0, str_0, list_0)