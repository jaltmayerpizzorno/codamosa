# Automatically generated by Pynguin.
import ansible.plugins.callback.junit as module_0

def test_case_0():
    try:
        bytes_0 = b'v6[k\x18D\xa0\xdeR\xd7\x88\x8e\x07\xc2\x13\xa2\xfeV'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_skipped(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xe7\xa6\x0f\x0c\xa7o\xdd\x17\x0f\xc8\xe2>H2"'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'62D\xc3'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "{[='\rfR] "
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_start(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 992
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_play_start(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_no_hosts(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'i\x99\xe4\xcfV\x80F\xc1\xee\rdV'
        dict_0 = {}
        float_0 = -1046.0
        list_0 = []
        host_data_0 = module_0.HostData(dict_0, float_0, list_0, dict_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_task_start(bytes_0, host_data_0)
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
        str_0 = '\x0b:~^h\\+'
        bytes_0 = b'G'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(str_0, bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'PT^c5I%P>&%r;'
        float_0 = -1576.840828
        list_0 = [str_0, str_0]
        int_0 = -2498
        host_data_0 = module_0.HostData(float_0, list_0, str_0, int_0)
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_on_skipped(callback_module_0)
    except BaseException:
        pass

def test_case_10():
    try:
        dict_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_include(dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        callback_module_0 = module_0.CallbackModule()
        list_0 = [callback_module_0, callback_module_0, callback_module_0, callback_module_0]
        bool_0 = False
        bytes_0 = b',\r\x16\x90\xeb\xd3bh\xb8(\rZ{o\xdeVY2\xb4'
        tuple_0 = (list_0, bytes_0)
        str_0 = None
        var_0 = callback_module_0.v2_playbook_on_stats(tuple_0)
        task_data_0 = module_0.TaskData(tuple_0, str_0, str_0, callback_module_0, bool_0)
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_0.v2_runner_on_no_hosts(bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        dict_0 = {}
        callback_module_0 = module_0.CallbackModule()
        str_0 = "%s not run command since '%s' exists"
        list_0 = [dict_0, callback_module_0]
        var_0 = callback_module_0.v2_playbook_on_stats(str_0)
        var_1 = callback_module_0.v2_runner_on_failed(list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 1
        str_0 = 'test'
        str_1 = 'path'
        str_2 = 'play'
        str_3 = 'action'
        task_data_0 = module_0.TaskData(int_0, str_0, str_1, str_2, str_3)
        str_4 = 'host1'
        host_data_0 = module_0.HostData(int_0, str_4, str_0, str_0)
        var_0 = task_data_0.add_host(host_data_0)
        host_data_1 = module_0.HostData(int_0, str_4, str_0, str_0)
        var_1 = task_data_0.add_host(host_data_1)
    except BaseException:
        pass