# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.openbsd as module_0

def test_case_0():
    try:
        str_0 = '\rq$aRFe6\x0b#S$zp"'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        var_0 = open_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xd1\x9a\xaa\xcag\x97\xbfCT\x93G\xc8\x07JaO'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bytes_0)
        var_0 = open_b_s_d_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        open_b_s_d_hardware_collector_0 = module_0.OpenBSDHardwareCollector()
        str_0 = "/P('=wB)"
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(open_b_s_d_hardware_collector_0, str_0)
        var_0 = open_b_s_d_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -1635.7666
        list_0 = [float_0]
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_0)
        var_0 = open_b_s_d_hardware_0.get_processor_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bool_0)
        var_0 = open_b_s_d_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 2466.951934491911
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(float_0)
        var_0 = open_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass