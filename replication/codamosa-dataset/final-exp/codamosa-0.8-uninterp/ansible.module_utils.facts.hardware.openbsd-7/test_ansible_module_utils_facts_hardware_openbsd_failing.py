# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.openbsd as module_0

def test_case_0():
    try:
        str_0 = ',HPRBs&]BYp%N4ze&^A<'
        set_0 = {str_0, str_0, str_0}
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(set_0)
        list_0 = [set_0, set_0, set_0, str_0]
        var_0 = open_b_s_d_hardware_0.populate(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'certificate_key_pem'
        tuple_0 = (str_0,)
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(tuple_0)
        var_0 = open_b_s_d_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'C> F17M%g."Z\nP,jf\x0c|A'
        set_0 = {str_0, str_0, str_0, str_0}
        bytes_0 = b'\xc8\xf1\xb8\x95\x89s\x8c\x8f\x17\xb7\x01\xfe'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(set_0, bytes_0)
        var_0 = open_b_s_d_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        open_b_s_d_hardware_collector_0 = None
        tuple_0 = (open_b_s_d_hardware_collector_0,)
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(tuple_0)
        var_0 = open_b_s_d_hardware_0.get_processor_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_0)
        var_0 = open_b_s_d_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 0.0
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(float_0)
        var_0 = open_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass