# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    try:
        int_0 = -1710
        set_0 = {int_0, int_0, int_0, int_0}
        var_0 = module_0.is_running_service(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        var_0 = module_0.is_deactivating_service(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 437
        var_0 = module_0.parse_systemctl_show(int_0)
    except BaseException:
        pass