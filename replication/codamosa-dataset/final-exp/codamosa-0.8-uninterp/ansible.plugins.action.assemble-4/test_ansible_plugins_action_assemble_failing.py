# Automatically generated by Pynguin.
import ansible.plugins.action.assemble as module_0

def test_case_0():
    try:
        int_0 = 271
        tuple_0 = (int_0,)
        str_0 = 'M,^N.'
        str_1 = 'x{;c"_9{\x0bVg+'
        bool_0 = False
        action_module_0 = module_0.ActionModule(tuple_0, int_0, str_0, str_1, str_0, bool_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass