# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0
import ansible.parsing.dataloader as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '^YS=|EXxBCcK[!nJn^Q'
    set_0 = {str_0, str_0, str_0}
    task_result_0 = module_0.TaskResult(str_0, set_0, str_0)

def test_case_2():
    str_0 = '^YS=|EXxBCcK[!nJn^Q'
    set_0 = {str_0, str_0, str_0}
    task_result_0 = module_0.TaskResult(str_0, set_0, str_0)
    var_0 = task_result_0.needs_debugger()

def test_case_3():
    int_0 = 4293
    list_0 = [int_0, int_0]
    int_1 = 1207
    dict_0 = {int_1: int_1}
    task_result_0 = module_0.TaskResult(int_1, int_0, dict_0)
    var_0 = task_result_0.needs_debugger(list_0)

def test_case_4():
    bool_0 = False
    str_0 = 'on_failed'
    var_0 = dict(debugger=str_0, ignore_errors=bool_0)
    var_1 = dict(failed=bool_0)
    str_1 = 'host'
    task_result_0 = module_0.TaskResult(str_1, str_1, var_1, var_0)
    var_2 = task_result_0.needs_debugger(bool_0)
    var_3 = task_result_0.is_skipped()
    task_result_1 = module_0.TaskResult(str_1, str_0, var_1, str_1)

def test_case_5():
    str_0 = 'results'
    bool_0 = False
    bool_1 = {str_0: bool_0, str_0: bool_0}
    bool_2 = {str_0: bool_0, str_0: bool_0, str_0: bool_1}
    var_0 = None
    task_result_0 = module_0.TaskResult(bool_0, bool_1, bool_2, var_0)
    var_1 = task_result_0.is_failed()
    var_2 = task_result_0.is_skipped()
    bool_3 = True
    bool_4 = {str_0: bool_3, str_0: bool_0}
    bool_5 = [bool_4]
    bool_6 = {str_0: bool_0, str_0: bool_0, str_0: bool_5}
    task_result_1 = module_0.TaskResult(var_0, bool_5, bool_6, var_0)

def test_case_6():
    var_0 = None
    var_1 = None
    str_0 = 'failed_when_result'
    str_1 = 'results'
    bool_0 = False
    bool_1 = {str_0: bool_0, str_0: bool_0}
    bool_2 = [bool_1]
    bool_3 = {str_0: bool_0, str_0: bool_0, str_1: bool_2}
    var_2 = None
    task_result_0 = module_0.TaskResult(var_0, var_1, bool_3, var_2)
    var_3 = task_result_0.is_failed()
    var_4 = task_result_0.is_skipped()
    bool_4 = True
    bool_5 = {str_0: bool_4, str_0: bool_0}
    bool_6 = [bool_5]
    bool_7 = {str_1: bool_0, str_0: bool_0, str_1: bool_6}
    task_result_1 = module_0.TaskResult(var_0, var_1, bool_7, var_2)

def test_case_7():
    var_0 = None
    str_0 = 'failed_when_result'
    str_1 = 'results'
    bool_0 = False
    bool_1 = {str_0: bool_0, str_0: bool_0, str_1: bool_0}
    var_1 = None
    task_result_0 = module_0.TaskResult(str_1, var_0, bool_1, var_1)
    var_2 = task_result_0.is_failed()
    var_3 = task_result_0.is_skipped()
    bool_2 = True
    bool_3 = {str_0: bool_2, str_0: bool_0}
    bool_4 = [bool_3]
    bool_5 = {str_1: bool_0, str_0: bool_0, str_1: bool_4}
    task_result_1 = module_0.TaskResult(str_0, var_0, bool_5, var_1)

def test_case_8():
    var_0 = None
    var_1 = None
    var_2 = {}
    str_0 = 'Test case 1. '
    var_3 = print(str_0)
    str_1 = 'results'
    str_2 = 'item'
    str_3 = 'skipped'
    str_4 = '1'
    bool_0 = True
    var_4 = {str_2: str_4, str_3: bool_0}
    str_5 = '2'
    var_5 = {str_2: str_5, str_3: bool_0}
    str_6 = '3'
    var_6 = {str_2: str_6, str_3: bool_0}
    var_7 = [var_4, var_5, var_6]
    var_8 = {str_1: var_7}
    task_result_0 = module_0.TaskResult(var_0, var_1, var_8, var_2)
    var_9 = task_result_0.is_skipped()
    str_7 = 'Test case 2. '
    var_10 = print(str_7)

def test_case_9():
    str_0 = '{"results": [{"failed_when_result": false, "failed": false}, {"failed_when_result": true, "failed": false}, {"failed_when_result": false, "failed": true}]}'
    data_loader_0 = module_1.DataLoader()
    var_0 = data_loader_0.load(str_0)
    str_1 = ''
    task_result_0 = module_0.TaskResult(str_1, var_0, var_0)
    var_1 = task_result_0.is_failed()
    str_2 = '{"results": [{"failed": false}, {"failed": false}]}'
    data_loader_1 = module_1.DataLoader()
    var_2 = data_loader_1.load(str_2)
    task_result_1 = module_0.TaskResult(str_1, str_0, var_2)
    var_3 = task_result_1.is_failed()
    str_3 = '{"results": [], "failed": true}'
    task_result_2 = module_0.TaskResult(str_1, str_3, var_2)
    var_4 = task_result_2.is_failed()

def test_case_10():
    str_0 = 'debugger'
    str_1 = 'ignore_errors'
    var_0 = None
    bool_0 = False
    var_1 = {str_0: var_0, str_1: bool_0}
    str_2 = 'unreachable'
    bool_1 = True
    bool_2 = {str_2: bool_1}
    task_result_0 = module_0.TaskResult(var_0, var_0, bool_2, var_1)
    var_2 = task_result_0.needs_debugger(bool_0)
    var_3 = task_result_0.needs_debugger(bool_1)
    str_3 = 'failed'
    bool_3 = {str_3: bool_1}
    task_result_1 = module_0.TaskResult(var_0, var_0, bool_3, var_1)
    var_4 = task_result_1.needs_debugger(bool_0)