# Automatically generated by Pynguin.
import ansible.plugins.action.service as module_0

def test_case_0():
    try:
        str_0 = '/proc/[0-9]*/comm'
        float_0 = 1241.96
        int_0 = -1225
        action_module_0 = module_0.ActionModule(float_0, float_0, str_0, float_0, int_0, float_0)
        var_0 = action_module_0.run(str_0)
    except BaseException:
        pass