# Automatically generated by Pynguin.
import ansible.plugins.action.copy as module_0

def test_case_0():
    try:
        list_0 = []
        bytes_0 = b''
        float_0 = -1148.3
        dict_0 = {bytes_0: float_0}
        float_1 = 512.0
        set_0 = {bytes_0, float_1}
        bool_0 = False
        action_module_0 = module_0.ActionModule(bytes_0, float_0, dict_0, set_0, bool_0, dict_0)
        var_0 = action_module_0.run(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        float_0 = -107.3
        set_0 = set()
        str_0 = '5o[3~"z.C7SAQIAOJ5{'
        str_1 = 'S?D|W@emMj\x0b&3\tW'
        tuple_0 = (str_1,)
        action_module_0 = module_0.ActionModule(set_0, bool_0, str_0, tuple_0, tuple_0, str_1)
        set_1 = {float_0, bool_0, float_0, float_0}
        str_2 = '*uIBdfii`$`n1z;X'
        str_3 = '6K0{v1C\\V@hh'
        str_4 = '}lpf/?*cwsw,hs]EyF0'
        int_0 = 604800
        action_module_1 = module_0.ActionModule(set_1, str_2, str_3, str_4, set_1, int_0)
        var_0 = action_module_1.run(action_module_0, set_0)
    except BaseException:
        pass