# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.openbsd as module_0

def test_case_0():
    try:
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector()
        float_0 = -395.67834
        dict_0 = {}
        open_b_s_d_hardware_collector_1 = module_0.OpenBSDHardwareCollector()
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(dict_0)
        open_b_s_d_hardware_1 = module_0.OpenBSDHardware(float_0, open_b_s_d_hardware_0)
        var_0 = open_b_s_d_hardware_1.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(set_0)
        open_b_s_d_hardware_1 = module_0.OpenBSDHardware(open_b_s_d_hardware_0)
        var_0 = open_b_s_d_hardware_1.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\x0c\\I&RkjfT h=3/\x0bx'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        var_0 = open_b_s_d_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector()
        str_0 = 'T0<h&^h,~S>\\1YB.u'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        var_0 = open_b_s_d_hardware_0.get_processor_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'de6'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        var_0 = open_b_s_d_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "tlvO^]\x0cW/5)}@'Rf>=>q"
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        var_0 = open_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass