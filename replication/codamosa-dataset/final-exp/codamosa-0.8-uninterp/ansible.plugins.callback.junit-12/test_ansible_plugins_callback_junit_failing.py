# Automatically generated by Pynguin.
import ansible.plugins.callback.junit as module_0

def test_case_0():
    try:
        str_0 = '  executable location = %s'
        set_0 = {str_0, str_0, str_0, str_0}
        bool_0 = True
        int_0 = -568
        callback_module_0 = None
        task_data_0 = module_0.TaskData(set_0, bool_0, set_0, int_0, callback_module_0)
        str_1 = 'usermod'
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_playbook_on_task_start(task_data_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 480
        list_0 = [int_0, int_0]
        str_0 = 'DT\n'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_task_start(list_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b"\xc2\xd4\x19\x95~\x1a\xec\xda\x90\xb6\x8ax\xdd\x98'\xa2u(]"
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        callback_module_0 = module_0.CallbackModule()
        bool_0 = False
        var_0 = callback_module_0.v2_playbook_on_stats(bool_0)
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_1.v2_playbook_on_start(callback_module_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_play_start(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0}
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_no_hosts(set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_handler_task_start(float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        callback_module_0 = module_0.CallbackModule()
        str_0 = 'foo'
        str_1 = 'bar'
        var_0 = callback_module_0.v2_runner_on_failed(str_0, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -267
        list_0 = [int_0]
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_skipped(list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        callback_module_0 = module_0.CallbackModule()
        str_0 = 'Mh-w|]xQQ0'
        var_0 = callback_module_0.v2_playbook_on_include(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '1'
        str_1 = '2'
        str_2 = '4'
        str_3 = '5'
        task_data_0 = module_0.TaskData(str_0, str_1, str_3, str_2, str_3)
        str_4 = '6'
        str_5 = '9'
        host_data_0 = module_0.HostData(str_4, str_3, str_4, str_5)
        host_data_1 = module_0.HostData(str_4, str_1, str_2, str_5)
        var_0 = task_data_0.add_host(host_data_0)
        var_1 = task_data_0.add_host(host_data_1)
    except BaseException:
        pass

def test_case_12():
    try:
        task_data_0 = None
        set_0 = {task_data_0, task_data_0}
        bytes_0 = b'\x02+\xca'
        host_data_0 = module_0.HostData(set_0, set_0, bytes_0, set_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(task_data_0, host_data_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'm '
        callback_module_0 = module_0.CallbackModule()
        dict_0 = {callback_module_0: callback_module_0, str_0: str_0, callback_module_0: callback_module_0, str_0: callback_module_0}
        var_0 = callback_module_0.v2_playbook_on_stats(dict_0)
        str_1 = 'Mzsj@L'
        str_2 = '16XYUns0_-BEg\tj13E'
        dict_1 = {callback_module_0: str_2, str_2: callback_module_0, str_1: str_1}
        str_3 = 'KU'
        str_4 = ''
        set_0 = {str_1, str_0, str_0}
        host_data_0 = module_0.HostData(dict_1, str_3, str_4, set_0)
        var_1 = callback_module_0.v2_runner_on_ok(dict_1)
    except BaseException:
        pass