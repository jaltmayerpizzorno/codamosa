# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        str_0 = 'g`\x0baJWF4w'
        str_1 = '|Vpbm'
        list_0 = [str_1, str_1, str_1]
        bool_0 = False
        str_2 = "S*jL~+x'<z"
        dict_0 = {str_0: bool_0}
        action_module_0 = module_0.ActionModule(str_0, str_1, list_0, bool_0, str_2, dict_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '3^CGh\x0cz]g"3!:'
        set_0 = {str_0}
        tuple_0 = None
        tuple_1 = (tuple_0,)
        str_1 = 'qPt9.FkG}UItnC?-;X{_'
        str_2 = '52u\r|2[l\x0b'
        str_3 = 'S.'
        str_4 = 'codename'
        int_0 = -1224
        float_0 = -1036.0
        bool_0 = True
        dict_0 = {str_3: str_3, str_3: str_3, str_1: float_0}
        action_module_0 = module_0.ActionModule(str_3, str_4, int_0, float_0, bool_0, dict_0)
        int_1 = 64
        str_5 = '>6~WX`'
        action_module_1 = module_0.ActionModule(str_1, str_2, action_module_0, int_1, str_3, str_5)
        var_0 = action_module_1.run(set_0, tuple_1)
    except BaseException:
        pass