# Automatically generated by Pynguin.
import ansible.plugins.action.fetch as module_0

def test_case_0():
    try:
        float_0 = -1275.897
        set_0 = set()
        str_0 = ')yc}}XPH\t}rC(qn1Q'
        str_1 = 'FilterModule'
        bytes_0 = b'\xacG\xb9r\xe5\x12\xaa\x8f9\x12d4\xe3\xbc\xf3'
        action_module_0 = module_0.ActionModule(float_0, set_0, str_0, str_1, bytes_0, set_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0}
        list_0 = []
        set_0 = None
        float_0 = 2.0
        bytes_0 = b'\xadS\xe0'
        str_0 = "Unable to decode JSON from response to {0}. Received '{1}'."
        action_module_0 = module_0.ActionModule(dict_0, list_0, set_0, float_0, bytes_0, str_0)
        str_1 = 'authorization'
        str_2 = "Y\tTiTpMyb'*Ym.u9?(U"
        str_3 = 'auth_timeout'
        str_4 = '\rEPMts\\Al*3mlb:i'
        str_5 = 'gnVt$'
        str_6 = '`RQ'
        list_1 = [str_5, str_2, str_4, str_6]
        int_0 = 4057
        action_module_1 = module_0.ActionModule(str_2, str_3, str_4, str_5, list_1, int_0)
        var_0 = action_module_1.run(bool_0, str_1)
    except BaseException:
        pass