# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.hpux as module_0

def test_case_0():
    try:
        int_0 = -2125
        h_p_u_x_hardware_0 = module_0.HPUXHardware(int_0)
        var_0 = h_p_u_x_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '@|#tfBy98#r>a ~qu49'
        h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector(str_0)
        str_1 = '\'"ug#L0Y\'~?xc'
        h_p_u_x_hardware_0 = module_0.HPUXHardware(str_1)
        str_2 = ''
        h_p_u_x_hardware_1 = module_0.HPUXHardware(str_2)
        var_0 = h_p_u_x_hardware_1.get_hw_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        complex_0 = None
        h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector(complex_0)
        float_0 = 145.875
        h_p_u_x_hardware_0 = module_0.HPUXHardware(float_0)
        bytes_0 = b'C"2'
        var_0 = h_p_u_x_hardware_0.populate(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ITd#3R7g/m\x0bZv0E<Is<'
        h_p_u_x_hardware_0 = module_0.HPUXHardware(str_0)
        h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector()
        float_0 = -885.559
        var_0 = h_p_u_x_hardware_0.get_memory_facts(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector()
        float_0 = 0.0
        h_p_u_x_hardware_0 = module_0.HPUXHardware(float_0)
        var_0 = h_p_u_x_hardware_0.get_hw_facts(h_p_u_x_hardware_collector_0)
    except BaseException:
        pass