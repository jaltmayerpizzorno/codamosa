# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.openbsd as module_0

def test_case_0():
    try:
        str_0 = 'R\x0c4(zk('
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        var_0 = open_b_s_d_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(bool_0)
        var_0 = open_b_s_d_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\\`j;@%E1TT<{>'
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(str_0)
        var_0 = open_b_s_d_hardware_0.get_uptime_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        tuple_0 = (dict_0,)
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(tuple_0)
        open_b_s_d_hardware_1 = module_0.OpenBSDHardware(open_b_s_d_hardware_0)
        var_0 = open_b_s_d_hardware_1.get_processor_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = None
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(list_0)
        var_0 = open_b_s_d_hardware_0.get_device_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 381
        open_b_s_d_hardware_0 = module_0.OpenBSDHardware(int_0)
        var_0 = open_b_s_d_hardware_0.get_dmi_facts()
    except BaseException:
        pass