# Automatically generated by Pynguin.
import ansible.plugins.action.pause as module_0

def test_case_0():
    try:
        int_0 = None
        dict_0 = {}
        var_0 = module_0.timeout_handler(int_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.is_interactive()
        list_0 = [var_0, var_0]
        bytes_0 = b'`\x9b_p'
        dict_0 = {}
        str_0 = None
        list_1 = []
        str_1 = 'E?bM2'
        action_module_0 = module_0.ActionModule(list_0, bytes_0, dict_0, str_0, list_1, str_1)
        var_1 = module_0.clear_line(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2898.655
        list_0 = [float_0, float_0, float_0]
        bool_0 = False
        int_0 = -3645
        bool_1 = True
        bytes_0 = b'\r\xd3\x85'
        action_module_0 = module_0.ActionModule(float_0, list_0, bool_0, int_0, bool_1, bytes_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '%s (args=%s vars=%s): %s'
        ansible_timeout_exceeded_0 = module_0.AnsibleTimeoutExceeded()
        dict_0 = {ansible_timeout_exceeded_0: ansible_timeout_exceeded_0, str_0: str_0, ansible_timeout_exceeded_0: ansible_timeout_exceeded_0}
        set_0 = {str_0, ansible_timeout_exceeded_0}
        list_0 = None
        str_1 = ';W[^7q@g)P^qY'
        bytes_0 = b"\xc1'\xe8\x00\xa0\xd85 \xd7\xd0Fk\x9c\xcf\xfe\x9f"
        action_module_0 = module_0.ActionModule(ansible_timeout_exceeded_0, dict_0, set_0, list_0, str_1, bytes_0)
        set_1 = set()
        int_0 = 2279
        bool_0 = False
        list_1 = [bool_0, bool_0]
        ansible_timeout_exceeded_1 = module_0.AnsibleTimeoutExceeded(*list_1)
        str_2 = 'zCZ\\\nTQ+^x9:$S~g'
        int_1 = 184
        action_module_1 = module_0.ActionModule(set_1, int_0, bool_0, ansible_timeout_exceeded_1, str_2, int_1)
        var_0 = action_module_1.run(str_0, action_module_0)
    except BaseException:
        pass