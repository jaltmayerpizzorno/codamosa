# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    try:
        str_0 = '\x0cZkT+\x0c '
        int_0 = 411
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(str_0, int_0)
        var_0 = net_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'whatever'
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(str_0)
        var_0 = net_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass