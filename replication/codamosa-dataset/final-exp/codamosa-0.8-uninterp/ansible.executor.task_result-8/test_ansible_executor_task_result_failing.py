# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0

def test_case_0():
    try:
        str_0 = 'c;f4vH'
        bytes_0 = b'b'
        list_0 = []
        task_result_0 = module_0.TaskResult(str_0, bytes_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 3207.105121
        bool_0 = False
        str_0 = '.)GeU!K!Mmw'
        task_result_0 = module_0.TaskResult(float_0, bool_0, str_0)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "TRyEf'L?-m\x0b"
        str_1 = 'debugger'
        str_2 = 'on_unreachable'
        str_3 = {str_0: str_2, str_0: str_0, str_2: str_0, str_0: str_0, str_1: str_2, str_1: str_0}
        var_0 = {}
        task_result_0 = module_0.TaskResult(str_2, str_2, var_0, str_3)
        var_1 = task_result_0.is_changed()
        var_2 = task_result_0.needs_debugger()
        var_3 = task_result_0.is_skipped()
        var_4 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 0.0
        bool_0 = False
        str_0 = '.)GeU!K!Mmw'
        task_result_0 = module_0.TaskResult(float_0, bool_0, str_0)
        var_0 = task_result_0.is_failed()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'gt\t'
        tuple_0 = ()
        str_1 = '(0x)?[0-9a-f]{8}'
        set_0 = {tuple_0, str_1}
        task_result_0 = module_0.TaskResult(str_0, tuple_0, str_1, set_0)
        var_0 = task_result_0.is_unreachable()
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        list_0 = [bool_0]
        set_0 = set()
        float_0 = 1542.31225
        tuple_0 = (set_0, bool_0, float_0)
        str_0 = 'QbfS'
        task_result_0 = module_0.TaskResult(list_0, tuple_0, str_0)
        var_0 = task_result_0.is_skipped()
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        str_0 = 'EuXjDXEy8e&Frd% '
        bool_1 = True
        task_result_0 = module_0.TaskResult(bool_0, dict_0, str_0, bool_1)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_7():
    try:
        var_0 = None
        str_0 = 'failed_when_result'
        bool_0 = False
        bool_1 = {str_0: bool_0}
        task_result_0 = module_0.TaskResult(var_0, var_0, bool_1)
        var_1 = task_result_0.is_failed()
        str_1 = 'failed'
        bool_2 = {str_1: bool_0}
        task_result_1 = module_0.TaskResult(var_0, var_0, bool_2)
        var_2 = task_result_1.is_failed()
        bool_3 = {str_1: bool_0}
        task_result_2 = module_0.TaskResult(var_0, var_0, bool_3)
        var_3 = task_result_2.is_failed()
        str_2 = 'results'
        bool_4 = {str_1: bool_1}
        bool_5 = [bool_4]
        bool_6 = {str_2: bool_5}
        task_result_3 = module_0.TaskResult(var_0, var_0, bool_6)
        var_4 = task_result_3.is_failed()
    except BaseException:
        pass