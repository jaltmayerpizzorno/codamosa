# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.sunos as module_0

def test_case_0():
    try:
        str_0 = 'YIi,}cT@&L.aeG4{8jl'
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0)
        var_0 = sun_o_s_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\\}XI.'
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector()
        tuple_0 = (sun_o_s_hardware_collector_0,)
        sun_o_s_hardware_0 = module_0.SunOSHardware(tuple_0)
        var_0 = sun_o_s_hardware_0.get_cpu_facts(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 965
        int_1 = 493
        list_0 = [int_0, int_0, int_0, int_1]
        sun_o_s_hardware_0 = module_0.SunOSHardware(list_0)
        var_0 = sun_o_s_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector()
        bool_0 = False
        sun_o_s_hardware_0 = module_0.SunOSHardware(bool_0)
        var_0 = sun_o_s_hardware_0.get_dmi_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector(bool_0)
        sun_o_s_hardware_collector_1 = module_0.SunOSHardwareCollector(sun_o_s_hardware_collector_0)
        sun_o_s_hardware_collector_2 = module_0.SunOSHardwareCollector(sun_o_s_hardware_collector_1)
        dict_0 = {}
        sun_o_s_hardware_0 = module_0.SunOSHardware(dict_0)
        var_0 = sun_o_s_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector()
        str_0 = '3w#d-Uoy]V$-n0'
        sun_o_s_hardware_0 = module_0.SunOSHardware(sun_o_s_hardware_collector_0, str_0)
        var_0 = sun_o_s_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1106
        list_0 = []
        dict_0 = {int_0: list_0, int_0: int_0, int_0: int_0}
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector(dict_0)
        float_0 = 1486.8682
        sun_o_s_hardware_0 = module_0.SunOSHardware(float_0)
        var_0 = sun_o_s_hardware_0.get_cpu_facts(list_0)
    except BaseException:
        pass