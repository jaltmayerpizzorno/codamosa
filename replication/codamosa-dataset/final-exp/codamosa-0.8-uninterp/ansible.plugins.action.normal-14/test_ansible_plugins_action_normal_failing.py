# Automatically generated by Pynguin.
import ansible.plugins.action.normal as module_0

def test_case_0():
    try:
        str_0 = 'not in sudoers'
        str_1 = 'i)}\rO 3bm3B'
        dict_0 = {str_0: str_0, str_1: str_0}
        bool_0 = False
        bytes_0 = b'\xf7\xe1\xe8\xe7\xc5\xf6!\x9dx\xf3\x01`\r:'
        float_0 = 0.5
        action_module_0 = module_0.ActionModule(dict_0, bool_0, bytes_0, float_0, dict_0, bool_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass