# Automatically generated by Pynguin.
import ansible.plugins.action.yum as module_0

def test_case_0():
    try:
        float_0 = -1596.0
        set_0 = {float_0, float_0, float_0, float_0}
        list_0 = [set_0, set_0, float_0, float_0]
        dict_0 = {}
        tuple_0 = (dict_0,)
        str_0 = 'p'
        bool_0 = True
        action_module_0 = module_0.ActionModule(float_0, list_0, set_0, tuple_0, str_0, bool_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass