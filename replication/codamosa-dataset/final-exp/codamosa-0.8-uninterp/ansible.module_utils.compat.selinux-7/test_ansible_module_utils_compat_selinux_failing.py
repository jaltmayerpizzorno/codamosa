# Automatically generated by Pynguin.
import ansible.module_utils.compat.selinux as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.lgetfilecon_raw(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = None
        set_0 = {tuple_0, tuple_0, tuple_0, tuple_0}
        var_0 = module_0.matchpathcon(tuple_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = module_0.selinux_getenforcemode()
        bytes_0 = b'r\xa6:\xb3;Qm\xac(K\x05\x9f'
        var_1 = module_0.lgetfilecon_raw(bytes_0)
    except BaseException:
        pass