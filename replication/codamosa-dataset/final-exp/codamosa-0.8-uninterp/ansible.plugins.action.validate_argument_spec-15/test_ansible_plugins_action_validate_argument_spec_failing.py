# Automatically generated by Pynguin.
import ansible.plugins.action.validate_argument_spec as module_0

def test_case_0():
    try:
        int_0 = None
        dict_0 = {}
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0, tuple_0]
        dict_1 = {}
        int_1 = 300
        bytes_0 = b'\xe4\xb8\xbcq\x95)\x9c\x037`\xa3\x8e~'
        action_module_0 = module_0.ActionModule(tuple_0, list_0, dict_1, int_1, bytes_0, list_0)
        var_0 = action_module_0.get_args_from_task_vars(int_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xe7Zk*\xbe\x0b\xa3x\xae\xb3\xbbP\xb0\xbd{8\t\x9b'
        bool_0 = False
        list_0 = [bool_0, bool_0]
        set_0 = {bool_0, bytes_0, bytes_0}
        str_0 = 'A[cJU?\\"(DuGCi[?KTNq'
        str_1 = 'R-)u\x0btgD8Gn=23x:<\tiz'
        dict_0 = {}
        bool_1 = True
        action_module_0 = module_0.ActionModule(list_0, set_0, str_0, str_1, dict_0, bool_1)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '`b#x\x0cX<?VY=/!w'
        bool_0 = True
        float_0 = 60.0
        str_1 = '2Zsw_:dap"0_!'
        str_2 = ',%!KB'
        list_0 = [float_0, str_0, str_2]
        action_module_0 = module_0.ActionModule(str_0, bool_0, float_0, str_1, str_2, list_0)
        set_0 = set()
        int_0 = -1257
        bytes_0 = b'\x1c\xcc\xbf\xca<\x9d\xb7\xa7\xf2\xdf\x90\xdc'
        str_3 = '1{H|2HHz{dqr0X9\x0c'
        action_module_1 = module_0.ActionModule(action_module_0, set_0, int_0, bytes_0, str_3, action_module_0)
        var_0 = action_module_1.run(set_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'v'
        set_0 = {str_0, str_0}
        int_0 = 127
        set_1 = set()
        float_0 = -618.978
        action_module_0 = module_0.ActionModule(str_0, set_0, set_0, int_0, str_0, set_1)
        str_1 = '}<~S<j2u,!5a#qT'
        dict_0 = {int_0: action_module_0, str_0: set_0, str_1: int_0}
        list_0 = [float_0, set_1]
        dict_1 = {}
        action_module_1 = module_0.ActionModule(dict_1, str_1, dict_1, set_0, set_1, int_0)
        var_0 = action_module_1.get_args_from_task_vars(dict_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '?82M;|\x0b,|Ec\r8%1ezi`'
        set_0 = {str_0, str_0}
        int_0 = 221
        str_1 = 'xwt'
        action_module_0 = module_0.ActionModule(str_0, set_0, set_0, int_0, str_1, set_0)
        dict_0 = {int_0: action_module_0, str_0: set_0, str_0: int_0}
        action_module_1 = module_0.ActionModule(dict_0, str_1, dict_0, set_0, set_0, int_0)
        str_2 = ''
        dict_1 = {str_2: str_2, str_2: str_2}
        str_3 = '?,t6V<'
        var_0 = action_module_1.get_args_from_task_vars(dict_1, str_3)
    except BaseException:
        pass