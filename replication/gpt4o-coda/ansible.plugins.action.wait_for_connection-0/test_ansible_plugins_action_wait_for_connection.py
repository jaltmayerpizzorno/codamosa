# Automatically generated by Pynguin.
import ansible.plugins.action.wait_for_connection as module_0
import builtins as module_1

def test_case_0():
    timed_out_exception_0 = module_0.TimedOutException()

def test_case_1():
    tuple_0 = ()
    bool_0 = False
    list_0 = [tuple_0]
    float_0 = None
    action_module_0 = module_0.ActionModule(bool_0, tuple_0, list_0, bool_0, tuple_0, float_0)
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
    str_0 = '}2$7_Q-5F'
    dict_1 = {str_0: str_0, str_0: str_0}
    str_1 = 'b;jf+kuN%5f}3lg'
    list_1 = [dict_0, str_1, dict_0]
    timed_out_exception_0 = module_0.TimedOutException(*list_1)
    str_2 = '\ry/V'
    float_1 = 1359.0
    bool_1 = None
    action_module_1 = module_0.ActionModule(timed_out_exception_0, dict_1, dict_1, str_2, float_1, bool_1)
    bool_2 = False
    list_2 = []
    dict_2 = module_1.dict()
    action_module_2 = module_0.ActionModule(tuple_0, dict_0, bool_2, float_1, list_2, dict_2)
    timed_out_exception_1 = None
    int_0 = 2696
    var_0 = action_module_1.do_until_success_or_timeout(timed_out_exception_1, int_0, bool_2, str_0)
    tuple_1 = (action_module_2,)
    var_1 = action_module_2.run(dict_1)
    set_0 = {dict_0, tuple_1, float_0, dict_0}
    int_1 = -2439
    tuple_2 = (set_0, int_1)
    action_module_3 = module_0.ActionModule(tuple_1, set_0, list_1, tuple_2, dict_0, dict_2)
    timed_out_exception_2 = None
    var_2 = action_module_2.do_until_success_or_timeout(list_2, dict_0, dict_0, timed_out_exception_2, list_1)
    var_3 = action_module_3.run()