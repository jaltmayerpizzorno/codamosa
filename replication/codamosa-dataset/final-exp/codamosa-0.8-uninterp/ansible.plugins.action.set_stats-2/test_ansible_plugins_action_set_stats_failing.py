# Automatically generated by Pynguin.
import ansible.plugins.action.set_stats as module_0

def test_case_0():
    try:
        float_0 = 1354.998
        set_0 = set()
        int_0 = 2262
        bool_0 = True
        int_1 = -2096
        str_0 = '(oR'
        str_1 = '/etc/ssl/certs'
        list_0 = None
        dict_0 = None
        action_module_0 = module_0.ActionModule(bool_0, int_1, str_0, str_1, list_0, dict_0)
        tuple_0 = (bool_0, action_module_0)
        action_module_1 = module_0.ActionModule(set_0, int_0, tuple_0, bool_0, action_module_0, list_0)
        var_0 = action_module_1.run(float_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        float_0 = -789.42477
        bytes_0 = b'eL*\xfaIio\xa0'
        float_1 = 4134.086
        str_0 = 'G%2'
        action_module_0 = module_0.ActionModule(set_0, float_0, bytes_0, float_1, set_0, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass