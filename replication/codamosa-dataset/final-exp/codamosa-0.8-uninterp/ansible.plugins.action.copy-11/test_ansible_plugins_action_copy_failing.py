# Automatically generated by Pynguin.
import ansible.plugins.action.copy as module_0

def test_case_0():
    try:
        str_0 = 'X\rD4V"jO'
        bytes_0 = b'\x92\xeb\xabi\x15\x05\xdfd+\xd8 \xb6\x80a\xd6\t\xa2'
        int_0 = 20
        tuple_0 = (int_0,)
        action_module_0 = module_0.ActionModule(str_0, str_0, bytes_0, int_0, tuple_0, bytes_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 375
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
        list_0 = []
        str_0 = '%s -r %s'
        bool_0 = True
        str_1 = 'Invalid "hosts" entry for "%s" group, requires a dict, found "%s" instead.'
        bytes_0 = b'\xd9Yd\xb5\xcb'
        str_2 = '0p_LS?q`ONSL'
        str_3 = None
        bytes_1 = b'\xf4AV\x9e0;E]\xf2\xb2\xfd{\xfb\x1c\xb6\x84\x14]y\xa8'
        action_module_0 = module_0.ActionModule(str_2, str_3, dict_0, list_0, bytes_1, dict_0)
        action_module_1 = module_0.ActionModule(list_0, str_0, bool_0, str_1, bytes_0, bool_0)
        action_module_2 = module_0.ActionModule(dict_0, action_module_1, action_module_1, bool_0, dict_0, bool_0)
        str_4 = '0`N)'
        float_0 = -2091.8
        action_module_3 = module_0.ActionModule(list_0, str_4, bytes_1, str_1, bool_0, float_0)
        var_0 = action_module_3.run(int_0, int_0)
    except BaseException:
        pass