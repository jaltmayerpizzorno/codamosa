# Automatically generated by Pynguin.
import ansible.module_utils.compat.selinux as module_0

def test_case_0():
    try:
        bytes_0 = None
        var_0 = module_0.selinux_getenforcemode()
        var_1 = module_0.lgetfilecon_raw(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.selinux_getpolicytype()
        var_1 = module_0.selinux_getpolicytype()
        list_0 = []
        var_2 = module_0.lgetfilecon_raw(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        str_0 = '\x0bj^/"SN6'
        var_0 = module_0.selinux_getpolicytype()
        var_1 = module_0.selinux_getenforcemode()
        var_2 = module_0.matchpathcon(bool_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'm'
        var_0 = module_0.lgetfilecon_raw(bytes_0)
    except BaseException:
        pass