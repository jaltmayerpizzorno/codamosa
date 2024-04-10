# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0
import ansible.parsing.dataloader as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = 12
    dict_0 = {int_0: int_0, int_0: int_0}
    task_result_0 = module_0.TaskResult(int_0, dict_0, dict_0)

def test_case_2():
    var_0 = None
    str_0 = 'failed'
    bool_0 = True
    bool_1 = {str_0: bool_0}
    task_result_0 = module_0.TaskResult(var_0, var_0, bool_1)
    var_1 = task_result_0.is_failed()

def test_case_3():
    str_0 = '\n    {\n        "failed_when_result": false,\n        "invocation": {\n            "module_name": "command",\n            "module_args": "echo  hello"\n        },\n        "rc": 0,\n        "delta": "0:00:00.005218",\n        "start": "2018-05-09 16:42:51.869094",\n        "end": "2018-05-09 16:42:51.874286",\n        "stdout": "hello",\n        "stdout_lines": [\n            "hello"\n        ],\n        "warnings": []\n    }\n    '
    data_loader_0 = module_1.DataLoader()
    var_0 = data_loader_0.load(str_0)
    var_1 = None
    task_result_0 = module_0.TaskResult(var_1, var_1, var_0)
    var_2 = task_result_0.is_failed()

def test_case_4():
    int_0 = 12
    dict_0 = {int_0: int_0, int_0: int_0}
    task_result_0 = module_0.TaskResult(int_0, dict_0, dict_0)
    var_0 = task_result_0.is_unreachable()

def test_case_5():
    str_0 = 'P0:PmLM4d(73P9 '
    bool_0 = False
    task_result_0 = module_0.TaskResult(bool_0, str_0, str_0)
    var_0 = task_result_0.needs_debugger()

def test_case_6():
    str_0 = '\n    {\n        "failed_when_result": false,\n        "invocation": {\n            "module_name": "command",\n            "module_args": "echo  hello"\n        },\n        "rc": 0,\n        "delta": "0:00:00.005218",\n        "start": "2018-05-09 16:42:51.869094",\n        "end": "2018-05-09 16:42:51.874286",\n        "stdout": "hello",\n        "stdout_lines": [\n            "hello"\n        ],\n        "warnings": []\n    }\n    '
    data_loader_0 = module_1.DataLoader()
    var_0 = data_loader_0.load(str_0)
    var_1 = None
    task_result_0 = module_0.TaskResult(var_1, var_1, var_0)
    var_2 = task_result_0.is_changed()
    var_3 = task_result_0.is_failed()

def test_case_7():
    str_0 = 'results'
    bool_0 = True
    bool_1 = {str_0: bool_0}
    bool_2 = {str_0: bool_1}
    str_1 = 'host'
    str_2 = 'task'
    task_result_0 = module_0.TaskResult(str_1, str_2, bool_2, str_2)
    var_0 = task_result_0.is_skipped()

def test_case_8():
    str_0 = 'skipped'
    bool_0 = True
    bool_1 = {str_0: bool_0}
    str_1 = 'task'
    task_result_0 = module_0.TaskResult(str_1, str_1, bool_1)
    bool_2 = False
    bool_3 = {str_0: bool_2}
    task_result_1 = module_0.TaskResult(str_0, str_1, bool_3)
    var_0 = task_result_1.is_skipped()
    str_2 = 'results'
    bool_4 = {str_0: bool_0}
    bool_5 = [bool_4]
    bool_6 = {str_2: bool_5}
    task_result_2 = module_0.TaskResult(str_1, str_1, bool_6)
    var_1 = task_result_2.is_skipped()
    bool_7 = {str_0: bool_2}
    bool_8 = [bool_7]
    bool_9 = {str_2: bool_8}
    task_result_3 = module_0.TaskResult(str_2, str_1, bool_9)
    var_2 = task_result_3.is_skipped()

