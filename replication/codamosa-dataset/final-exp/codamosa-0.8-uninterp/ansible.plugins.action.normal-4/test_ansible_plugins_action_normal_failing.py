# Automatically generated by Pynguin.
import ansible.plugins.action.normal as module_0

def test_case_0():
    try:
        str_0 = ''
        float_0 = -3220.8089
        bytes_0 = b'\x0e'
        set_0 = {bytes_0}
        tuple_0 = (set_0,)
        dict_0 = {}
        float_1 = -426.0
        float_2 = -2282.0
        action_module_0 = module_0.ActionModule(dict_0, float_1, dict_0, float_2, tuple_0, set_0)
        action_module_1 = module_0.ActionModule(str_0, float_0, bytes_0, set_0, tuple_0, action_module_0)
        var_0 = action_module_1.run()
    except BaseException:
        pass