# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        str_0 = 'V'
        bytes_0 = b'\xd8H9\xe5\xc3\x8b\x0f\xa2\x96k\xed*\x18\xa6\x13~'
        dict_0 = {}
        action_module_0 = module_0.ActionModule(str_0, bytes_0, str_0, str_0, dict_0, dict_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        int_0 = 32602
        str_0 = 'H]Oe-/!K9xKb.q'
        list_0 = [str_0, int_0]
        int_1 = 30
        str_1 = '?w4F"FU;o=s'
        set_0 = {str_1}
        float_0 = 934.4
        tuple_0 = None
        str_2 = "#Ik=/'X]*Xl't_&ae"
        action_module_0 = module_0.ActionModule(set_0, str_2, float_0, set_0, bool_0, bool_0)
        action_module_1 = module_0.ActionModule(tuple_0, str_1, int_1, list_0, action_module_0, action_module_0)
        str_3 = 'Unknown'
        float_1 = 2.0
        action_module_2 = module_0.ActionModule(bool_0, action_module_1, str_3, float_1, action_module_0, tuple_0)
        action_module_3 = module_0.ActionModule(int_0, str_1, set_0, float_0, action_module_2, tuple_0)
        dict_0 = None
        dict_1 = {dict_0: tuple_0}
        var_0 = action_module_3.run(int_0, dict_1)
    except BaseException:
        pass