# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    try:
        str_0 = '.aL\tL'
        int_0 = -986
        tuple_0 = ()
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(int_0, tuple_0)
        net_b_s_d_hardware_1 = module_0.NetBSDHardware(str_0)
        var_0 = net_b_s_d_hardware_1.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 't\t$&v(%1E0K|/4'
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(str_0)
        var_0 = net_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass