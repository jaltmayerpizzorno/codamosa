# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        float_0 = -322.053881
        str_0 = "Entering '"
        int_0 = -2372
        dict_0 = {}
        list_0 = [str_0]
        action_module_0 = module_0.ActionModule(float_0, str_0, int_0, dict_0, float_0, list_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        set_0 = {bool_0, bool_0}
        float_0 = -1468.57652
        bytes_0 = b"\x82+'o\x08\xd2\xdd\x1e_"
        set_1 = {bytes_0, float_0}
        bytes_1 = b'\n\x141?\x12.g<`r\xc7'
        bytes_2 = b'\xe1\x83\x9c\x9c\xb8\x04\xc6O'
        str_0 = 'To-scn@s$tz|'
        action_module_0 = module_0.ActionModule(float_0, set_1, bytes_1, bytes_2, str_0, str_0)
        var_0 = action_module_0.run(bool_0, set_0)
    except BaseException:
        pass