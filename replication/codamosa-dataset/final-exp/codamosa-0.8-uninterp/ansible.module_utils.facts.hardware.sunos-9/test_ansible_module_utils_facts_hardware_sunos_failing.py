# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.sunos as module_0

def test_case_0():
    try:
        str_0 = 'B[*\r'
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0)
        bool_0 = None
        var_0 = sun_o_s_hardware_0.populate(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'value for config entry {0} contains invalid characters, ignoring...'
        float_0 = 714.2
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector(float_0)
        sun_o_s_hardware_0 = module_0.SunOSHardware(sun_o_s_hardware_collector_0)
        var_0 = sun_o_s_hardware_0.get_cpu_facts(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector(bool_0)
        tuple_0 = ()
        set_0 = {tuple_0, bool_0, bool_0, sun_o_s_hardware_collector_0}
        sun_o_s_hardware_0 = module_0.SunOSHardware(set_0, set_0)
        var_0 = sun_o_s_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector()
        sun_o_s_hardware_0 = module_0.SunOSHardware(sun_o_s_hardware_collector_0)
        var_0 = sun_o_s_hardware_0.get_dmi_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1974
        sun_o_s_hardware_0 = module_0.SunOSHardware(int_0)
        var_0 = sun_o_s_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'tqe\x8eW\x86P~\xe9U5v'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        sun_o_s_hardware_0 = module_0.SunOSHardware(set_0, set_0)
        var_0 = sun_o_s_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = None
        str_0 = 'y_1Cd^hzcbnF5Pq2k'
        sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector()
        sun_o_s_hardware_0 = module_0.SunOSHardware(str_0, sun_o_s_hardware_collector_0)
        var_0 = sun_o_s_hardware_0.get_cpu_facts(bytes_0)
    except BaseException:
        pass