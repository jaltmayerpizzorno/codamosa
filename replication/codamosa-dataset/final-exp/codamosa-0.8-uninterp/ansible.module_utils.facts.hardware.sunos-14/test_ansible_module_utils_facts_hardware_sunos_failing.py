# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.sunos as module_0

def test_case_0():
    try:
        str_0 = '0Yxxd2\tVPCIXS\rly"D'
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0)
        var_0 = sun_o_s_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        list_0 = [set_0, set_0, set_0, set_0]
        bool_0 = False
        float_0 = 0.001
        sun_o_s_hardware_0 = module_0.SunOSHardware(bool_0, float_0)
        sun_o_s_hardware_1 = module_0.SunOSHardware(list_0)
        bytes_0 = b'Z&\x87\x1e\xa5\xcbG\x164\xc1\x0b\x9f~J'
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector(bytes_0)
        var_0 = sun_o_s_hardware_1.get_cpu_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'z..4N7%7J^(,ZYk9LW'
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0)
        var_0 = sun_o_s_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'V#nJ0-\reZ'
        bool_0 = True
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0, bool_0)
        int_0 = -31
        sun_o_s_hardware_1 = module_0.SunOSHardware(int_0)
        var_0 = sun_o_s_hardware_1.get_dmi_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'B]i#E@S,8\x0b!T]kx/\n'
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0)
        var_0 = sun_o_s_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -1828
        sun_o_s_hardware_0 = module_0.SunOSHardware(int_0)
        var_0 = sun_o_s_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -38
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector(int_0)
        sun_o_s_hardware_0 = module_0.SunOSHardware(sun_o_s_hardware_collector_0)
        bytes_0 = b'\xa9a5(_\xf4\x1e\x91dA\x17\x81\xcf'
        var_0 = sun_o_s_hardware_0.get_cpu_facts(bytes_0)
    except BaseException:
        pass