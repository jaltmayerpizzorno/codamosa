# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.hpux as module_0

def test_case_0():
    try:
        bytes_0 = b'\x8fq\xe6\xe2> \xd1\xdf\x95\x01\xb5\xe0\x1f\x96G\xa0\xd0\x97'
        h_p_u_x_hardware_0 = module_0.HPUXHardware(bytes_0, bytes_0)
        var_0 = h_p_u_x_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '`"L!{Iq'
        h_p_u_x_hardware_0 = module_0.HPUXHardware(str_0)
        var_0 = h_p_u_x_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        h_p_u_x_hardware_0 = module_0.HPUXHardware(dict_0)
        var_0 = h_p_u_x_hardware_0.get_hw_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 60.0
        bytes_0 = b'=\x11\xad\xf4=\x8bF0giF\xd5\xde\x99\x8e\tV'
        h_p_u_x_hardware_0 = module_0.HPUXHardware(bytes_0)
        var_0 = h_p_u_x_hardware_0.populate(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 0.5
        h_p_u_x_hardware_0 = module_0.HPUXHardware(float_0)
        str_0 = 'yb"PE(=WU,JOnnN&{8'
        bool_0 = False
        str_1 = ':|vG#|K<P%m%OEa|)A'
        tuple_0 = (str_0, bool_0, str_1)
        var_0 = h_p_u_x_hardware_0.get_memory_facts(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        float_0 = 214.4624
        h_p_u_x_hardware_0 = module_0.HPUXHardware(bool_0, float_0)
        bytes_0 = b'\xf0Mig\xf0\xa6\xc8'
        bytes_1 = b'\x1c=\t\xee\x86\xb0/\xfbx\xbf\xe04'
        h_p_u_x_hardware_1 = module_0.HPUXHardware(bytes_1)
        var_0 = h_p_u_x_hardware_1.get_hw_facts(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'ansible_architecture'
        str_1 = 'ansible_distribution'
        str_2 = '9000/800'
        str_3 = 'HP-UX'
        str_4 = {str_0: str_2, str_1: str_3}
        h_p_u_x_hardware_0 = module_0.HPUXHardware(str_0, str_4)
        var_0 = h_p_u_x_hardware_0.get_cpu_facts(str_4)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '2U)aeFlD`:g\\wf@h'
        h_p_u_x_hardware_0 = module_0.HPUXHardware(str_0)
        str_1 = 'ansible_architecture'
        str_2 = 'ansible_distribution_version'
        str_3 = 'B.11.23'
        str_4 = 'ia64'
        str_5 = {str_1: str_4, str_2: str_3}
        var_0 = h_p_u_x_hardware_0.get_cpu_facts(str_5)
    except BaseException:
        pass