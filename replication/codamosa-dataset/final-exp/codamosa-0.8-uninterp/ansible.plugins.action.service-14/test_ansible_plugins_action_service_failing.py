# Automatically generated by Pynguin.
import ansible.plugins.action.service as module_0

def test_case_0():
    try:
        bool_0 = True
        tuple_0 = ()
        tuple_1 = (tuple_0,)
        bool_1 = True
        str_0 = 'author'
        dict_0 = {bool_1: tuple_1, tuple_1: bool_1, str_0: bool_1, tuple_1: tuple_1}
        float_0 = 2447.684495
        bytes_0 = b'\x07)\xc2\x14\x01\xc7>\x93`\x14\x14\x04'
        action_module_0 = module_0.ActionModule(tuple_1, dict_0, float_0, bytes_0, float_0, dict_0)
        set_0 = set()
        str_1 = '*thH\x0c5h,6)DkLI\r'
        action_module_1 = module_0.ActionModule(bool_0, action_module_0, set_0, set_0, str_0, str_1)
        var_0 = action_module_1.run()
    except BaseException:
        pass