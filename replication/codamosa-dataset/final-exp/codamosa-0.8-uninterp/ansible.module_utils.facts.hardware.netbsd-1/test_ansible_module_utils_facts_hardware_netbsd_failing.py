# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    try:
        bool_0 = True
        str_0 = '%_$pa-xb\nm'
        net_b_s_d_hardware_collector_0 = module_0.NetBSDHardwareCollector(str_0)
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(bool_0)
        var_0 = net_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        net_b_s_d_hardware_0 = module_0.NetBSDHardware(tuple_0)
        var_0 = net_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass