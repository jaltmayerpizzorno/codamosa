# Automatically generated by Pynguin.
import ansible.plugins.action.debug as module_0

def test_case_0():
    try:
        action_module_0 = None
        tuple_0 = (action_module_0,)
        bytes_0 = b'B\xa6\xbcm\xb6]\xa7\x8f<%\x8d7K'
        bool_0 = True
        set_0 = {tuple_0}
        action_module_1 = module_0.ActionModule(tuple_0, action_module_0, bytes_0, bool_0, set_0, set_0)
        var_0 = action_module_1.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        str_1 = '2J]h5(,8Ca\x0c7WMdDe`v#'
        bytes_0 = b''
        bool_0 = False
        list_0 = [str_1]
        int_0 = None
        str_2 = '"@y[WQ8yM<t:Sj>Vq(f>'
        dict_0 = {str_2: list_0}
        str_3 = 'l2Aa'
        action_module_0 = module_0.ActionModule(bool_0, list_0, int_0, dict_0, str_3, str_0)
        float_0 = 1807.99605
        action_module_1 = module_0.ActionModule(str_1, bytes_0, bool_0, action_module_0, dict_0, float_0)
        set_0 = {bytes_0, bytes_0}
        str_4 = 'omit'
        str_5 = 'z\r.\x0cTdn<{<p{ei!'
        str_6 = '0;e_'
        int_1 = 8
        set_1 = {str_0, str_6}
        dict_1 = {str_6: set_1}
        dict_2 = {str_0: dict_1, int_1: dict_1, str_4: str_0, str_0: str_0}
        action_module_2 = module_0.ActionModule(str_4, str_5, str_6, int_1, set_1, dict_2)
        var_0 = action_module_2.run(action_module_1, set_0)
    except BaseException:
        pass