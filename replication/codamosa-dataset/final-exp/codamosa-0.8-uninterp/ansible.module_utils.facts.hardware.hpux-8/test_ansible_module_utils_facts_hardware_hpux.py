# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.hpux as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = {}
    h_p_u_x_hardware_0 = module_0.HPUXHardware(var_0)
    str_0 = 'ansible_architecture'
    str_1 = 'ansible_distribution_version'
    str_2 = 'ia64'
    str_3 = {str_0: str_2, str_1: str_2}
    var_1 = h_p_u_x_hardware_0.get_cpu_facts(str_3)