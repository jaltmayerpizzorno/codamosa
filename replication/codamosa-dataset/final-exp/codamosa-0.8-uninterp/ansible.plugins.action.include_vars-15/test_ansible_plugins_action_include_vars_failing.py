# Automatically generated by Pynguin.
import ansible.plugins.action.include_vars as module_0

def test_case_0():
    try:
        float_0 = 0.7556978139197067
        bytes_0 = b'2\xda3\x8a\xd5U\xe1\xf0\x9b\xdb\xees\x13\x19\xd3\x9fu\xa4\xf7\xdd'
        str_0 = '"dJk5D}O3\x0c^'
        int_0 = -1666
        action_module_0 = module_0.ActionModule(float_0, bytes_0, bytes_0, str_0, str_0, int_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -423
        str_0 = 'C@N +K:\r{WCm-ri{\x0cQ'
        str_1 = '9:2'
        dict_0 = {str_1: str_0, str_1: int_0}
        str_2 = 'u#P^a-'
        float_0 = -2293.7895
        float_1 = 2497.20989
        float_2 = -317.915
        float_3 = -656.268007
        set_0 = {str_2, int_0, float_3, float_3}
        action_module_0 = module_0.ActionModule(str_2, float_0, float_1, float_2, set_0, set_0)
        str_3 = "LF-%- Y'K3qSe6mhH]"
        action_module_1 = module_0.ActionModule(action_module_0, float_2, str_3, float_0, float_1, action_module_0)
        var_0 = action_module_1.run(str_1, dict_0)
    except BaseException:
        pass