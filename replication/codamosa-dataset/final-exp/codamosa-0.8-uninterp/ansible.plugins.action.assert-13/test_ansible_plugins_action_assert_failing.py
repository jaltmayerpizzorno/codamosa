# Automatically generated by Pynguin.
import ansible.plugins.action.assert as module_0

def test_case_0():
    try:
        str_0 = '/sbin/sysctl -n kern.version'
        int_0 = -1722
        bytes_0 = b'\xb0o\xcb\x86\xef'
        set_0 = {int_0, str_0, bytes_0, int_0}
        action_module_0 = module_0.ActionModule(str_0, int_0, str_0, set_0, bytes_0, bytes_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'x\xb5b&\xb3%W5\xd6\x1dK\xca\xf4\xcc\x8bN\xbcL'
        bytes_1 = b'b\xb45\x84\xa1\x16\n\x1f\xa3\x85\x08$'
        int_0 = 940
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
        set_0 = {int_0}
        str_0 = 'j srk\x0bK'
        str_1 = 'z{ h~@q>Pzt$[L'
        list_0 = [str_0, str_0, set_0, dict_0]
        action_module_0 = module_0.ActionModule(dict_0, set_0, str_0, str_1, list_0, dict_0)
        var_0 = action_module_0.run(bytes_0, bytes_1)
    except BaseException:
        pass