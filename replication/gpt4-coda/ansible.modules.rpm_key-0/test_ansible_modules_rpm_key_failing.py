# Automatically generated by Pynguin.
import ansible.modules.rpm_key as module_0

def test_case_0():
    try:
        int_0 = 603
        rpm_key_0 = module_0.RpmKey(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0]
        var_0 = module_0.is_pubkey(list_0)
        bytes_0 = b'\xce\xdb\xba\xc4I\x12\xf2\xe9A\xd2\xfeY\xd4'
        rpm_key_0 = module_0.RpmKey(bytes_0)
    except BaseException:
        pass