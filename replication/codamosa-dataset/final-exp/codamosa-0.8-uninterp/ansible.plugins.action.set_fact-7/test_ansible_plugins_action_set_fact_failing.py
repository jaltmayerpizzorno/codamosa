# Automatically generated by Pynguin.
import ansible.plugins.action.set_fact as module_0

def test_case_0():
    try:
        dict_0 = None
        dict_1 = {}
        bytes_0 = b'Q\xed\\FD\xba\x84\xb4\xc4\x1d\x19\xf9\xaa\x7fp\x83'
        str_0 = 'AZ8B+sYZb+'
        list_0 = []
        float_0 = 1181.5
        str_1 = 'qXC'
        tuple_0 = (float_0, str_1)
        bytes_1 = b'\x88:\x86\xe1\xe2{@\xd1\xad\xb08\x0f\xf7\x15'
        action_module_0 = module_0.ActionModule(dict_1, bytes_0, str_0, list_0, tuple_0, bytes_1)
        var_0 = action_module_0.run(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        bytes_0 = b'\xf9'
        str_0 = '--erase'
        dict_1 = {bool_0: bool_0, bool_0: dict_0, bytes_0: str_0}
        tuple_0 = (str_0,)
        int_0 = -1306
        float_0 = -3068.9
        bool_1 = False
        list_0 = []
        int_1 = -1168
        action_module_0 = module_0.ActionModule(int_0, float_0, bool_1, list_0, bool_1, int_1)
        var_0 = action_module_0.run(dict_1, tuple_0)
    except BaseException:
        pass