# Automatically generated by Pynguin.
import ansible.parsing.dataloader as module_0
import ansible.executor.task_result as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    float_0 = 2381.4715
    data_loader_0 = module_0.DataLoader()
    dict_0 = {float_0: float_0, float_0: data_loader_0, bool_0: float_0, data_loader_0: bool_0}
    task_result_0 = module_1.TaskResult(bool_0, float_0, dict_0)
    var_0 = task_result_0.is_failed()

def test_case_2():
    str_0 = '\n    {\n        "failed_when_result": false,\n        "msg": "the output has beenhidden due to the fact that \'no_log: true\' was specified for this result",\n        "changed": false,\n        "invocation": {\n            "module_name": "debug",\n            "module_args": {\n                "msg": "Hello, world!",\n                "_ansible_verbose_always": true\n            },\n            "module_complex_args": {\n                "msg": "Hello, world!",\n                "_ansible_verbose_always": true\n            }\n        },\n        "stdout": "Hello, world!",\n        "stderr": "",\n        "_ansible_verbose_always": true,\n        "_ansible_no_log": true\n    }\n    '
    bytes_0 = b'\xa8'
    data_loader_0 = module_0.DataLoader()
    float_0 = 1818.26
    dict_0 = {str_0: data_loader_0}
    task_result_0 = module_1.TaskResult(data_loader_0, float_0, dict_0)
    var_0 = task_result_0.needs_debugger(bytes_0)

def test_case_3():
    int_0 = 904
    bool_0 = True
    bytes_0 = b'\x1c\x83\xb4C\x1d\xfd\x08\xc6\xbc\xf1\xbc\x9d'
    set_0 = None
    dict_0 = {bool_0: int_0, bytes_0: set_0}
    task_result_0 = module_1.TaskResult(int_0, bool_0, dict_0)
    var_0 = task_result_0.is_skipped()
    var_1 = task_result_0.needs_debugger()
    var_2 = task_result_0.is_unreachable()

def test_case_4():
    var_0 = None
    var_1 = None
    str_0 = 'results'
    var_2 = {str_0: str_0}
    var_3 = None
    task_result_0 = module_1.TaskResult(var_0, var_1, var_2, var_3)
    var_4 = task_result_0.is_skipped()

def test_case_5():
    var_0 = None
    var_1 = None
    str_0 = 'results'
    str_1 = 'skipped'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    str_2 = 'msg'
    var_2 = {str_1: bool_0, str_2: str_2}
    var_3 = [bool_1, var_2]
    var_4 = {str_0: var_3}
    var_5 = None
    task_result_0 = module_1.TaskResult(var_0, var_1, var_4, var_5)
    var_6 = task_result_0.is_skipped()

def test_case_6():
    bool_0 = True
    var_0 = dict(failed=bool_0)
    bool_1 = False
    var_1 = dict(ignore_errors=bool_1)
    var_2 = dict(failed=bool_0)
    var_3 = dict(ignore_errors=bool_0)
    var_4 = dict(failed_when_result=bool_0)
    var_5 = dict()
    task_result_0 = module_1.TaskResult(var_0, var_0, var_4, var_5)
    var_6 = task_result_0.is_failed()

def test_case_7():
    var_0 = None
    var_1 = None
    str_0 = 'results'
    str_1 = 'kiped'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    var_2 = [bool_1, var_0]
    var_3 = {str_0: var_2}
    var_4 = None
    task_result_0 = module_1.TaskResult(var_0, var_1, var_3, var_4)
    var_5 = task_result_0.is_skipped()

def test_case_8():
    var_0 = None
    var_1 = None
    str_0 = 'results'
    str_1 = 'kiped'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    var_2 = [bool_1, var_0]
    var_3 = {str_0: var_2}
    var_4 = None
    task_result_0 = module_1.TaskResult(var_0, var_1, var_3, var_4)
    var_5 = task_result_0.is_changed()
    var_6 = task_result_0.is_skipped()

def test_case_9():
    str_0 = 'host'
    str_1 = 'task'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    task_result_0 = module_1.TaskResult(str_0, str_1, bool_1)
    var_0 = task_result_0.is_skipped()
    str_2 = 'results'
    bool_2 = [bool_1]
    bool_3 = {str_2: bool_2}
    task_result_1 = module_1.TaskResult(str_0, str_1, bool_3)
    var_1 = task_result_1.is_skipped()
    var_2 = task_result_1.is_failed()
    bool_4 = {str_2: bool_3}
    task_result_2 = module_1.TaskResult(str_0, str_1, bool_4)
    var_3 = task_result_2.is_skipped()
    var_4 = {}
    task_result_3 = module_1.TaskResult(str_0, str_1, var_4)