# Automatically generated by Pynguin.
import ansible.plugins.callback.tree as module_0

def test_case_0():
    try:
        set_0 = set()
        callback_module_0 = module_0.CallbackModule(set_0)
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
        str_0 = '@0qWsNi4v"bNj\t'
        list_0 = [str_0, str_0, str_0]
        dict_0 = {str_0: str_0, str_0: list_0, str_0: list_0, str_0: list_0}
        bool_0 = False
        callback_module_0 = module_0.CallbackModule(bool_0)
        var_0 = callback_module_0.result_to_tree(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 0.001
        tuple_0 = (float_0,)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 3511.6235
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        callback_module_0 = module_0.CallbackModule()
        float_0 = 1.0
        var_0 = callback_module_0.v2_runner_on_unreachable(float_0)
    except BaseException:
        pass