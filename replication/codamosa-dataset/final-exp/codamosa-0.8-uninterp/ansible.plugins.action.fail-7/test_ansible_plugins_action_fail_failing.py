# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        str_0 = 'Q"WTEIaIs2pHP|+5T'
        bool_0 = False
        tuple_0 = (bool_0,)
        int_0 = -296
        action_module_0 = module_0.ActionModule(str_0, bool_0, tuple_0, int_0, bool_0, bool_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        list_0 = [bool_0]
        bool_1 = False
        set_0 = set()
        float_0 = 0.0001
        tuple_0 = (bool_1, set_0, float_0)
        int_0 = 5
        str_0 = 'X0#5O11'
        float_1 = -2801.20818
        int_1 = None
        int_2 = -888
        str_1 = 'Failed to convert "%s": %s'
        tuple_1 = (int_1, str_0, int_2, str_1)
        set_1 = set()
        list_1 = [set_1, set_1, set_1]
        float_2 = 2.0
        action_module_0 = module_0.ActionModule(str_0, float_1, bool_1, tuple_1, list_1, float_2)
        bool_2 = True
        action_module_1 = module_0.ActionModule(float_0, action_module_0, tuple_1, bool_2, action_module_0, bool_2)
        dict_0 = {float_0: action_module_1, action_module_1: bool_2, bool_2: int_0, bool_2: str_1}
        bytes_0 = b'>\x11\x19\xa4nZ\xa8\xf5Km\x80\x10\x0e8\x1f\x93\x14\xd9'
        action_module_2 = module_0.ActionModule(set_0, int_0, dict_0, str_0, bytes_0, tuple_1)
        action_module_3 = module_0.ActionModule(tuple_0, bool_1, bool_1, tuple_0, bool_1, action_module_2)
        var_0 = action_module_3.run(bool_0, list_0)
    except BaseException:
        pass