# Automatically generated by Pynguin.
import ansible.plugins.action.assemble as module_0

def test_case_0():
    try:
        float_0 = -2577.77
        set_0 = {float_0}
        list_0 = [set_0, set_0, float_0]
        bool_0 = True
        str_0 = 'Skipping key (%s) in group (%s) as it is not a mapping, it is a %s'
        action_module_0 = module_0.ActionModule(set_0, set_0, list_0, bool_0, float_0, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass