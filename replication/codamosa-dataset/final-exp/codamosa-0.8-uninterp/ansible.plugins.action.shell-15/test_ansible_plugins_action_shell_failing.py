# Automatically generated by Pynguin.
import ansible.plugins.action.shell as module_0

def test_case_0():
    try:
        float_0 = -326.82
        dict_0 = {float_0: float_0}
        str_0 = 'stdout chunk (state=%s):\n>>>%s<<<\n'
        str_1 = "a5\r''Q-H^FXPb;el!.Wz"
        int_0 = 4
        action_module_0 = module_0.ActionModule(float_0, dict_0, str_0, float_0, str_1, int_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass