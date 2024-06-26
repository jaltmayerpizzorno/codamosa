# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.hpux as module_0

def test_case_0():
    try:
        set_0 = None
        h_p_u_x_hardware_0 = module_0.HPUXHardware(set_0)
        var_0 = h_p_u_x_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x19\xeb\x12\xeb\x90\xc2\xbd\xb3\x83'
        bytes_1 = b'\xf3\x81\x93\xf8'
        h_p_u_x_hardware_0 = module_0.HPUXHardware(bytes_0, bytes_1)
        var_0 = h_p_u_x_hardware_0.get_hw_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ansible_architecture'
        str_1 = '6'
        str_2 = {str_0: str_0, str_0: str_1, str_0: str_1, str_0: str_1}
        h_p_u_x_hardware_0 = module_0.HPUXHardware(str_2)
        var_0 = h_p_u_x_hardware_0.populate(str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'X^hTBZDt_9'
        str_1 = 'ANSIBLE_HTTPAPI_PLUGINS'
        bool_0 = False
        h_p_u_x_hardware_0 = module_0.HPUXHardware(bool_0)
        h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector(str_1)
        set_0 = {str_0, h_p_u_x_hardware_collector_0, str_1}
        float_0 = 1333.0
        h_p_u_x_hardware_1 = module_0.HPUXHardware(set_0, float_0)
        var_0 = h_p_u_x_hardware_1.get_memory_facts(h_p_u_x_hardware_collector_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '^H&W:m\ndy'
        set_0 = {str_0, str_0, str_0}
        int_0 = 301
        list_0 = [int_0, int_0, int_0]
        h_p_u_x_hardware_0 = module_0.HPUXHardware(list_0)
        h_p_u_x_hardware_1 = module_0.HPUXHardware(int_0, h_p_u_x_hardware_0)
        h_p_u_x_hardware_2 = module_0.HPUXHardware(h_p_u_x_hardware_1)
        var_0 = h_p_u_x_hardware_2.get_hw_facts(set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'ansible_facts'
        str_1 = 'ansible_system_vendor'
        str_2 = 'ansible_architecture'
        str_3 = 'ansible_distribution'
        str_4 = 'ansible_distribution_version'
        str_5 = 'HP '
        str_6 = '9000/800'
        str_7 = 'HP-UX'
        str_8 = 'B.11.11'
        str_9 = {str_1: str_5, str_2: str_6, str_3: str_7, str_4: str_8}
        str_10 = {str_0: str_9}
        var_0 = None
        h_p_u_x_hardware_0 = module_0.HPUXHardware(var_0)
        var_1 = str_10[str_0]
        var_2 = h_p_u_x_hardware_0.populate(var_1)
    except BaseException:
        pass