# Automatically generated by Pynguin.
import ansible.plugins.callback.default as module_0

def test_case_0():
    pass

def test_case_1():
    callback_module_0 = module_0.CallbackModule()

def test_case_2():
    int_0 = None
    str_0 = 'C;'
    callback_module_0 = module_0.CallbackModule()
    var_0 = callback_module_0.v2_playbook_on_no_hosts_remaining()
    var_1 = callback_module_0.v2_playbook_on_notify(int_0, str_0)

def test_case_3():
    tuple_0 = ()
    callback_module_0 = module_0.CallbackModule()
    var_0 = callback_module_0.v2_playbook_on_notify(tuple_0, tuple_0)