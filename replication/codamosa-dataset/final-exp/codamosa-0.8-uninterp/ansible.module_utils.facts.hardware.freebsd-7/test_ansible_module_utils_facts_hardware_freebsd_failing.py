# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.freebsd as module_0

def test_case_0():
    try:
        bytes_0 = b'j$yzo{=_J\xdc\xcb2R\xff\xb7\x1b'
        free_b_s_d_hardware_collector_0 = module_0.FreeBSDHardwareCollector()
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(free_b_s_d_hardware_collector_0)
        var_0 = free_b_s_d_hardware_0.populate(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        bytes_0 = b'\x8a\xd9\xaem'
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(list_0, bytes_0)
        var_0 = free_b_s_d_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xdbSl5/d!\x85\xd1\n'
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(bytes_0)
        var_0 = free_b_s_d_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        free_b_s_d_hardware_collector_0 = module_0.FreeBSDHardwareCollector()
        int_0 = 373
        bool_0 = True
        free_b_s_d_hardware_0 = module_0.FreeBSDHardware(int_0, bool_0)
        var_0 = free_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass