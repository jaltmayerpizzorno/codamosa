# Automatically generated by Pynguin.
import ansible.plugins.action.yum as module_0

def test_case_0():
    try:
        float_0 = -4420.7
        bool_0 = True
        set_0 = {float_0, float_0, float_0, float_0}
        str_0 = 'The last named variable will be "%s". The rest will not have names.'
        bytes_0 = b''
        int_0 = 588
        tuple_0 = ()
        action_module_0 = module_0.ActionModule(set_0, str_0, bytes_0, str_0, int_0, tuple_0)
        var_0 = action_module_0.run(bool_0)
    except BaseException:
        pass