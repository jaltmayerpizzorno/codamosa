# Automatically generated by Pynguin.
import ansible.plugins.action.assemble as module_0

def test_case_0():
    try:
        str_0 = 'e$0$?*8N'
        bytes_0 = b';\x9c\xb0bc\xf2\x1er\x06\x04$`\xe6'
        list_0 = [str_0, bytes_0, str_0, bytes_0]
        tuple_0 = None
        int_0 = 2044
        action_module_0 = module_0.ActionModule(str_0, bytes_0, list_0, tuple_0, int_0, bytes_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass