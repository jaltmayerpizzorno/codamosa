# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b']\xcd3\xa2\xc2\xa0!\xcc+w\x90\xf9\xc9\x0e`\xc8\x00'
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(bytes_0)
    var_0 = net_b_s_d_hardware_0.get_cpu_facts()

def test_case_2():
    list_0 = None
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(list_0)
    var_0 = net_b_s_d_hardware_0.get_memory_facts()