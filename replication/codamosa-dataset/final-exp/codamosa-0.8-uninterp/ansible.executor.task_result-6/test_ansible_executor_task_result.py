# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'lA1hd9QBo"h+t '
    set_0 = set()
    dict_0 = {str_0: set_0, str_0: set_0}
    task_result_0 = module_0.TaskResult(str_0, set_0, dict_0)

def test_case_2():
    str_0 = 'lA1h9QBo"h+ '
    set_0 = set()
    dict_0 = {str_0: set_0, str_0: set_0}
    task_result_0 = module_0.TaskResult(str_0, set_0, dict_0)
    var_0 = task_result_0.is_failed()

def test_case_3():
    bool_0 = None
    str_0 = '\x0cr%BIL`/%'
    dict_0 = {str_0: str_0, bool_0: bool_0}
    task_result_0 = module_0.TaskResult(dict_0, str_0, dict_0)
    var_0 = task_result_0.needs_debugger()

def test_case_4():
    str_0 = '+Q$V`<\x0c"h\'`/ITofd,r'
    str_1 = 'failed'
    str_2 = 'xddLAVayv\x0c\tW'
    bool_0 = True
    bool_1 = {str_1: bool_0, str_2: bool_0}
    task_result_0 = module_0.TaskResult(str_0, str_0, bool_1)
    var_0 = task_result_0.needs_debugger(str_1)
    var_1 = task_result_0.is_changed()

def test_case_5():
    var_0 = None
    str_0 = 'failed'
    bool_0 = False
    bool_1 = {str_0: bool_0}
    task_result_0 = module_0.TaskResult(var_0, var_0, bool_1)
    bool_2 = True
    bool_3 = {str_0: bool_2}
    task_result_1 = module_0.TaskResult(var_0, var_0, bool_3)
    str_1 = 'results'
    var_1 = task_result_0.is_failed()
    bool_4 = {str_1: bool_0}
    bool_5 = [bool_4]
    bool_6 = {str_1: bool_5}
    task_result_2 = module_0.TaskResult(var_0, var_0, bool_6)
    var_2 = task_result_2.is_failed()
    bool_7 = {str_0: bool_2}
    bool_8 = [bool_7]
    bool_9 = {str_1: bool_8}
    task_result_3 = module_0.TaskResult(var_0, var_0, bool_9)
    bool_10 = {str_0: bool_0}
    bool_11 = {str_0: bool_0}
    bool_12 = [bool_10, bool_11]
    bool_13 = {str_1: bool_12}
    task_result_4 = module_0.TaskResult(var_0, var_0, bool_13)
    task_result_5 = module_0.TaskResult(var_0, var_0, bool_7)
    var_3 = task_result_5.is_failed()

def test_case_6():
    var_0 = None
    var_1 = {}
    task_result_0 = module_0.TaskResult(var_0, var_0, var_1)
    var_2 = task_result_0.is_skipped()
    str_0 = 'results'
    str_1 = 'skipped'
    bool_0 = False
    bool_1 = {str_1: bool_0}
    bool_2 = [bool_1]
    bool_3 = {str_0: bool_2}
    task_result_1 = module_0.TaskResult(var_0, var_0, bool_3)
    var_3 = task_result_1.is_skipped()
    bool_4 = True
    bool_5 = {str_1: bool_4}
    task_result_2 = module_0.TaskResult(var_0, var_0, bool_5)
    var_4 = task_result_2.is_skipped()
    bool_6 = {str_1: bool_0}
    task_result_3 = module_0.TaskResult(var_0, var_0, bool_6)
    var_5 = task_result_3.is_skipped()
    bool_7 = {str_1: bool_4}
    task_result_4 = module_0.TaskResult(var_0, var_0, bool_7)

def test_case_7():
    var_0 = None
    var_1 = {}
    task_result_0 = module_0.TaskResult(var_0, var_0, var_1)
    var_2 = task_result_0.is_skipped()
    str_0 = 'results'
    str_1 = 'skipped'
    bool_0 = False
    bool_1 = {str_1: bool_0}
    bool_2 = [bool_1]
    bool_3 = {str_0: bool_2}
    task_result_1 = module_0.TaskResult(var_0, var_0, bool_3)
    var_3 = task_result_1.is_skipped()
    bool_4 = True
    bool_5 = {str_1: bool_4}
    bool_6 = [bool_5]
    bool_7 = {str_0: bool_6}
    task_result_2 = module_0.TaskResult(var_0, var_0, bool_7)
    var_4 = task_result_2.is_skipped()
    bool_8 = {str_1: bool_0}
    task_result_3 = module_0.TaskResult(var_0, var_0, bool_8)
    var_5 = task_result_3.is_skipped()
    bool_9 = {str_1: bool_4}
    task_result_4 = module_0.TaskResult(var_0, var_0, bool_9)

def test_case_8():
    var_0 = None
    var_1 = {}
    str_0 = 'debugger'
    str_1 = 'always'
    str_2 = {str_0: str_1}
    task_result_0 = module_0.TaskResult(str_2, var_0, var_1, str_2)
    var_2 = task_result_0.needs_debugger()
    str_3 = 'on_failed'
    str_4 = {str_0: str_3}
    task_result_1 = module_0.TaskResult(str_2, var_0, var_1, str_4)
    var_3 = task_result_1.needs_debugger()

def test_case_9():
    str_0 = 'host'
    var_0 = None
    var_1 = {}
    var_2 = {}
    task_result_0 = module_0.TaskResult(str_0, var_0, var_1, var_2)
    var_3 = task_result_0.needs_debugger()
    str_1 = 'debugger'
    str_2 = 'always'
    str_3 = {str_1: str_2}
    task_result_1 = module_0.TaskResult(str_0, var_0, var_1, str_3)
    var_4 = task_result_1.needs_debugger()
    str_4 = 'on_failed'
    str_5 = {str_1: str_4}
    task_result_2 = module_0.TaskResult(str_0, var_0, var_1, str_5)
    var_5 = task_result_2.needs_debugger()
    str_6 = 'failed'
    bool_0 = True
    bool_1 = {str_6: bool_0}
    task_result_3 = module_0.TaskResult(str_0, var_0, bool_1, str_5)
    var_6 = task_result_3.needs_debugger()