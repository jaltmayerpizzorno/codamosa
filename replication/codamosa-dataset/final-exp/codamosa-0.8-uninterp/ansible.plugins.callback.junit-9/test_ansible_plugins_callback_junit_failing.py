# Automatically generated by Pynguin.
import ansible.plugins.callback.junit as module_0

def test_case_0():
    try:
        bytes_0 = b'\x18X>\x90$\xb0\xad'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_stats(bytes_0)
        task_data_0 = None
        var_1 = callback_module_0.v2_runner_on_ok(task_data_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'eMXH 4mPtu$R'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_no_hosts(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = None
        dict_0 = {tuple_0: tuple_0}
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        host_data_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_stats(host_data_0)
        list_0 = None
        var_1 = callback_module_0.v2_playbook_on_start(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'KDE neon'
        host_data_0 = None
        bool_0 = None
        set_0 = {host_data_0, host_data_0, bool_0, str_0}
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_stats(host_data_0)
        task_data_0 = module_0.TaskData(bool_0, bool_0, set_0, callback_module_0, callback_module_0)
        float_0 = None
        var_1 = task_data_0.add_host(task_data_0)
        var_2 = callback_module_0.v2_playbook_on_play_start(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ':HUk\x0b3da'
        str_1 = 'k[]5;'
        dict_0 = {str_0: str_1}
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_task_start(str_0, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'when changing (small) files and templates, show the differences in those files; works great with --check'
        bool_0 = None
        str_1 = 'C-!S:| \t82>;>_'
        tuple_0 = (str_0, bool_0, str_1)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ''
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_handler_task_start(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        callback_module_0 = module_0.CallbackModule()
        int_0 = -2606
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_on_failed(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = None
        float_0 = -1321.0
        dict_0 = None
        callback_module_0 = module_0.CallbackModule()
        int_0 = 523
        str_1 = ";%\r8MS*WBFV21'("
        str_2 = 'isfifo'
        bytes_0 = b'5l\xc9x\xdf^u&\xa1w\xa2\xd1\xf7\xbb\x1d\xfcV'
        bool_0 = True
        tuple_0 = (bytes_0, bool_0)
        bytes_1 = b"9\xc7\xc7J\xf7\x7ft\x00\x1c\xee\xd7:\x83'7HWN\xd72"
        str_3 = '6xj&'
        task_data_0 = module_0.TaskData(str_1, str_2, tuple_0, bytes_1, str_3)
        str_4 = 'slaves'
        str_5 = '5dCrse\x0cM9Z`[U'
        list_0 = [str_5, callback_module_0]
        set_0 = None
        task_data_1 = module_0.TaskData(task_data_0, str_4, list_0, set_0, callback_module_0)
        bytes_2 = b"\xcb\xe0A@1wGO\xf8\xe8\\\x89<>(H'"
        host_data_0 = module_0.HostData(task_data_1, dict_0, list_0, bytes_2)
        host_data_1 = module_0.HostData(int_0, str_0, host_data_0, dict_0)
        host_data_2 = module_0.HostData(float_0, dict_0, callback_module_0, host_data_1)
        set_1 = None
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_on_skipped(set_1)
    except BaseException:
        pass

def test_case_11():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_playbook_on_include(callback_module_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'6\xd3\x81I \xd8E\x85'
        int_0 = 2057
        float_0 = 1026.94021
        bytes_1 = b'\xdb\x1b\xb6\x97x\xd2\xa3\xd5$\x10'
        float_1 = 2543.246733
        list_0 = [bytes_1]
        task_data_0 = module_0.TaskData(int_0, float_0, bytes_1, float_1, list_0)
        var_0 = task_data_0.add_host(bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = None
        list_0 = [float_0, float_0, float_0, float_0]
        bytes_0 = None
        float_1 = -107.8
        host_data_0 = module_0.HostData(list_0, bytes_0, float_1, float_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'dummy'
        str_1 = 'ok'
        str_2 = 'result'
        str_3 = 'dummy_result'
        host_data_0 = module_0.HostData(str_0, str_0, str_1, str_1)
        task_data_0 = module_0.TaskData(str_0, str_0, str_0, str_0, str_0)
        var_0 = task_data_0.add_host(host_data_0)
        str_4 = {str_2: str_3}
        host_data_1 = module_0.HostData(str_0, str_0, str_1, str_4)
        var_1 = task_data_0.add_host(host_data_1)
    except BaseException:
        pass