# Automatically generated by Pynguin.
import ansible.plugins.action.gather_facts as module_0

def test_case_0():
    try:
        bool_0 = False
        list_0 = []
        str_0 = 'log output to this directory'
        float_0 = -30.761868
        bool_1 = False
        action_module_0 = module_0.ActionModule(bool_0, list_0, str_0, float_0, bool_1, float_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass