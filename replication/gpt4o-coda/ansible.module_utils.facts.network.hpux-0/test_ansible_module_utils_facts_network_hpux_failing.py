# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.hpux as module_0

def test_case_0():
    try:
        bytes_0 = b'\xc2\xcd\xb1\x8c\xaa\x88\xb2\xdbs\x86\xb3.\x87\xb6\xad'
        h_p_u_x_network_0 = module_0.HPUXNetwork(bytes_0)
        var_0 = h_p_u_x_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1874
        h_p_u_x_network_0 = module_0.HPUXNetwork(int_0)
        var_0 = h_p_u_x_network_0.get_default_interfaces()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 304
        int_1 = -2493
        h_p_u_x_network_0 = module_0.HPUXNetwork(int_0, int_1)
        var_0 = h_p_u_x_network_0.get_interfaces_info()
    except BaseException:
        pass