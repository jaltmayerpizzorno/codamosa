# Automatically generated by Pynguin.
import ansible.plugins.callback.default as module_0
import ansible.playbook.task_include as module_1

def test_case_0():
    try:
        bytes_0 = b'0\x99^L\x0fU[\x9f\xc6\x95\xf3\x8d\x08\x0f'
        bool_0 = True
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.set_options(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_matched()
        callback_module_1 = module_0.CallbackModule()
        set_0 = {callback_module_1, callback_module_1, callback_module_1, callback_module_1}
        float_0 = None
        list_0 = [set_0, callback_module_1, set_0, float_0]
        var_1 = callback_module_1.v2_runner_on_failed(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        callback_module_0 = module_0.CallbackModule()
        int_0 = 1739
        var_0 = callback_module_0.v2_runner_on_skipped(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 145
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_unreachable(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_matched()
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_1.v2_playbook_on_start(set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_no_hosts_remaining()
        int_0 = 1548
        callback_module_1 = module_0.CallbackModule()
        var_1 = callback_module_1.v2_playbook_on_stats(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_task_start(tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 6
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_handler_task_start(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '/kJ8<'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 82
        set_0 = {int_0, int_0, int_0}
        bytes_0 = b'\xfb\x93o$\x87\x1b&a'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_start(set_0, bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 10240
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_item_on_ok(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        callback_module_0 = module_0.CallbackModule()
        bytes_0 = b'X\x9ely3\xb47Sk'
        var_0 = callback_module_0.v2_runner_item_on_failed(bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_runner_item_on_skipped(callback_module_0)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = []
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_include(list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_playbook_on_stats(callback_module_0)
    except BaseException:
        pass

def test_case_16():
    try:
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_start(callback_module_0)
    except BaseException:
        pass

def test_case_17():
    try:
        tuple_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_retry(tuple_0)
    except BaseException:
        pass

def test_case_18():
    try:
        tuple_0 = None
        dict_0 = {tuple_0: tuple_0}
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_async_poll(dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'R0>;RYk;THuG5+.VhUF!'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_async_ok(str_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '\\o'
        list_0 = [str_0]
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_async_failed(list_0)
    except BaseException:
        pass

def test_case_21():
    try:
        callback_module_0 = module_0.CallbackModule()
        int_0 = 599
        var_0 = callback_module_0.v2_playbook_on_play_start(int_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'S;!>Y`;qIF'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_on_file_diff(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        tuple_0 = ()
        task_include_0 = module_1.TaskInclude(tuple_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(task_include_0)
    except BaseException:
        pass