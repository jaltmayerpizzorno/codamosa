# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.hpux as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'B.11.31'
    h_p_u_x_hardware_0 = module_0.HPUXHardware(str_0)
    str_1 = 'ansible_architecture'
    str_2 = 'ia64'
    str_3 = {str_1: str_2, str_1: str_0}
    var_0 = h_p_u_x_hardware_0.get_cpu_facts(str_3)

def test_case_2():
    str_0 = '9000/800'
    h_p_u_x_hardware_0 = module_0.HPUXHardware(str_0)
    str_1 = 'ansible_architecture'
    str_2 = 'ansible_distribution_version'
    str_3 = 'ia64'
    str_4 = {str_1: str_3, str_2: str_2}
    var_0 = h_p_u_x_hardware_0.get_cpu_facts(str_4)