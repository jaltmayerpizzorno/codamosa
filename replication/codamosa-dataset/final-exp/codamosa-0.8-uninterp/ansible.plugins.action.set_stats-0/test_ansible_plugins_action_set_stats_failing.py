# Automatically generated by Pynguin.
import ansible.plugins.action.set_stats as module_0

def test_case_0():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        action_module_0 = None
        set_0 = {action_module_0, action_module_0, action_module_0, action_module_0}
        float_0 = -3469.8502
        int_0 = 5445
        str_0 = 'sha256'
        bool_1 = False
        action_module_1 = module_0.ActionModule(set_0, float_0, int_0, int_0, str_0, bool_1)
        var_0 = action_module_1.run(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        float_0 = -764.6173
        bool_1 = True
        bytes_0 = b'\xb4\xbf\x9b\xba\xfb]VI\x05m\xc8\xaa'
        str_0 = 'B.'
        bool_2 = False
        list_0 = [float_0, bool_2]
        bytes_1 = b'\xea\xe5$\xce\xc9\xb0\x8a'
        action_module_0 = module_0.ActionModule(bytes_0, str_0, bool_2, list_0, bytes_1, float_0)
        list_1 = [bool_1, bool_1, bool_1, bool_1]
        float_1 = -1230.0
        set_0 = {float_1}
        str_1 = "Unable to determine module's fully qualified name"
        str_2 = '7di/1v*LCDMrrtG`a9'
        str_3 = 'H&~{_<.>S\rX\n(,;6=\\x'
        dict_0 = {str_3: str_2, bool_1: list_0, action_module_0: list_1, str_1: action_module_0}
        action_module_1 = module_0.ActionModule(str_3, list_1, dict_0, bool_2, set_0, str_2)
        action_module_2 = module_0.ActionModule(list_1, float_1, set_0, str_1, list_1, str_2)
        var_0 = action_module_2.run(bool_0, float_0)
    except BaseException:
        pass