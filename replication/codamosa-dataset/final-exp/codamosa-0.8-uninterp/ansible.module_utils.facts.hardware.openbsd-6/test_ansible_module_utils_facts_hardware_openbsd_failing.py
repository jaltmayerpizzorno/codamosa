# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.openbsd as module_0

def test_case_0():
    try:
        bool_0 = True
        set_0 = {bool_0, bool_0, bool_0}
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(set_0)
        var_0 = open_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'>)c$\xebd\xe7@\x96\x06\xb5G\xad\x85\xfc%\x01'
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector(bytes_0)
        float_0 = -234.913187
        float_1 = -3169.5
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(float_1)
        open_b_s_d_hardware_1 = module_0.OpenBSDHardware(float_0, open_b_s_d_hardware_0)
        open_b_s_d_hardware_2 = module_0.OpenBSDHardware(open_b_s_d_hardware_collector_0, open_b_s_d_hardware_1)
        var_0 = open_b_s_d_hardware_2.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xaaL7'
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector(bytes_0, bytes_0)
        tuple_0 = ()
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(tuple_0)
        var_0 = open_b_s_d_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 4637
        list_0 = [int_0, int_0, int_0, int_0]
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_0)
        var_0 = open_b_s_d_hardware_0.get_processor_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0]
        int_0 = 429
        float_0 = 0.0
        tuple_0 = (list_0, int_0, float_0)
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(tuple_0)
        var_0 = open_b_s_d_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = []
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_0)
        var_0 = open_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass