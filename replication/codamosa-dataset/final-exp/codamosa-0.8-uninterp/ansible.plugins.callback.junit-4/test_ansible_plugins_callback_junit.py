# Automatically generated by Pynguin.
import ansible.plugins.callback.junit as module_0

def test_case_0():
    pass

def test_case_1():
    callback_module_0 = module_0.CallbackModule()
    var_0 = callback_module_0.v2_playbook_on_stats(callback_module_0)

def test_case_2():
    var_0 = None
    var_1 = lambda : var_0
    str_0 = '_file_name'
    str_1 = '/home/user/ansible/playbooks/test.yml'
    var_2 = setattr(var_1, str_0, str_1)
    callback_module_0 = module_0.CallbackModule()
    var_3 = callback_module_0.v2_playbook_on_start(var_1)
    var_4 = callback_module_0._playbook_name

def test_case_3():
    str_0 = 'uuid'
    str_1 = 'name'
    str_2 = 'path'
    str_3 = 'play'
    str_4 = 'action'
    task_data_0 = module_0.TaskData(str_0, str_1, str_2, str_3, str_4)
    str_5 = 'status'
    str_6 = 'result'
    host_data_0 = module_0.HostData(str_0, str_1, str_5, str_6)
    var_0 = task_data_0.add_host(host_data_0)

def test_case_4():
    str_0 = 'asd'
    str_1 = 'name'
    str_2 = 'path'
    str_3 = 'play'
    str_4 = 'action'
    task_data_0 = module_0.TaskData(str_0, str_1, str_2, str_3, str_4)
    str_5 = 'qwe'
    str_6 = 'host_name'
    str_7 = 'result'
    host_data_0 = module_0.HostData(str_5, str_6, str_5, str_7)
    str_8 = 'included'
    str_9 = 'result2'
    host_data_1 = module_0.HostData(str_5, str_6, str_8, str_9)
    var_0 = task_data_0.add_host(host_data_0)
    var_1 = task_data_0.add_host(host_data_1)