# Automatically generated by Pynguin.
import ansible.plugins.action.gather_facts as module_0

def test_case_0():
    try:
        str_0 = 'PfHk\t=2SS6XS'
        int_0 = 2121
        dict_0 = {}
        int_1 = 3688
        list_0 = [dict_0, int_1, int_0, dict_0]
        float_0 = -518.0
        set_0 = {int_0, int_1, float_0}
        action_module_0 = module_0.ActionModule(str_0, int_0, dict_0, list_0, set_0, str_0)
        bytes_0 = b'\r\xc6\xf7\xd8\xcd\xc7!p.\xa6 \xca\xc2\xc3\x06\xe3'
        bool_0 = False
        action_module_1 = module_0.ActionModule(action_module_0, bytes_0, str_0, set_0, bool_0, int_1)
        var_0 = action_module_1.run()
    except BaseException:
        pass