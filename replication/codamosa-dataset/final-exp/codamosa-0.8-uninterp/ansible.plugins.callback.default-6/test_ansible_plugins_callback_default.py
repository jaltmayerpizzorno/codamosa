# Automatically generated by Pynguin.
import ansible.plugins.callback.default as module_0

def test_case_0():
    pass

def test_case_1():
    callback_module_0 = module_0.CallbackModule()

def test_case_2():
    bool_0 = False
    str_0 = 'V'
    callback_module_0 = module_0.CallbackModule()
    var_0 = callback_module_0.v2_playbook_on_notify(bool_0, str_0)
    callback_module_1 = module_0.CallbackModule()
    var_1 = callback_module_1.v2_playbook_on_no_hosts_matched()

def test_case_3():
    float_0 = 0.0
    callback_module_0 = module_0.CallbackModule()
    var_0 = callback_module_0.v2_playbook_on_notify(float_0, callback_module_0)