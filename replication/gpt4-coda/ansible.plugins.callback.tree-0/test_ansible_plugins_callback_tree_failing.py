# Automatically generated by Pynguin.
import ansible.plugins.callback.tree as module_0

def test_case_0():
    try:
        bytes_0 = b'\x9e\xa1'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.set_options(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.write_tree_file(callback_module_0, callback_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -1851
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'S9\r>|)'
        bytes_0 = b'\x86\x1a'
        dict_0 = {str_0: bytes_0}
        tuple_0 = (str_0, bytes_0, dict_0, str_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        str_0 = '\x0b~RNZ\n@<uzg7*CL\x0bO'
        var_0 = callback_module_1.v2_runner_on_unreachable(str_0)
    except BaseException:
        pass