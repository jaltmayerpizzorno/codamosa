# Automatically generated by Pynguin.
import ansible.plugins.callback.junit as module_0

def test_case_0():
    try:
        bytes_0 = None
        int_0 = 3102
        str_0 = 'p">*TGe[[6Cv@'
        set_0 = None
        list_0 = [set_0, int_0, bytes_0]
        list_1 = [str_0]
        host_data_0 = module_0.HostData(list_0, list_1, bytes_0, bytes_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_stats(host_data_0)
        var_1 = callback_module_0.v2_playbook_on_play_start(list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'vJH&'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        callback_module_0 = module_0.CallbackModule()
        int_0 = 2480
        var_0 = callback_module_0.v2_runner_on_failed(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = set()
        list_0 = None
        tuple_0 = (list_0, set_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_start(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_playbook_on_play_start(callback_module_0)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = []
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_stats(list_0)
        var_1 = callback_module_0.v2_runner_on_no_hosts(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        callback_module_0 = module_0.CallbackModule()
        host_data_0 = None
        var_0 = callback_module_0.v2_playbook_on_task_start(host_data_0, callback_module_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_handler_task_start(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_on_ok(callback_module_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        tuple_0 = (bool_0,)
        list_0 = []
        int_0 = 9000
        task_data_0 = module_0.TaskData(tuple_0, tuple_0, list_0, int_0, list_0)
        callback_module_0 = module_0.CallbackModule()
        host_data_0 = module_0.HostData(task_data_0, callback_module_0, bool_0, list_0)
        set_0 = set()
        var_0 = callback_module_0.v2_runner_on_skipped(set_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'java_properties'
        set_0 = {str_0, str_0, str_0, str_0}
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_include(set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        callback_module_0 = module_0.CallbackModule()
        int_0 = 1756
        bool_0 = True
        str_0 = 'weeknumber'
        str_1 = 'sSXA4~Vs'
        callback_module_1 = module_0.CallbackModule()
        task_data_0 = module_0.TaskData(int_0, bool_0, str_0, str_1, callback_module_1)
        var_0 = task_data_0.add_host(callback_module_0)
    except BaseException:
        pass

def test_case_12():
    try:
        callback_module_0 = module_0.CallbackModule()
        int_0 = 2480
        callback_module_1 = module_0.CallbackModule()
        list_0 = []
        str_0 = 'A%}6'
        host_data_0 = module_0.HostData(callback_module_1, callback_module_0, list_0, str_0)
        var_0 = callback_module_0.v2_runner_on_failed(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        callback_module_0 = module_0.CallbackModule()
        int_0 = 348
        var_0 = callback_module_0.v2_runner_on_failed(int_0, callback_module_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'abc'
        str_1 = 'name'
        str_2 = 'path'
        str_3 = 'play'
        str_4 = 'action'
        task_data_0 = module_0.TaskData(str_0, str_1, str_2, str_3, str_4)
        str_5 = 'host'
        str_6 = 'status'
        str_7 = 'result'
        host_data_0 = module_0.HostData(str_0, str_5, str_6, str_7)
        var_0 = task_data_0.add_host(host_data_0)
        var_1 = task_data_0.host_data
        var_2 = len(var_1)
        var_3 = task_data_0.host_data[str_0]
        var_4 = var_3.result
        var_5 = len(var_4)
        str_8 = 'def'
        str_9 = 'host2'
        str_10 = 'status2'
        str_11 = 'result2'
        host_data_1 = module_0.HostData(str_8, str_9, str_10, str_11)
        var_6 = task_data_0.add_host(host_data_1)
        var_7 = task_data_0.host_data
        var_8 = len(var_7)
        var_9 = task_data_0.host_data[str_0]
        var_10 = var_9.result
        var_11 = len(var_10)
        var_12 = task_data_0.host_data[str_8]
        var_13 = var_12.result
        var_14 = len(var_13)
        str_12 = 'abc'
        str_13 = 'host'
        str_14 = 'status'
        str_15 = 'result'
        host_data_2 = module_0.HostData(str_12, str_13, str_14, str_15)
        var_15 = task_data_0.add_host(host_data_2)
    except BaseException:
        pass