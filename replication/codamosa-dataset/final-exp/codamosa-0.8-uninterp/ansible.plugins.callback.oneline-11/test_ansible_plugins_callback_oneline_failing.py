# Automatically generated by Pynguin.
import ansible.plugins.callback.oneline as module_0

def test_case_0():
    try:
        str_0 = 'mtime'
        str_1 = '@ xOqaa.Yuu/:qAu?N"w'
        list_0 = [str_0, str_0, str_1, str_1]
        float_0 = 316.9
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_on_ok(callback_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ischr'
        callback_module_0 = module_0.CallbackModule()
        str_1 = None
        bytes_0 = b'\x0f\x19\x05hB'
        tuple_0 = (str_0, str_1, bytes_0)
        dict_0 = {}
        dict_1 = {tuple_0: str_0, str_1: dict_0, tuple_0: bytes_0, bytes_0: bytes_0}
        bytes_1 = b'\xe0&'
        tuple_1 = (tuple_0, dict_0, dict_1, bytes_1)
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_on_unreachable(tuple_1)
    except BaseException:
        pass

def test_case_3():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        callback_module_2 = module_0.CallbackModule()
        bytes_0 = b'\xc2K\xeaD\xa3G1Y'
        bool_0 = False
        tuple_0 = (bytes_0, bool_0)
        var_0 = callback_module_0.v2_runner_on_skipped(tuple_0)
    except BaseException:
        pass