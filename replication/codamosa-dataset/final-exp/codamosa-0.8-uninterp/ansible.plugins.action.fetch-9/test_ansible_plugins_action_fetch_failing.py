# Automatically generated by Pynguin.
import ansible.plugins.action.fetch as module_0

def test_case_0():
    try:
        int_0 = -2606
        float_0 = 0.1
        bytes_0 = b'\xe4\x8e'
        dict_0 = {float_0: float_0, float_0: bytes_0}
        bool_0 = False
        str_0 = ''
        float_1 = -3860.1
        str_1 = '+'
        action_module_0 = module_0.ActionModule(dict_0, bool_0, bool_0, str_0, float_1, str_1)
        var_0 = action_module_0.run(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'G;>uAVf?\x0b@#4-t1a\t*X'
        set_0 = set()
        dict_0 = {}
        float_0 = 0.2
        action_module_0 = module_0.ActionModule(str_0, set_0, dict_0, dict_0, dict_0, float_0)
        str_1 = 'a~Jq0!'
        var_0 = action_module_0.run(str_1, set_0)
    except BaseException:
        pass