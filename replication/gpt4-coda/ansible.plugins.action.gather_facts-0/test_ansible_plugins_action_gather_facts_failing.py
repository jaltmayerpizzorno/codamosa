# Automatically generated by Pynguin.
import ansible.plugins.action.gather_facts as module_0

def test_case_0():
    try:
        int_0 = 118
        float_0 = 0.2
        list_0 = [int_0, int_0, float_0]
        bytes_0 = None
        tuple_0 = (bytes_0,)
        tuple_1 = (int_0, float_0, tuple_0)
        int_1 = 697
        action_module_0 = module_0.ActionModule(int_0, list_0, tuple_1, tuple_0, int_1, tuple_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass