# Automatically generated by Pynguin.
import ansible.plugins.callback.tree as module_0

def test_case_0():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.set_options()
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
        callback_module_0 = None
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.result_to_tree(callback_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xfc\xa3w\xaa\xdc\x8a-\xf3\xaf\xee\x85)\xfe\x1d/\x02\x05'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$y]y.'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_unreachable(str_0)
    except BaseException:
        pass