def test_case_9():
    str_0 = 'results'
    bool_0 = False
    bool_1 = {str_0: bool_0}
    bool_2 = True
    bool_3 = {str_0: bool_2}
    bool_4 = [bool_1, bool_3]
    bool_5 = {str_0: bool_4}
    str_1 = 'host'
    str_2 = 'task'
    task_result_0 = module_0.TaskResult(str_1, str_2, bool_5, str_0)
    var_0 = task_result_0.is_skipped()

def test_case_10():
    str_0 = 'debugger'
    str_1 = 'ignore_errors'
    str_2 = 'always'
    bool_0 = False
    var_0 = {str_0: str_2, str_1: bool_0}
    str_3 = 'action'
    str_4 = {str_3: str_2}
    bool_1 = True
    str_5 = 'failed'
    bool_2 = True
    bool_3 = {str_5: bool_0, str_5: bool_2}
    str_6 = 'hostname_1'
    task_result_0 = module_0.TaskResult(str_6, str_4, bool_3, var_0)
    var_1 = task_result_0.needs_debugger(bool_1)

def test_case_11():
    var_0 = None
    var_1 = dict()
    task_result_0 = module_0.TaskResult(var_0, var_0, var_1)
    bool_0 = False
    var_2 = task_result_0.needs_debugger(bool_0)
    bool_1 = True
    var_3 = task_result_0.needs_debugger(bool_1)
    var_4 = dict(failed=bool_1)
    var_5 = task_result_0.is_unreachable()
    str_0 = 'on_failed'
    var_6 = dict(debugger=str_0)
    var_7 = dict(failed=str_0)
    task_result_1 = module_0.TaskResult(var_0, var_0, var_7, var_6)
    var_8 = task_result_1.needs_debugger(bool_1)

def test_case_12():
    var_0 = None
    var_1 = dict()
    task_result_0 = module_0.TaskResult(var_0, var_0, var_1)
    bool_0 = False
    var_2 = task_result_0.needs_debugger(bool_0)
    bool_1 = True
    var_3 = task_result_0.needs_debugger(bool_1)
    str_0 = 'never'
    var_4 = dict(debugger=str_0)
    var_5 = dict(failed=bool_1)
    task_result_1 = module_0.TaskResult(var_0, var_0, var_5, var_4)
    var_6 = task_result_1.needs_debugger(bool_1)
    var_7 = dict(debugger=str_0, ignore_errors=bool_1)
    var_8 = dict(failed=bool_1)
    task_result_2 = module_0.TaskResult(var_0, var_0, var_8, var_7)
    var_9 = task_result_2.needs_debugger(bool_1)
    str_1 = 'on_failed'
    var_10 = dict(debugger=str_1)
    var_11 = dict(failed=bool_1)
    task_result_3 = module_0.TaskResult(var_0, var_0, var_11, var_10)
    var_12 = task_result_3.needs_debugger(bool_1)

def test_case_13():
    var_0 = None
    bool_0 = True
    var_1 = dict(failed=bool_0)
    task_result_0 = module_0.TaskResult(var_0, var_0, var_1)
    var_2 = task_result_0.is_failed()
    bool_1 = False
    var_3 = dict(failed=bool_1)
    task_result_1 = module_0.TaskResult(var_0, var_0, var_3)
    var_4 = task_result_1.is_failed()
    var_5 = dict(failed=bool_0)
    var_6 = [var_5]
    var_7 = dict(results=var_6)
    task_result_2 = module_0.TaskResult(var_0, var_0, var_7)
    var_8 = task_result_2.is_failed()
    var_9 = dict(failed=bool_1)
    var_10 = dict(results=var_3)
    task_result_3 = module_0.TaskResult(var_0, var_0, var_10)
    var_11 = task_result_3.is_failed()
    var_12 = dict(failed=bool_0)
    var_13 = dict(failed=bool_1)
    var_14 = [var_12, var_13]
    var_15 = dict(results=var_14)
    task_result_4 = module_0.TaskResult(var_0, var_0, var_15)
    var_16 = task_result_4.is_failed()
    var_17 = dict(failed=bool_1)
    var_18 = dict(failed=bool_1)
    var_19 = [var_17, var_18]
    var_20 = dict(results=var_19)
    task_result_5 = module_0.TaskResult(var_0, var_0, var_20)