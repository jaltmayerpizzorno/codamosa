# Automatically generated by Pynguin.
import ansible.plugins.action.debug as module_0

def test_case_0():
    try:
        action_module_0 = module_0.ActionModule()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'pexpect'
        int_0 = 1216
        set_0 = {str_0, str_0}
        float_0 = 3056.09
        action_module_0 = module_0.ActionModule(str_0, int_0, set_0, set_0, str_0, float_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        float_0 = -1413.0
        str_1 = '?w9+IOZ8?'
        bytes_0 = b'\xb3\xd1+\xa6<\xfe@Vb\xfd\t\xf9\x98D\xb8]\x1d\xba\x9b'
        float_1 = -1935.88803
        list_0 = [bytes_0, float_1, bytes_0]
        bool_0 = False
        tuple_0 = (float_1, list_0, bool_0)
        set_0 = {str_1, bool_0, float_1}
        action_module_0 = module_0.ActionModule(str_1, bytes_0, bytes_0, tuple_0, set_0, tuple_0)
        var_0 = action_module_0.run(str_0, float_0)
    except BaseException:
        pass