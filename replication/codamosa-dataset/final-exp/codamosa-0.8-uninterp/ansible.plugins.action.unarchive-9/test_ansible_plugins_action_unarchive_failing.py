# Automatically generated by Pynguin.
import ansible.plugins.action.unarchive as module_0

def test_case_0():
    try:
        bytes_0 = b'Y6j*\xb8\xffNw\x9e'
        int_0 = 128
        dict_0 = {int_0: int_0}
        int_1 = 855
        bool_0 = True
        str_0 = ''
        action_module_0 = module_0.ActionModule(int_0, dict_0, int_1, bool_0, int_1, str_0)
        var_0 = action_module_0.run(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        int_0 = 1412
        dict_0 = {}
        bytes_0 = b'p\xe6}\x80^o\x93g\xfa\x82\xd0\xa3<\x1eh\x7f\x04'
        bool_1 = False
        str_0 = 't:zQ;gu2/X*H*YM\\'
        bytes_1 = b'\xab\xb3\x07X\xbe".\xec\xe7\xd8M\x05\xdd\xd8H\\\x10'
        bool_2 = True
        bool_3 = True
        float_0 = 1093.39609
        action_module_0 = module_0.ActionModule(str_0, bytes_1, str_0, bool_2, bool_3, float_0)
        int_1 = 79
        bytes_2 = b"k'\xd0\xaf\xe0=rK\x90#\xdb3\xedp\x048\xe2\x0b"
        action_module_1 = module_0.ActionModule(dict_0, bytes_0, bool_1, action_module_0, int_1, bytes_2)
        var_0 = action_module_1.run(bool_0, int_0)
    except BaseException:
        pass