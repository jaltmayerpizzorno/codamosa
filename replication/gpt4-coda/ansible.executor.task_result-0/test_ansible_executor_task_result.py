# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0

def test_case_0():
    bytes_0 = b'\x8e"4\xf5B\x99Q\x81(`l\xe4\x0f~\xcb\t'
    str_0 = '^(-?\\d+)(b|k|m|g|t)?$'
    task_result_0 = module_0.TaskResult(bytes_0, str_0, str_0)

def test_case_1():
    bytes_0 = b'\x97\x8e\x85\xd1\x97\xbc\xa1'
    str_0 = 'Choose which plugin type (defaults to "module"). Available plugin types are : {0}'
    task_result_0 = module_0.TaskResult(bytes_0, bytes_0, str_0)
    var_0 = task_result_0.is_unreachable()
    var_1 = task_result_0.needs_debugger()

def test_case_2():
    bytes_0 = b'\x97\x8e\x85\xd1\x97\xbc\xa1'
    str_0 = 'Choose which plugin type (defaults to "module"). Available plugin types are : {0}'
    task_result_0 = module_0.TaskResult(bytes_0, bytes_0, str_0)
    var_0 = task_result_0.needs_debugger()

def test_case_3():
    bytes_0 = b'\x97\x8e\x85\xd1\x97\xbc\xa1'
    str_0 = 'Choose which plugin type (defaults to "module"). Available plugin types are : {0}'
    task_result_0 = module_0.TaskResult(bytes_0, bytes_0, str_0)
    var_0 = task_result_0.is_failed()

def test_case_4():
    bytes_0 = b'\x97\x8e\x85\xd1\x97\xbc\xa1'
    str_0 = 'Choose which plugin type (defaults to "module"). Available plugin types are : {0}'
    task_result_0 = module_0.TaskResult(bytes_0, bytes_0, str_0)
    var_0 = task_result_0.is_failed()
    dict_0 = {task_result_0: task_result_0}
    var_1 = task_result_0.needs_debugger(dict_0)

def test_case_5():
    str_0 = 'dummy_task'
    str_1 = 'skipped'
    bool_0 = True
    str_2 = 'results'
    bool_1 = {str_1: bool_0}
    bool_2 = {str_1: bool_0}
    bool_3 = [bool_1, bool_2]
    bool_4 = {str_2: bool_3}
    task_result_0 = module_0.TaskResult(str_1, str_0, bool_4)
    var_0 = task_result_0.is_skipped()

def test_case_6():
    str_0 = 'localhost'
    str_1 = 'dummy_task'
    var_0 = {}
    str_2 = 'failed'
    bool_0 = False
    bool_1 = {str_2: bool_0}
    task_result_0 = module_0.TaskResult(str_0, str_1, bool_1, var_0)
    var_1 = task_result_0.is_failed()
    str_3 = 'failed_when_result'
    bool_2 = {str_3: bool_0}
    task_result_1 = module_0.TaskResult(str_0, str_1, bool_2, var_0)
    var_2 = task_result_1.is_failed()
    str_4 = 'some_other_key'
    bool_3 = {str_4: bool_0}
    task_result_2 = module_0.TaskResult(str_0, str_1, bool_3, var_0)
    var_3 = task_result_2.is_failed()

def test_case_7():
    str_0 = 'localhost'
    str_1 = 'failed'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    task_result_0 = module_0.TaskResult(str_0, str_1, bool_1, bool_1)
    var_0 = task_result_0.needs_debugger(bool_0)

def test_case_8():
    str_0 = 'localhost'
    str_1 = 'dummy_task'
    bool_0 = True
    str_2 = 'results'
    bool_1 = {str_0: bool_0}
    bool_2 = {str_0: bool_0}
    bool_3 = [bool_1, bool_2]
    bool_4 = {str_2: bool_3}
    task_result_0 = module_0.TaskResult(str_0, str_1, bool_4)
    var_0 = task_result_0.is_skipped()

def test_case_9():
    str_0 = 'localhost'
    str_1 = 'dummy_task'
    str_2 = 'skipped'
    bool_0 = True
    bool_1 = {str_2: bool_0}
    task_result_0 = module_0.TaskResult(str_0, str_1, bool_1)
    var_0 = task_result_0.is_skipped()
    bool_2 = False
    bool_3 = {str_2: bool_2}
    task_result_1 = module_0.TaskResult(str_0, str_1, bool_3)
    var_1 = task_result_1.is_skipped()
    str_3 = 'results'
    bool_4 = {str_2: bool_0}
    bool_5 = {str_3: bool_4}
    task_result_2 = module_0.TaskResult(str_0, str_1, bool_5)
    var_2 = task_result_2.is_skipped()

def test_case_10():
    str_0 = 'localhost'
    str_1 = 'mock_task'
    str_2 = 'debugger'
    str_3 = 'ignore_errors'
    str_4 = 'always'
    bool_0 = False
    var_0 = {str_2: str_4, str_3: bool_0}
    task_result_0 = module_0.TaskResult(str_0, str_1, str_2, var_0)
    var_1 = task_result_0.needs_debugger()
    var_2 = task_result_0.needs_debugger()

def test_case_11():
    str_0 = 'dummy_task'
    bool_0 = False
    str_1 = 'results'
    bool_1 = {str_1: bool_0}
    task_result_0 = module_0.TaskResult(str_1, str_0, bool_1)
    var_0 = task_result_0.is_skipped()