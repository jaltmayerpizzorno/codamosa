# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    try:
        tuple_0 = ()
        var_0 = module_0.is_running_service(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1192
        tuple_0 = (int_0,)
        var_0 = module_0.is_deactivating_service(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        var_0 = module_0.request_was_ignored(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -2169
        var_0 = module_0.parse_systemctl_show(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = None
        list_0 = [tuple_0]
        var_0 = module_0.parse_systemctl_show(list_0)
    except BaseException:
        pass