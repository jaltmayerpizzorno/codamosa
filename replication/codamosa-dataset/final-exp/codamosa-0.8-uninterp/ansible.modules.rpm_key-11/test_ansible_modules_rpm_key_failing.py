# Automatically generated by Pynguin.
import ansible.modules.rpm_key as module_0

def test_case_0():
    try:
        int_0 = 443
        var_0 = module_0.is_pubkey(int_0)
        float_0 = -1513.449
        rpm_key_0 = module_0.RpmKey(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        rpm_key_0 = module_0.RpmKey(bool_0)
    except BaseException:
        pass