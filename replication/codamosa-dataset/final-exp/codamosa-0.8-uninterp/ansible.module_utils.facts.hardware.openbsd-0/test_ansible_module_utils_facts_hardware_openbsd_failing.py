# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.openbsd as module_0

def test_case_0():
    try:
        float_0 = -341.5
        list_0 = [float_0, float_0, float_0, float_0]
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_0)
        var_0 = open_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -341.5
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(float_0)
        var_0 = open_b_s_d_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x1bzt\x86r\x95I:6o'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bytes_0)
        var_0 = open_b_s_d_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector()
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0, tuple_0]
        open_b_s_d_hardware_collector_1 = module_0.OpenBSDHardwareCollector(list_0)
        set_0 = {tuple_0, tuple_0}
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(tuple_0, set_0)
        var_0 = open_b_s_d_hardware_0.get_processor_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector()
        float_0 = -2338.7
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(open_b_s_d_hardware_collector_0, float_0)
        var_0 = open_b_s_d_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -12.819575931812329
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(float_0)
        var_0 = open_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass