# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        bytes_0 = b'\xa0\xa9\x91\xe9\xf2\xf7EV\xcb\xe8(,&\x9b\x7f\xf0v\xa5A@'
        str_0 = 'H8x\n '
        str_1 = 'R(w2\x0c[X'
        float_0 = 3765.3
        str_2 = "8Bnjw>'NEk,L"
        bytes_1 = b'e4\x7f\n\x9b\xfc\xa7\\\xc0\\Wf\x8d\x0b\xe6'
        action_module_0 = module_0.ActionModule(bytes_0, str_0, str_1, float_0, str_2, bytes_1)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 512.0
        int_0 = -1458
        bool_0 = False
        list_0 = [float_0]
        tuple_0 = ()
        set_0 = {bool_0, tuple_0, float_0}
        float_1 = 0.5
        str_0 = '(pEu5r\\eQ!ysWFYL'
        str_1 = '+.@i1Y{&T'
        bytes_0 = b'>\xf7\xf5\xfc\x10h\xf8\x01\xcej\xe5~\xf6\xef\xf9\xf8'
        action_module_0 = module_0.ActionModule(tuple_0, int_0, bool_0, str_0, str_1, bytes_0)
        float_2 = -3132.98
        action_module_1 = module_0.ActionModule(float_1, action_module_0, str_1, bytes_0, float_2, list_0)
        var_0 = action_module_1.run(set_0, tuple_0)
    except BaseException:
        pass