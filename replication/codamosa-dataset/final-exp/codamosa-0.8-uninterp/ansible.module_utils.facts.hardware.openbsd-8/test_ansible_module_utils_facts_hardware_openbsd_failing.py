# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.openbsd as module_0

def test_case_0():
    try:
        str_0 = 'vtS?_<"I7AN\''
        str_1 = 'uK*m'
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector(str_0)
        int_0 = -1301
        tuple_0 = (open_b_s_d_hardware_collector_0, int_0)
        float_0 = 1.0
        list_0 = [float_0, str_1]
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(tuple_0, list_0)
        var_0 = open_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 429
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(int_0)
        var_0 = open_b_s_d_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bool_0)
        var_0 = open_b_s_d_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ',Xv#PW'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        var_0 = open_b_s_d_hardware_0.get_processor_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        bool_1 = False
        list_0 = [bool_0, bool_1, bool_1, bool_0]
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_0)
        open_b_s_d_hardware_1 = module_0.OpenBSDHardware(open_b_s_d_hardware_0)
        var_0 = open_b_s_d_hardware_1.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bool_0)
        var_0 = open_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass