# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    try:
        str_0 = '1KamLpn'
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(str_0)
        bytes_0 = b'\x0c\x12/Y\x9ej{\xf5V n\xcdx\xc4\x02\x15'
        net_b_s_d_hardware_1 = module_0.NetBSDHardware(bytes_0)
        var_0 = net_b_s_d_hardware_1.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(dict_0)
        var_0 = net_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass