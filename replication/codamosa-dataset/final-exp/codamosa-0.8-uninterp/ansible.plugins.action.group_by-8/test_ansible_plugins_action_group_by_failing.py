# Automatically generated by Pynguin.
import ansible.plugins.action.group_by as module_0

def test_case_0():
    try:
        int_0 = None
        float_0 = -182.0
        str_0 = 'http://schemas.microsoft.com/wbem/wsman/1/windows/shell/cmd'
        bytes_0 = b'\xb7}gH\xd7\xee\xf9\x99\xd0R+\r\xaf\xe3'
        str_1 = '\nU/3Rg]h=PH_'
        str_2 = 'K\\>&zLG(aLlw&OI;'
        tuple_0 = ()
        tuple_1 = (str_2, tuple_0)
        bool_0 = False
        str_3 = 'a@'
        action_module_0 = module_0.ActionModule(str_0, bytes_0, str_1, tuple_1, bool_0, str_3)
        var_0 = action_module_0.run(int_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'O.A$|\r_c7pDZaGdd6xd:'
        str_1 = 'minimal'
        bool_0 = True
        set_0 = {str_1}
        float_0 = -1545.39649
        int_0 = 33188
        str_2 = 'c^\x0bfv]8}\x0c>B%\x0cc%fh@:@'
        dict_0 = {}
        action_module_0 = module_0.ActionModule(float_0, str_1, int_0, float_0, str_2, dict_0)
        bytes_0 = b'\x12<J\xa8\x0c\xf3'
        tuple_0 = (bool_0, dict_0, str_2, bytes_0)
        action_module_1 = module_0.ActionModule(str_1, bool_0, set_0, action_module_0, tuple_0, float_0)
        var_0 = action_module_1.run(str_0)
    except BaseException:
        pass