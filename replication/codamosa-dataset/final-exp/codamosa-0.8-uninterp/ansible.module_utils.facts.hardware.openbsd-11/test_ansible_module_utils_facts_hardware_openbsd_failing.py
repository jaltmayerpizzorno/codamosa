# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.openbsd as module_0

def test_case_0():
    try:
        int_0 = -2869
        int_1 = -2506
        dict_0 = {int_1: int_1, int_1: int_0, int_1: int_0}
        tuple_0 = (int_1, dict_0)
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector()
        tuple_1 = (int_0, tuple_0, open_b_s_d_hardware_collector_0)
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(tuple_1)
        var_0 = open_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bool_0)
        var_0 = open_b_s_d_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "V%d+C/LZNCt{'"
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        str_1 = 's'
        list_0 = [open_b_s_d_hardware_0, str_1, open_b_s_d_hardware_0]
        open_b_s_d_hardware_1 = module_0.OpenBSDHardware(open_b_s_d_hardware_0, list_0)
        var_0 = open_b_s_d_hardware_1.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 2618
        set_0 = {int_0, int_0, int_0, int_0}
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(set_0)
        var_0 = open_b_s_d_hardware_0.get_processor_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b''
        float_0 = -280.6
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bytes_0, float_0)
        var_0 = open_b_s_d_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b''
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bytes_0)
        var_0 = open_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass