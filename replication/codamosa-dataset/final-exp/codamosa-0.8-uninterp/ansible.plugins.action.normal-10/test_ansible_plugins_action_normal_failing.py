# Automatically generated by Pynguin.
import ansible.plugins.action.normal as module_0

def test_case_0():
    try:
        float_0 = -1381.8874
        int_0 = -3305
        bool_0 = True
        dict_0 = {bool_0: int_0}
        bytes_0 = b'R\x1a\xb3'
        str_0 = 'w?EN%,1`]S!'
        action_module_0 = module_0.ActionModule(int_0, bool_0, dict_0, bytes_0, str_0, int_0)
        var_0 = action_module_0.run(float_0)
    except BaseException:
        pass