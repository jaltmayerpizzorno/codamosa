# Automatically generated by Pynguin.
import ansible.plugins.action.service as module_0

def test_case_0():
    try:
        action_module_0 = module_0.ActionModule()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -640
        dict_0 = {int_0: int_0, int_0: int_0}
        str_0 = 'HP vPar'
        tuple_0 = ()
        float_0 = -435.8
        str_1 = 'Nboc|/z$Xj8Lggf'
        bytes_0 = b'\xab0\x8b&\x98\x8e\x16b\xc0\x98qe'
        action_module_0 = module_0.ActionModule(dict_0, str_0, tuple_0, float_0, str_1, bytes_0)
        action_module_1 = module_0.ActionModule(int_0, int_0, int_0, dict_0, action_module_0, int_0)
        var_0 = action_module_1.run()
    except BaseException:
        pass