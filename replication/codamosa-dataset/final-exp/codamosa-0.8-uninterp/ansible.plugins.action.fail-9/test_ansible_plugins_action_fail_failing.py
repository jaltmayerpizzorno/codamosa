# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        bytes_0 = b'e\xa2\xdb'
        float_0 = -3010.7
        bool_0 = False
        str_0 = '-B'
        str_1 = 'Removed group %s from inventory'
        int_0 = -4
        bool_1 = True
        action_module_0 = module_0.ActionModule(float_0, bool_0, str_0, str_1, int_0, bool_1)
        var_0 = action_module_0.run(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 4090
        int_1 = None
        set_0 = set()
        list_0 = [set_0, int_0]
        str_0 = 'N)tvOO0'
        int_2 = -2209
        dict_0 = {int_0: int_1}
        action_module_0 = module_0.ActionModule(str_0, int_2, int_0, dict_0, dict_0, dict_0)
        var_0 = action_module_0.run(set_0, list_0)
    except BaseException:
        pass