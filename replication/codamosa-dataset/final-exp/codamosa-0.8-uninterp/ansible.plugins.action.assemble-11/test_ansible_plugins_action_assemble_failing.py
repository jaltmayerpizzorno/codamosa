# Automatically generated by Pynguin.
import ansible.plugins.action.assemble as module_0

def test_case_0():
    try:
        bytes_0 = b'\xc5\x98\x03\xd0\xe1\x07!\x1d/&'
        tuple_0 = ()
        bool_0 = False
        int_0 = 171
        str_0 = 'TLZB<'
        tuple_1 = (int_0, bool_0, int_0, str_0)
        action_module_0 = module_0.ActionModule(bytes_0, tuple_0, bool_0, int_0, tuple_1, tuple_1)
        var_0 = action_module_0.run()
    except BaseException:
        pass