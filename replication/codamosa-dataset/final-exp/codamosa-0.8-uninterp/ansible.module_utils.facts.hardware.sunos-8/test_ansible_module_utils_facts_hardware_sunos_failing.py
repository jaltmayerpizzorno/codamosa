# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.sunos as module_0

def test_case_0():
    try:
        bool_0 = True
        sun_o_s_hardware_0 = module_0.SunOSHardware(bool_0)
        var_0 = sun_o_s_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ';|$\n:f3'
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0)
        var_0 = sun_o_s_hardware_0.get_cpu_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -911.5702
        int_0 = 1125
        sun_o_s_hardware_0 = module_0.SunOSHardware(float_0, int_0)
        var_0 = sun_o_s_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 1.5
        float_1 = -3012.0
        dict_0 = {float_1: float_0, float_1: float_1}
        bytes_0 = b'\xcd\r\xd4+b'
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector()
        sun_o_s_hardware_collector_1 = module_0.SunOSHardwareCollector(sun_o_s_hardware_collector_0)
        sun_o_s_hardware_collector_2 = module_0.SunOSHardwareCollector(sun_o_s_hardware_collector_1)
        tuple_0 = (float_1, dict_0, bytes_0, sun_o_s_hardware_collector_2)
        sun_o_s_hardware_0 = module_0.SunOSHardware(float_0, tuple_0)
        var_0 = sun_o_s_hardware_0.get_dmi_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        sun_o_s_hardware_0 = module_0.SunOSHardware(bool_0)
        var_0 = sun_o_s_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        tuple_0 = (bool_0, list_0, bool_0)
        sun_o_s_hardware_0 = module_0.SunOSHardware(tuple_0)
        var_0 = sun_o_s_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'N\x87K\x03U\x8ct\xaa'
        str_0 = '3\tKusvDRqZ|\t]!<Dn'
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0)
        var_0 = sun_o_s_hardware_0.get_cpu_facts(bytes_0)
    except BaseException:
        pass