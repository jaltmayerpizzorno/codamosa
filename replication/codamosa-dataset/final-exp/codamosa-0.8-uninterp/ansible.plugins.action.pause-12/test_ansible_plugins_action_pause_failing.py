# Automatically generated by Pynguin.
import ansible.plugins.action.pause as module_0

def test_case_0():
    try:
        int_0 = -1939
        list_0 = [int_0, int_0, int_0]
        float_0 = 801.4
        var_0 = module_0.timeout_handler(list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'host_pinned'
        bool_0 = True
        var_0 = module_0.is_interactive(bool_0)
        dict_0 = {}
        int_0 = None
        str_1 = '([a-z0-9])([A-Z]+)'
        dict_1 = {str_1: dict_0, str_1: str_0, str_0: str_0, str_1: dict_0}
        list_0 = [dict_1, str_1, str_1, str_1]
        list_1 = [int_0, list_0, str_0]
        var_1 = module_0.clear_line(list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2735.0
        list_0 = [float_0, float_0, float_0, float_0]
        bool_0 = False
        int_0 = -3892
        list_1 = [int_0, bool_0, bool_0]
        tuple_0 = ()
        float_1 = 231.0
        action_module_0 = module_0.ActionModule(bool_0, int_0, list_1, tuple_0, tuple_0, float_1)
        var_0 = action_module_0.run(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = None
        set_0 = {bytes_0}
        str_0 = None
        dict_0 = {str_0: bytes_0}
        list_0 = [str_0]
        str_1 = 'FZ'
        str_2 = None
        action_module_0 = module_0.ActionModule(bytes_0, set_0, dict_0, list_0, str_1, str_2)
        int_0 = 2935
        str_3 = '@]=,\\:JHvTE!h&5'
        int_1 = 92
        dict_1 = {str_3: list_0, str_1: int_1, str_0: dict_0}
        dict_2 = {str_1: dict_1}
        var_0 = action_module_0.run(int_0, dict_2)
    except BaseException:
        pass