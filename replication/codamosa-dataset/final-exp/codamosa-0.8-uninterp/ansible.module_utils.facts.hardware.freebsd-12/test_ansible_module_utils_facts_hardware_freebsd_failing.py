# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.freebsd as module_0

def test_case_0():
    try:
        int_0 = 384
        list_0 = [int_0, int_0, int_0, int_0]
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(list_0)
        var_0 = free_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'}\xdbhQ+\xbe\x81\x8c\xb7\r\xa1)'
        list_0 = [bytes_0, bytes_0]
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(list_0)
        var_0 = free_b_s_d_hardware_0.get_cpu_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'armv'
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(str_0)
        var_0 = free_b_s_d_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        free_b_s_d_hardware_collector_0 = module_0.FreeBSDHardwareCollector(bool_0)
        str_0 = ''
        str_1 = " |F~fP{|&\x0cF'~WMG\\E["
        bytes_0 = b''
        int_0 = None
        free_b_s_d_hardware_0 = None
        tuple_0 = (bytes_0, int_0, free_b_s_d_hardware_0)
        free_b_s_d_hardware_1 = module_0.FreeBSDHardware(tuple_0)
        var_0 = free_b_s_d_hardware_1.get_device_facts()
        free_b_s_d_hardware_collector_1 = module_0.FreeBSDHardwareCollector(str_1)
        free_b_s_d_hardware_2 = module_0.FreeBSDHardware(str_0)
        var_1 = free_b_s_d_hardware_2.get_uptime_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        free_b_s_d_hardware_collector_0 = module_0.FreeBSDHardwareCollector()
        float_0 = None
        dict_0 = {float_0: float_0, float_0: float_0, float_0: free_b_s_d_hardware_collector_0}
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(dict_0)
        var_0 = free_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass