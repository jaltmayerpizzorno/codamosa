# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.darwin as module_0

def test_case_0():
    try:
        bytes_0 = b'5%X1\xd4'
        float_0 = 100.0
        set_0 = {bytes_0, bytes_0, float_0}
        str_0 = '3:8A"\nd09JmWg#hO'
        list_0 = [set_0, bytes_0, str_0]
        darwin_hardware_0 = module_0.DarwinHardware(list_0)
        var_0 = darwin_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 4685
        darwin_hardware_0 = module_0.DarwinHardware(int_0)
        var_0 = darwin_hardware_0.get_system_profile()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'OL|<T7r7SZ"\x0c'
        tuple_0 = (str_0,)
        darwin_hardware_0 = module_0.DarwinHardware(tuple_0)
        var_0 = darwin_hardware_0.get_mac_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        darwin_hardware_collector_0 = module_0.DarwinHardwareCollector()
        set_0 = {darwin_hardware_collector_0, darwin_hardware_collector_0, darwin_hardware_collector_0}
        darwin_hardware_0 = module_0.DarwinHardware(set_0)
        darwin_hardware_1 = module_0.DarwinHardware(darwin_hardware_0)
        var_0 = darwin_hardware_1.get_cpu_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -2160
        darwin_hardware_0 = module_0.DarwinHardware(int_0)
        var_0 = darwin_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 2733
        darwin_hardware_0 = module_0.DarwinHardware(int_0)
        var_0 = darwin_hardware_0.get_uptime_facts()
    except BaseException:
        pass