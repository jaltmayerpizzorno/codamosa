# Automatically generated by Pynguin.
import ansible.plugins.action.assert as module_0

def test_case_0():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0]
        int_0 = 24
        bytes_0 = b'\xa33LK5\xc9<&'
        str_0 = '~`@j}HYao%RzBO0G:9f'
        action_module_0 = module_0.ActionModule(bool_0, list_0, int_0, bytes_0, list_0, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        bool_0 = False
        list_0 = [bool_0, bool_0]
        float_0 = -1526.834089
        int_0 = -3487
        set_0 = set()
        action_module_0 = module_0.ActionModule(bool_0, list_0, float_0, list_0, int_0, set_0)
        var_0 = action_module_0.run(tuple_0, tuple_0)
    except BaseException:
        pass