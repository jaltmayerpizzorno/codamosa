# Automatically generated by Pynguin.
import ansible.plugins.action.fetch as module_0

def test_case_0():
    try:
        int_0 = 604800
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        bytes_0 = b'\xf1\xda\x8c"\xfd\xc5Y\x10:;\xc8\x1d\x9a\xb9'
        bytes_1 = b'h\x01\xe6\x07\xc0\xaf\xeb;\t\x01'
        bool_0 = True
        action_module_0 = module_0.ActionModule(int_0, dict_0, dict_0, bytes_0, bytes_1, bool_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 69
        dict_0 = None
        tuple_0 = (int_0, dict_0)
        str_0 = '\\(awqPTCdI%qps_Y'
        set_0 = {str_0, str_0}
        str_1 = 'i5\\K\x0b~d{y4e~~^f#[t'
        list_0 = [dict_0]
        float_0 = 3688.913
        dict_1 = {str_0: int_0, str_0: dict_0, str_1: tuple_0, dict_0: str_1}
        float_1 = -307.2
        action_module_0 = module_0.ActionModule(tuple_0, dict_1, float_1, set_0, str_0, set_0)
        var_0 = action_module_0.run(list_0, float_0)
    except BaseException:
        pass