# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0

def test_case_0():
    try:
        float_0 = 4284.94472
        task_result_0 = module_0.TaskResult(float_0, float_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\\.7lz#|'
        task_result_0 = module_0.TaskResult(str_0, str_0, str_0)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'failed'
        bool_0 = False
        set_0 = set()
        float_0 = -373.6
        dict_0 = {str_0: set_0, str_0: bool_0, str_0: float_0, str_0: bool_0}
        task_result_0 = module_0.TaskResult(bool_0, set_0, dict_0)
        int_0 = None
        set_1 = {float_0, int_0}
        var_0 = task_result_0.is_changed()
        var_1 = task_result_0.needs_debugger(set_1)
        var_2 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '127.0.0.1'
        task_result_0 = module_0.TaskResult(str_0, str_0, str_0)
        var_0 = task_result_0.needs_debugger(task_result_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'failed'
        bool_0 = True
        set_0 = set()
        float_0 = -373.57
        dict_0 = {str_0: set_0, str_0: bool_0, str_0: float_0, str_0: bool_0}
        task_result_0 = module_0.TaskResult(bool_0, set_0, dict_0)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '127.0.0.1'
        task_result_0 = module_0.TaskResult(str_0, str_0, str_0)
        var_0 = task_result_0.is_skipped()
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = {}
        str_0 = 'results'
        str_1 = 'skipped'
        bool_0 = True
        bool_1 = {str_1: bool_0}
        bool_2 = {str_0: bool_1}
        task_result_0 = module_0.TaskResult(str_1, var_0, bool_2, var_0)
        var_1 = task_result_0.is_skipped()
        var_2 = {}
        task_result_1 = module_0.TaskResult(str_0, var_0, bool_0, var_2)
    except BaseException:
        pass

def test_case_7():
    try:
        var_0 = {}
        str_0 = 'results'
        str_1 = 'skipped'
        bool_0 = True
        str_2 = 'host'
        bool_1 = {str_2: bool_0}
        bool_2 = {str_1: bool_0}
        bool_3 = [bool_1, bool_2]
        bool_4 = {str_0: bool_3}
        task_result_0 = module_0.TaskResult(str_2, var_0, bool_4, var_0)
        var_1 = task_result_0.is_skipped()
        var_2 = {}
        task_result_1 = module_0.TaskResult(str_2, var_0, bool_0, var_2)
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = None
        var_1 = {}
        str_0 = 'debugger'
        str_1 = 'always'
        str_2 = {str_0: str_1}
        task_result_0 = module_0.TaskResult(var_0, var_0, var_1, str_2)
        bool_0 = False
        var_2 = task_result_0.needs_debugger(bool_0)
        var_3 = {}
        str_3 = 'never'
        str_4 = {str_0: str_3}
        task_result_1 = module_0.TaskResult(var_0, var_0, var_3, str_4)
        var_4 = task_result_1.needs_debugger(bool_0)
        var_5 = {}
        str_5 = 'on_failed'
        var_6 = task_result_1.is_skipped()
        str_6 = {str_0: str_5}
        task_result_2 = module_0.TaskResult(var_0, var_0, var_5, str_6)
        var_7 = task_result_2.needs_debugger(bool_0)
        var_8 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = {}
        str_0 = 'debugger'
        str_1 = {str_0: str_0}
        task_result_0 = module_0.TaskResult(var_0, var_0, var_0, str_1)
        task_result_1 = module_0.TaskResult(var_0, var_0, str_1, str_0)
        var_1 = task_result_0.is_failed()
        str_2 = 'on_failed'
        var_2 = task_result_1.is_skipped()
        str_3 = {str_0: str_2}
        task_result_2 = module_0.TaskResult(str_1, str_1, str_3, str_3)
        var_3 = task_result_2.needs_debugger(task_result_1)
        var_4 = task_result_2.clean_copy()
    except BaseException:
        pass