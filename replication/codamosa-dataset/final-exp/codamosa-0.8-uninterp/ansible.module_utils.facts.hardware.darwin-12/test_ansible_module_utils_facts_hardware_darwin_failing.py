# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.darwin as module_0

def test_case_0():
    try:
        float_0 = -110.859
        darwin_hardware_0 = module_0.DarwinHardware(float_0)
        var_0 = darwin_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        darwin_hardware_0 = module_0.DarwinHardware(list_0)
        darwin_hardware_1 = module_0.DarwinHardware(darwin_hardware_0)
        var_0 = darwin_hardware_1.get_system_profile()
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 1983.0
        darwin_hardware_collector_0 = module_0.DarwinHardwareCollector()
        darwin_hardware_0 = module_0.DarwinHardware(float_0, darwin_hardware_collector_0)
        var_0 = darwin_hardware_0.get_mac_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        darwin_hardware_0 = module_0.DarwinHardware(bool_0)
        bool_1 = True
        dict_0 = {bool_1: bool_1, bool_1: bool_1, bool_1: bool_1}
        darwin_hardware_1 = module_0.DarwinHardware(bool_1, dict_0)
        tuple_0 = (darwin_hardware_1,)
        darwin_hardware_collector_0 = module_0.DarwinHardwareCollector(tuple_0)
        var_0 = darwin_hardware_0.get_cpu_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'y_\\lN6Q;\x0cY;/3_z<M+0O'
        darwin_hardware_collector_0 = module_0.DarwinHardwareCollector(str_0)
        darwin_hardware_0 = module_0.DarwinHardware(darwin_hardware_collector_0)
        var_0 = darwin_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 998
        bytes_0 = b'|\xe0'
        darwin_hardware_0 = module_0.DarwinHardware(int_0, bytes_0)
        var_0 = darwin_hardware_0.get_uptime_facts()
    except BaseException:
        pass