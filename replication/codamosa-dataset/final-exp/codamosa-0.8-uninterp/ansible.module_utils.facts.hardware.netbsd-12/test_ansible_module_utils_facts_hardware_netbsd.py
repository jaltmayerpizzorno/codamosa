# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\x0b\x12\x87\xf7\x99)\xb7\xbe\x9eu>\xaa\xec\xb4\x141\x89'
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(bytes_0)
    var_0 = net_b_s_d_hardware_0.get_cpu_facts()

def test_case_2():
    list_0 = []
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(list_0)
    var_0 = net_b_s_d_hardware_0.get_memory_facts()

def test_case_3():
    var_0 = None
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(var_0)
    str_0 = 'sysctl'
    str_1 = 'machdep.dmi.system-product'
    str_2 = 'machdep.dmi.system-version'
    str_3 = 'machdep.dmi.system-serial'
    str_4 = 'machdep.dmi.system-uuid'
    str_5 = 'System Vendor'
    str_6 = 'System Version'
    str_7 = 'System UUID'
    str_8 = {str_5: str_5, str_1: str_4, str_2: str_6, str_3: str_4, str_4: str_7}
    var_1 = setattr(net_b_s_d_hardware_0, str_0, str_8)
    var_2 = net_b_s_d_hardware_0.get_dmi_facts()