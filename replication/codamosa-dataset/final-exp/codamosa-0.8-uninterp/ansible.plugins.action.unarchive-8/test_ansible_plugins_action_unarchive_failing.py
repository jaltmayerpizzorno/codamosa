# Automatically generated by Pynguin.
import ansible.plugins.action.unarchive as module_0

def test_case_0():
    try:
        float_0 = 560.72
        str_0 = 'HD\rgcC3>1K'
        bytes_0 = b'\xe5'
        bool_0 = True
        action_module_0 = module_0.ActionModule(float_0, str_0, float_0, bytes_0, bool_0, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xa2\x1b\xc7\\t{\x7f\\\xf6\xe2|\xba\x8e'
        list_0 = [bytes_0]
        float_0 = -1166.0
        bool_0 = True
        int_0 = 3367
        bytes_1 = b'\x9b\xff/\x87.9\x8d\x01'
        dict_0 = {}
        action_module_0 = module_0.ActionModule(list_0, float_0, bool_0, int_0, bytes_1, dict_0)
        tuple_0 = ()
        tuple_1 = ()
        set_0 = {tuple_1}
        float_1 = 2026.0
        action_module_1 = module_0.ActionModule(tuple_1, set_0, tuple_1, float_1, set_0, float_1)
        var_0 = action_module_1.run(action_module_0, tuple_0)
    except BaseException:
        pass