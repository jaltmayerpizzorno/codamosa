# Automatically generated by Pynguin.
import ansible.plugins.action.shell as module_0

def test_case_0():
    try:
        bytes_0 = b'M\xe6j\xa2\x9e\xa9\xf3\xa5\xc7\x93d\xc4\x9b\xab'
        bool_0 = False
        int_0 = 90
        bool_1 = False
        str_0 = ''
        action_module_0 = module_0.ActionModule(bytes_0, bytes_0, bool_0, int_0, bool_1, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass