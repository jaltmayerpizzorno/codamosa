# Automatically generated by Pynguin.
import ansible.plugins.action.set_fact as module_0

def test_case_0():
    try:
        bytes_0 = b'\x93]\xc2IYD'
        int_0 = None
        tuple_0 = (int_0,)
        float_0 = 4643.4767
        bytes_1 = b'\t_N\xde\x8av\xec\xa3d\xaf;`4\xf6|\x82is\xee\xe9'
        list_0 = [bytes_0]
        action_module_0 = module_0.ActionModule(bytes_0, tuple_0, float_0, bytes_1, list_0, int_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ' '
        bool_0 = True
        str_1 = "R'KUy@ fbx4tqyH"
        str_2 = 'bn",OVK`JfW][F~\''
        list_0 = [str_1, str_1, str_2]
        bool_1 = False
        dict_0 = {}
        bool_2 = True
        float_0 = -3347.542333
        action_module_0 = module_0.ActionModule(list_0, bool_1, dict_0, bool_2, dict_0, float_0)
        var_0 = action_module_0.run(str_0, bool_0)
    except BaseException:
        pass