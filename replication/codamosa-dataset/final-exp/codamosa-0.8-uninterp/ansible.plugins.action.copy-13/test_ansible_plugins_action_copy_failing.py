# Automatically generated by Pynguin.
import ansible.plugins.action.copy as module_0

def test_case_0():
    try:
        str_0 = ' Given a config key figure out the actual value and report on the origin of the settings '
        list_0 = [str_0]
        str_1 = '9;'
        bool_0 = False
        bytes_0 = b''
        dict_0 = {}
        action_module_0 = module_0.ActionModule(str_0, list_0, str_1, bool_0, bytes_0, dict_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 0.0
        complex_0 = None
        float_1 = -1168.0
        int_0 = 1500
        dict_0 = {float_1: float_0}
        dict_1 = {}
        tuple_0 = (float_0, int_0, dict_0, dict_1)
        bytes_0 = b'zi\xe5\xcd\xfc\xd1\xa6\xc1\x91\xd2\xb4R'
        set_0 = None
        str_0 = 'wFj`clv:T\x0b'
        action_module_0 = module_0.ActionModule(complex_0, float_1, tuple_0, bytes_0, set_0, str_0)
        list_0 = [tuple_0, int_0, dict_0, action_module_0]
        bool_0 = True
        action_module_1 = module_0.ActionModule(action_module_0, str_0, float_1, int_0, list_0, bool_0)
        action_module_2 = module_0.ActionModule(complex_0, action_module_1, complex_0, tuple_0, action_module_0, tuple_0)
        str_1 = 'A_;z~~s\nm~N '
        var_0 = action_module_1.run(str_1, str_1)
    except BaseException:
        pass