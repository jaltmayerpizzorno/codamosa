# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    net_b_s_d_hardware_collector_0 = module_0.NetBSDHardwareCollector()

def test_case_1():
    var_0 = {}
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(var_0)
    var_1 = net_b_s_d_hardware_0.get_cpu_facts()

def test_case_2():
    net_b_s_d_hardware_collector_0 = module_0.NetBSDHardwareCollector()
    float_0 = 1.0
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(net_b_s_d_hardware_collector_0, float_0)
    var_0 = net_b_s_d_hardware_0.get_memory_facts()