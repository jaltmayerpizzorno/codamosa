# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    try:
        str_0 = '[ZjPEC'
        var_0 = module_0.parse_systemctl_show(str_0)
        var_1 = module_0.is_running_service(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '?*G=@_@A=OO&4\ru<@H'
        var_0 = module_0.is_deactivating_service(str_0)
    except BaseException:
        pass