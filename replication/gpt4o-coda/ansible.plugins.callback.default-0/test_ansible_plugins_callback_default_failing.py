# Automatically generated by Pynguin.
import ansible.plugins.callback.default as module_0

def test_case_0():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.set_options()
    except BaseException:
        pass

def test_case_1():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        callback_module_2 = module_0.CallbackModule()
        var_0 = callback_module_2.v2_runner_on_ok(callback_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = None
        list_0 = [set_0, set_0]
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_skipped(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_remaining()
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_1.v2_runner_on_unreachable(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_matched()
        callback_module_1 = module_0.CallbackModule()
        bool_0 = True
        dict_0 = {callback_module_1: bool_0, callback_module_1: callback_module_1, bool_0: bool_0}
        str_0 = 'E"E\t3*p*U$\tqCI!'
        callback_module_2 = module_0.CallbackModule()
        float_0 = -2263.7
        set_0 = set()
        tuple_0 = (callback_module_2, float_0, set_0)
        int_0 = 82
        tuple_1 = (dict_0, str_0, tuple_0, int_0)
        int_1 = -2745
        var_1 = callback_module_1.v2_playbook_on_notify(tuple_1, int_1)
        var_2 = callback_module_1.v2_playbook_on_cleanup_task_start(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_remaining()
        float_0 = -1942.2763
        set_0 = {float_0}
        list_0 = [set_0]
        tuple_0 = ()
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_1.v2_playbook_on_notify(list_0, tuple_0)
        callback_module_2 = module_0.CallbackModule()
        var_2 = callback_module_2.v2_runner_on_start(set_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        callback_module_0 = module_0.CallbackModule()
        str_0 = '\ncU:rM'
        var_0 = callback_module_0.v2_playbook_on_task_start(callback_module_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(callback_module_0)
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_handler_task_start(tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        callback_module_0 = module_0.CallbackModule()
        str_0 = None
        var_0 = callback_module_0.v2_runner_on_start(str_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'@\x8b3hA\xc5YM\xe4\xf6\x8a\xcc\x81\xb4R'
        complex_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_notify(bytes_0, complex_0)
        float_0 = 2.0
        var_1 = callback_module_0.v2_playbook_on_play_start(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '-Yh?'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_on_file_diff(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0]
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_item_on_ok(list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = None
        callback_module_0 = module_0.CallbackModule()
        bool_0 = True
        float_0 = -343.938447
        list_0 = [bool_0, int_0, float_0]
        int_1 = 70
        var_0 = callback_module_0.v2_playbook_on_notify(list_0, int_1)
        var_1 = callback_module_0.v2_runner_item_on_failed(bool_0)
    except BaseException:
        pass

def test_case_14():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_item_on_skipped(callback_module_0)
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = 660.0
        dict_0 = {float_0: float_0}
        tuple_0 = (dict_0,)
        tuple_1 = (tuple_0,)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_include(tuple_1)
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b'\xfc\xacA\xd6;\xb9\xcci\xbeo\xbb\xab;\xd9\x13\xa4j'
        dict_0 = {bytes_0: bytes_0}
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_stats(dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_start(callback_module_0)
    except BaseException:
        pass

def test_case_18():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_retry(callback_module_0)
    except BaseException:
        pass

def test_case_19():
    try:
        bytes_0 = b':\x91\xf15\xab\x062r\xe8.\xd9Q\x13\xf7q\xe0'
        bool_0 = False
        int_0 = 69
        tuple_0 = (bytes_0, bool_0, int_0, int_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_async_poll(tuple_0)
    except BaseException:
        pass

def test_case_20():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_remaining()
        callback_module_1 = module_0.CallbackModule()
        list_0 = [callback_module_1, callback_module_1, callback_module_1, callback_module_1]
        var_1 = callback_module_1.v2_runner_on_async_failed(list_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = None
        dict_0 = {str_0: str_0, str_0: str_0}
        list_0 = [str_0, dict_0, dict_0, str_0]
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(list_0)
    except BaseException:
        pass

def test_case_22():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        dict_0 = {}
        callback_module_2 = module_0.CallbackModule()
        var_0 = callback_module_2.v2_runner_on_async_ok(dict_0)
    except BaseException:
        pass