# Automatically generated by Pynguin.
import ansible.plugins.callback.default as module_0
import ansible.playbook.task_include as module_1

def test_case_0():
    pass

def test_case_1():
    callback_module_0 = module_0.CallbackModule()

def test_case_2():
    callback_module_0 = module_0.CallbackModule()
    task_include_0 = module_1.TaskInclude()
    var_0 = callback_module_0.v2_playbook_on_play_start(task_include_0)
    callback_module_1 = module_0.CallbackModule()
    var_1 = callback_module_1.v2_playbook_on_no_hosts_matched()

def test_case_3():
    str_0 = ''
    callback_module_0 = module_0.CallbackModule()
    var_0 = callback_module_0.v2_playbook_on_notify(str_0, str_0)