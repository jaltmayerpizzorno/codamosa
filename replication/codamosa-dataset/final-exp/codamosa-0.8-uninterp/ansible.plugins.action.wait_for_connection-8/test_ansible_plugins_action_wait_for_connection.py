# Automatically generated by Pynguin.
import ansible.plugins.action.wait_for_connection as module_0

def test_case_0():
    timed_out_exception_0 = module_0.TimedOutException()

def test_case_1():
    str_0 = 'C@A%'
    bool_0 = True
    dict_0 = None
    list_0 = [dict_0, str_0, str_0, str_0]
    int_0 = 186
    list_1 = [bool_0]
    action_module_0 = module_0.ActionModule(dict_0, list_0, int_0, dict_0, str_0, list_1)
    bytes_0 = b'\xb5\x8b\xfa'
    set_0 = {bytes_0, bytes_0, bytes_0}
    tuple_0 = None
    int_1 = 1606
    bytes_1 = b'\xf5\x14\xb8\x0c\x94\x17{\xbf'
    var_0 = action_module_0.do_until_success_or_timeout(tuple_0, int_1, set_0, bytes_1)
    int_2 = -913
    bool_1 = True
    dict_1 = {str_0: str_0, str_0: int_2, str_0: str_0}
    bool_2 = True
    action_module_1 = module_0.ActionModule(str_0, dict_1, bool_2, action_module_0, set_0, bool_2)
    tuple_1 = (list_0,)
    tuple_2 = (action_module_1, tuple_1)
    var_1 = action_module_0.do_until_success_or_timeout(list_1, tuple_2, dict_0, bool_1)