# Automatically generated by Pynguin.
import ansible.plugins.action.include_vars as module_0

def test_case_0():
    try:
        bool_0 = False
        str_0 = "Vim+q#Yb,/E'"
        bytes_0 = b'<\x80\x95\x1e'
        float_0 = 2609.38
        int_0 = 1085
        bytes_1 = b'\x98}\n\x84\x94\x04'
        bool_1 = False
        str_1 = 'repo_gpgcheck'
        action_module_0 = module_0.ActionModule(bytes_0, float_0, int_0, bytes_1, bool_1, str_1)
        var_0 = action_module_0.run(bool_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 307
        bool_0 = True
        dict_0 = {bool_0: bool_0, int_0: int_0}
        bytes_0 = b'rpt\xd1MG\xa2\xbb\xeb\x0b\xfe<\xa1\xb7_\xe1\r.\xdb'
        float_0 = 812.06531
        set_0 = {float_0}
        action_module_0 = module_0.ActionModule(bool_0, dict_0, bytes_0, float_0, set_0, int_0)
        list_0 = [action_module_0]
        bytes_1 = b'\x98\xdd\xc7\'Q\xc3\xa0\x00\x01K6"N\x99\x7f'
        action_module_1 = module_0.ActionModule(int_0, action_module_0, list_0, list_0, bool_0, bytes_1)
        var_0 = action_module_1.run()
    except BaseException:
        pass