# Automatically generated by Pynguin.
import ansible.plugins.action.include_vars as module_0

def test_case_0():
    try:
        float_0 = 1745.36
        bool_0 = True
        bytes_0 = b'\xb7\xa9^F\xc2m\x143\xd7\x80\x0c\xe1/P\x8d\xbcq\xa0'
        tuple_0 = ()
        list_0 = [bytes_0, tuple_0, bool_0]
        str_0 = 'fe\x0b^euMuLv88\\iq8'
        action_module_0 = module_0.ActionModule(bool_0, bytes_0, tuple_0, list_0, str_0, float_0)
        var_0 = action_module_0.run(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -3154
        bytes_0 = b'@\x9aw\x92\xb70\xcd'
        set_0 = {bytes_0, int_0, int_0, bytes_0}
        dict_0 = None
        bool_0 = False
        list_0 = [bytes_0, set_0, dict_0, dict_0]
        bytes_1 = b'\x04*\x18\n\xdc\xcd\xba\xdc'
        float_0 = -829.481298
        tuple_0 = ()
        str_0 = 'y a\x0bm`Z '
        float_1 = 544.45
        action_module_0 = module_0.ActionModule(dict_0, set_0, tuple_0, str_0, float_1, tuple_0)
        tuple_1 = None
        action_module_1 = module_0.ActionModule(float_0, tuple_0, action_module_0, dict_0, tuple_1, action_module_0)
        tuple_2 = (list_0, list_0, bytes_0, list_0)
        str_1 = "Jinja2's unique filter failed and we cannot fall back to Ansible's version as it does not support the parameters supplied"
        action_module_2 = module_0.ActionModule(list_0, bytes_1, int_0, tuple_2, list_0, str_1)
        var_0 = action_module_2.run(int_0, bool_0)
    except BaseException:
        pass