# Automatically generated by Pynguin.
import ansible.plugins.callback.junit as module_0

def test_case_0():
    pass

def test_case_1():
    callback_module_0 = module_0.CallbackModule()
    var_0 = callback_module_0.v2_playbook_on_stats(callback_module_0)

def test_case_2():
    callback_module_0 = module_0.CallbackModule()
    callback_module_1 = module_0.CallbackModule()
    dict_0 = {callback_module_0: callback_module_0, callback_module_0: callback_module_0, callback_module_0: callback_module_1, callback_module_1: callback_module_0}
    bytes_0 = b'\xb6\xe0\xb7Vq\xaa:\xab\xcdvq\x03'
    str_0 = '_I0P_*('
    host_data_0 = module_0.HostData(dict_0, dict_0, bytes_0, str_0)

def test_case_3():
    str_0 = ''
    task_data_0 = module_0.TaskData(str_0, str_0, str_0, str_0, str_0)
    str_1 = 'ok'
    host_data_0 = module_0.HostData(str_0, str_0, str_1, str_0)
    var_0 = task_data_0.add_host(host_data_0)
    var_1 = task_data_0.host_data
    var_2 = len(var_1)
    str_2 = 'included'
    host_data_1 = module_0.HostData(str_0, str_0, str_2, str_0)
    var_3 = task_data_0.add_host(host_data_1)
    var_4 = task_data_0.host_data
    var_5 = len(var_4)