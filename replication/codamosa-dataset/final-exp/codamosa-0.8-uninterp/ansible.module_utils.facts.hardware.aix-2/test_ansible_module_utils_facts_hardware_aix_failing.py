# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.aix as module_0

def test_case_0():
    try:
        int_0 = 3690
        a_i_x_hardware_0 = module_0.AIXHardware(int_0)
        bool_0 = False
        str_0 = '^hzv.3o\rXs[N]5]`1-'
        tuple_0 = (a_i_x_hardware_0, bool_0, str_0)
        a_i_x_hardware_1 = module_0.AIXHardware(tuple_0)
        var_0 = a_i_x_hardware_1.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        a_i_x_hardware_0 = module_0.AIXHardware(bool_0)
        var_0 = a_i_x_hardware_0.get_cpu_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        a_i_x_hardware_collector_0 = module_0.AIXHardwareCollector(list_0)
        a_i_x_hardware_0 = module_0.AIXHardware(a_i_x_hardware_collector_0)
        var_0 = a_i_x_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ')X-:<'
        bool_0 = False
        a_i_x_hardware_collector_0 = module_0.AIXHardwareCollector(str_0, bool_0)
        a_i_x_hardware_0 = module_0.AIXHardware(a_i_x_hardware_collector_0)
        var_0 = a_i_x_hardware_0.get_dmi_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        a_i_x_hardware_collector_0 = module_0.AIXHardwareCollector()
        tuple_0 = ()
        a_i_x_hardware_0 = None
        tuple_1 = (tuple_0, a_i_x_hardware_0, a_i_x_hardware_collector_0)
        a_i_x_hardware_1 = module_0.AIXHardware(tuple_1, a_i_x_hardware_collector_0)
        var_0 = a_i_x_hardware_1.get_vgs_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'A'
        tuple_0 = ()
        float_0 = 1321.20239
        a_i_x_hardware_0 = module_0.AIXHardware(float_0, bytes_0)
        tuple_1 = (bytes_0, tuple_0, tuple_0, a_i_x_hardware_0)
        str_0 = '(\\(\\D+\\))|,(\\s+)?\\D+'
        a_i_x_hardware_1 = module_0.AIXHardware(tuple_1, str_0)
        var_0 = a_i_x_hardware_1.get_mount_facts()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\xbc5\xd6u\xb9\xf9)I'
        a_i_x_hardware_0 = module_0.AIXHardware(bytes_0)
        var_0 = a_i_x_hardware_0.get_device_facts()
    except BaseException:
        pass