# Automatically generated by Pynguin.
import ansible.plugins.action.debug as module_0

def test_case_0():
    try:
        float_0 = 573.0
        set_0 = set()
        bool_0 = False
        float_1 = 1000.0
        int_0 = 1183
        action_module_0 = module_0.ActionModule(float_0, set_0, bool_0, float_1, float_1, int_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b''
        list_0 = [bytes_0]
        bool_0 = False
        str_0 = 'flatten'
        str_1 = 'V#fh>EPC'
        dict_0 = {bytes_0: bytes_0, str_1: str_1, str_1: list_0}
        bytes_1 = b'\t\xfa\xe2V^:\xceB'
        complex_0 = None
        tuple_0 = (complex_0,)
        action_module_0 = module_0.ActionModule(str_1, dict_0, bytes_1, bytes_1, tuple_0, list_0)
        str_2 = 'plugins'
        float_0 = -4310.51
        action_module_1 = module_0.ActionModule(action_module_0, dict_0, str_2, float_0, tuple_0, dict_0)
        int_0 = -2636
        str_3 = '\rv\x0cIszUwD'
        str_4 = '7_'
        action_module_2 = module_0.ActionModule(action_module_1, str_1, int_0, bytes_0, str_3, str_4)
        var_0 = action_module_2.run(bool_0, str_0)
    except BaseException:
        pass