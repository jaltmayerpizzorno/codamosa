# Automatically generated by Pynguin.
import ansible.plugins.action.set_fact as module_0

def test_case_0():
    try:
        tuple_0 = None
        int_0 = None
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        str_0 = 'aSLow'
        bool_0 = False
        float_0 = 0.1
        action_module_0 = module_0.ActionModule(dict_0, str_0, bool_0, dict_0, float_0, float_0)
        var_0 = action_module_0.run(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 0.1
        str_0 = 'initctl'
        int_0 = 251
        str_1 = '@WUz`(&udq!'
        dict_0 = {float_0: float_0, str_1: str_1, float_0: int_0}
        bool_0 = False
        tuple_0 = ()
        str_2 = 'D[G'
        action_module_0 = module_0.ActionModule(dict_0, bool_0, tuple_0, dict_0, tuple_0, str_2)
        int_1 = 1083
        set_0 = {float_0, float_0, int_1}
        int_2 = 647
        action_module_1 = module_0.ActionModule(action_module_0, str_1, set_0, int_2, bool_0, int_0)
        action_module_2 = module_0.ActionModule(int_0, action_module_1, action_module_0, tuple_0, float_0, dict_0)
        var_0 = action_module_2.run(str_0, float_0)
    except BaseException:
        pass