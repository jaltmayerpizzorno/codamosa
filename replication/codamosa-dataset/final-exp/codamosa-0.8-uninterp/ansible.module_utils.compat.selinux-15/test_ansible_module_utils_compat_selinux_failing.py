# Automatically generated by Pynguin.
import ansible.module_utils.compat.selinux as module_0

def test_case_0():
    try:
        bool_0 = None
        var_0 = module_0.lgetfilecon_raw(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '%s -y %s %s %s %s %s %s %s'
        list_0 = [str_0]
        str_1 = '>(Mq\x0b/iV|&["\\y],d\\R'
        var_0 = module_0.matchpathcon(list_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = module_0.selinux_getenforcemode()
        var_1 = module_0.selinux_getpolicytype()
        bytes_0 = b'~\x92\x80\xa1\xf2\xc7\xed5\x12j\xcf\xda\xc0\xcf\xa5H\xa8\xbc\xe7r'
        var_2 = module_0.lgetfilecon_raw(bytes_0)
    except BaseException:
        pass