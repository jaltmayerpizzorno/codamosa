# Automatically generated by Pynguin.
import ansible.plugins.action.copy as module_0

def test_case_0():
    try:
        list_0 = None
        bytes_0 = b'\xef\xc5?\xab'
        tuple_0 = ()
        set_0 = {tuple_0}
        str_0 = 'Kt?'
        action_module_0 = module_0.ActionModule(bytes_0, tuple_0, tuple_0, set_0, str_0, tuple_0)
        var_0 = action_module_0.run(list_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\\n\\W+(.*)'
        int_0 = -2402
        tuple_0 = ()
        bool_0 = False
        float_0 = 3634.05279
        set_0 = set()
        list_0 = [str_0]
        str_1 = '%s-'
        float_1 = -4416.152
        action_module_0 = module_0.ActionModule(tuple_0, set_0, list_0, str_1, float_1, bool_0)
        var_0 = action_module_0.run(float_0, int_0)
    except BaseException:
        pass