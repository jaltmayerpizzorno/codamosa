# Automatically generated by Pynguin.
import ansible.plugins.action.set_stats as module_0

def test_case_0():
    try:
        list_0 = []
        float_0 = -2701.74084
        float_1 = 3513.82002
        int_0 = 5985
        bool_0 = True
        action_module_0 = module_0.ActionModule(list_0, float_0, float_1, int_0, bool_0, bool_0)
        int_1 = 3177
        str_0 = 'N('
        str_1 = ',nwwW\x0bB<Q~)8O;[xnA'
        set_0 = {float_1}
        float_2 = -1934.0
        action_module_1 = module_0.ActionModule(action_module_0, int_1, str_0, str_1, set_0, float_2)
        var_0 = action_module_1.run()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 100.0
        list_0 = None
        dict_0 = {list_0: list_0}
        set_0 = None
        tuple_0 = (list_0, dict_0, set_0)
        tuple_1 = (tuple_0,)
        str_0 = 'MjbE{\x0b5B` '
        set_1 = {str_0, str_0}
        list_1 = []
        bytes_0 = b'\xb6g\x07'
        int_0 = -489
        str_1 = 'XOoQaz1\t8Y\rgW.<'
        dict_1 = {str_1: bytes_0, bytes_0: int_0, str_1: str_0, bytes_0: list_1}
        float_1 = 1388.5
        bool_0 = True
        tuple_2 = (str_1, dict_1, float_1, bool_0)
        int_1 = 2896
        int_2 = 577
        action_module_0 = module_0.ActionModule(int_0, tuple_2, str_0, int_1, float_1, int_2)
        str_2 = 'qTchO#'
        action_module_1 = module_0.ActionModule(set_1, list_1, bytes_0, action_module_0, str_2, list_1)
        int_3 = -3861
        bytes_1 = b'\x0e\x08\xbd\xd7\xc6\xd7\x8c\x1a-\xb0'
        float_2 = -2236.0
        action_module_2 = module_0.ActionModule(action_module_1, int_3, bytes_1, dict_1, action_module_1, float_2)
        var_0 = action_module_2.run(float_0, tuple_1)
    except BaseException:
        pass