# Automatically generated by Pynguin.
import ansible.plugins.action.unarchive as module_0

def test_case_0():
    try:
        str_0 = 'releasever'
        dict_0 = {str_0: str_0, str_0: str_0}
        bool_0 = False
        list_0 = [dict_0, dict_0, dict_0, str_0]
        action_module_0 = module_0.ActionModule(str_0, dict_0, dict_0, bool_0, dict_0, list_0)
        var_0 = action_module_0.run(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '"jKS4<`CK*K\nBKv;XR(l'
        str_1 = '`?g'
        bytes_0 = b"\x97\xeb\x16\xb2\xce\xd1\r('\xea"
        bool_0 = False
        str_2 = '\\\\(\\d+)'
        list_0 = [str_0, str_1, str_1, bytes_0]
        str_3 = 'UF'
        bytes_1 = b'vhk\xa7\x9d('
        int_0 = -1753
        action_module_0 = module_0.ActionModule(str_2, list_0, str_3, bytes_1, int_0, str_0)
        var_0 = action_module_0.run(bool_0, bool_0)
    except BaseException:
        pass