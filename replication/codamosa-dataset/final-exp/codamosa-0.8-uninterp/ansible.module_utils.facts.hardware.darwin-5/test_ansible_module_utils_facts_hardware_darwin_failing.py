# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.darwin as module_0

def test_case_0():
    try:
        int_0 = -4425
        bool_0 = True
        bytes_0 = b'm4\xb0\x1a\xa8C'
        darwin_hardware_0 = module_0.DarwinHardware(bool_0, bytes_0)
        var_0 = darwin_hardware_0.populate(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 2549.3158
        darwin_hardware_0 = module_0.DarwinHardware(float_0)
        var_0 = darwin_hardware_0.get_system_profile()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '_F2}\ra7EDkj<[S\x0b@,N`'
        float_0 = -886.0
        darwin_hardware_0 = module_0.DarwinHardware(str_0, float_0)
        var_0 = darwin_hardware_0.get_mac_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/dev/disk/by-id'
        darwin_hardware_0 = module_0.DarwinHardware(str_0)
        var_0 = darwin_hardware_0.get_cpu_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'ylcq7@miu]2<Bj'
        int_0 = 2755
        dict_0 = {int_0: int_0, str_0: int_0, str_0: int_0, int_0: int_0}
        darwin_hardware_0 = module_0.DarwinHardware(int_0, dict_0)
        set_0 = {str_0}
        darwin_hardware_1 = module_0.DarwinHardware(set_0)
        list_0 = [str_0, set_0, darwin_hardware_1, set_0]
        darwin_hardware_2 = module_0.DarwinHardware(list_0)
        darwin_hardware_3 = module_0.DarwinHardware(str_0)
        var_0 = darwin_hardware_3.get_memory_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'n:\x08\x81\x12u(+]\xf1\xee\t\x87\x14\xe8\x92s_\xd4'
        darwin_hardware_0 = module_0.DarwinHardware(bytes_0)
        var_0 = darwin_hardware_0.get_uptime_facts()
    except BaseException:
        pass