# Automatically generated by Pynguin.
import ansible.plugins.action.assemble as module_0

def test_case_0():
    try:
        action_module_0 = module_0.ActionModule()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        float_0 = -843.35
        set_0 = {float_0, bool_0}
        int_0 = -3878
        action_module_0 = module_0.ActionModule(bool_0, set_0, bool_0, float_0, int_0, set_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass