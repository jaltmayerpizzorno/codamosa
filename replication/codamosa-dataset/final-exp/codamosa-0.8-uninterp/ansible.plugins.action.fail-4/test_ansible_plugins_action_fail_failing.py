# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        float_0 = 100.0
        list_0 = [float_0, float_0]
        str_0 = ",O'5)&.Y6n!8"
        float_1 = 0.0
        set_0 = {float_1, str_0, float_1}
        bytes_0 = b'M\x14'
        float_2 = 571.374177
        list_1 = []
        action_module_0 = module_0.ActionModule(str_0, float_1, set_0, bytes_0, float_2, list_1)
        var_0 = action_module_0.run(float_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        set_0 = {bool_0}
        str_0 = 'cei'
        tuple_0 = (str_0,)
        int_0 = -1376
        set_1 = {tuple_0, int_0, tuple_0, str_0}
        float_0 = 2.0
        int_1 = 125
        str_1 = '6JD'
        action_module_0 = module_0.ActionModule(set_1, float_0, int_1, str_1, set_1, tuple_0)
        var_0 = action_module_0.run(set_0)
    except BaseException:
        pass