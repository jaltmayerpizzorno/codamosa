# Automatically generated by Pynguin.
import ansible.plugins.action.gather_facts as module_0

def test_case_0():
    try:
        str_0 = 'It['
        set_0 = {str_0}
        bool_0 = False
        bytes_0 = b'\\\xd1\x11\x03\xee\x80\xce=\x8dQ\xc4\x94\x11Ef\x88\xdc6.'
        set_1 = set()
        str_1 = 'l@`\x0cwIF>N'
        action_module_0 = module_0.ActionModule(str_0, set_0, bool_0, bytes_0, set_1, str_1)
        var_0 = action_module_0.run()
    except BaseException:
        pass