# Automatically generated by Pynguin.
import ansible.plugins.action.assemble as module_0

def test_case_0():
    try:
        bytes_0 = b'8\x03\xec\x0b\t\x89mv\x04`\xcd\\\n,\xd22\xec'
        tuple_0 = ()
        int_0 = -1325
        str_0 = 'a'
        action_module_0 = module_0.ActionModule(bytes_0, tuple_0, int_0, str_0, bytes_0, tuple_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass