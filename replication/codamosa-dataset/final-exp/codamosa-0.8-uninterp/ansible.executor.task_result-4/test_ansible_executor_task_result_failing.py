# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0

def test_case_0():
    try:
        str_0 = "\tX!Hs9'n~YO[ x;A@K"
        bool_0 = True
        list_0 = [bool_0]
        task_result_0 = module_0.TaskResult(str_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'b_^=RL\x0c|"c-l|jZ32{c'
        bool_0 = False
        dict_0 = {str_0: str_0, str_0: str_0, str_0: bool_0, str_0: bool_0}
        task_result_0 = module_0.TaskResult(bool_0, dict_0, dict_0)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0, tuple_0]
        str_0 = "F^#'<QUyu`}lGKQBtE.]"
        task_result_0 = module_0.TaskResult(list_0, tuple_0, str_0)
        var_0 = task_result_0.is_unreachable()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'b_^=RL\x0c|"c-l|jZ32{c'
        bool_0 = False
        dict_0 = {str_0: str_0, str_0: str_0, str_0: bool_0, str_0: bool_0}
        task_result_0 = module_0.TaskResult(bool_0, dict_0, dict_0)
        int_0 = 2033
        var_0 = task_result_0.needs_debugger(int_0)
        var_1 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        str_0 = 'results'
        bool_1 = {str_0: bool_0}
        var_0 = None
        task_result_0 = module_0.TaskResult(var_0, var_0, bool_1)
        var_1 = task_result_0.is_skipped()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'debugger'
        str_1 = 'on_failed'
        str_2 = {str_0: str_1}
        str_3 = 'task'
        str_4 = 'failed'
        bool_0 = True
        bool_1 = {str_4: bool_0}
        task_result_0 = module_0.TaskResult(str_0, str_3, bool_1, str_2)
        var_0 = task_result_0.needs_debugger()
        var_1 = task_result_0.needs_debugger()
        var_2 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = None
        str_0 = '_ansible_no_Cog'
        bool_0 = True
        var_1 = {str_0: bool_0, str_0: str_0, str_0: bool_0}
        task_result_0 = module_0.TaskResult(var_0, var_0, var_1)
        var_2 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'debugger'
        str_1 = 'on_failed'
        str_2 = {str_0: str_1}
        str_3 = 'homt'
        str_4 = 'task'
        str_5 = 'failed'
        bool_0 = True
        bool_1 = {str_5: bool_0}
        task_result_0 = module_0.TaskResult(str_3, str_4, bool_1, str_2)
        var_0 = task_result_0.needs_debugger()
        str_6 = 'on_unreachable'
        str_7 = {str_0: str_6}
        bool_2 = {str_1: bool_0}
        task_result_1 = module_0.TaskResult(str_3, str_4, bool_2, str_7)
        var_1 = task_result_1.needs_debugger()
        str_8 = {str_1: str_6, var_1: bool_1, str_3: task_result_1}
        bool_3 = {str_6: str_5, str_6: bool_2}
        task_result_2 = module_0.TaskResult(str_3, str_4, bool_3, str_8)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'debugger'
        str_1 = 'on_failed'
        str_2 = {str_0: str_1}
        str_3 = 'task'
        str_4 = 'fa)lned'
        bool_0 = True
        bool_1 = {str_4: bool_0}
        task_result_0 = module_0.TaskResult(str_0, str_3, bool_1, str_2)
        var_0 = task_result_0.needs_debugger()
        var_1 = task_result_0.needs_debugger()
        var_2 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'debugger'
        str_1 = {str_0: str_0}
        str_2 = 'hos;t'
        str_3 = ''
        bool_0 = True
        bool_1 = {str_0: bool_0, str_2: bool_0}
        task_result_0 = module_0.TaskResult(str_2, str_3, bool_1, str_1)
        var_0 = task_result_0.needs_debugger()
        str_4 = '(i'
        dict_0 = {str_4: str_2, var_0: task_result_0}
        var_1 = task_result_0.needs_debugger(dict_0)
        str_5 = 'on_skipped'
        str_6 = {str_0: str_5}
        bool_2 = {var_0: str_3}
        task_result_1 = module_0.TaskResult(str_2, str_3, bool_2, str_6)
        var_2 = task_result_1.needs_debugger()
        var_3 = task_result_1.is_unreachable()
        var_4 = task_result_0.is_skipped()
        var_5 = task_result_0.is_failed()
        var_6 = task_result_0.is_unreachable()
        var_7 = task_result_0.is_failed()
        var_8 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'fakehost1'
        var_0 = None
        bool_0 = True
        var_1 = None
        var_2 = dict(failed=bool_0, results=var_1)
        task_result_0 = module_0.TaskResult(str_0, str_0, var_2, var_0)
        var_3 = task_result_0.is_failed()
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'debugger'
        bool_0 = True
        str_1 = {str_0: str_0}
        str_2 = 'unreachable'
        bool_1 = {str_2: bool_0}
        task_result_0 = module_0.TaskResult(str_1, str_1, bool_1, str_1)
        var_0 = task_result_0.is_failed()
        var_1 = task_result_0.is_changed()
        var_2 = task_result_0.needs_debugger()
        var_3 = task_result_0.needs_debugger(str_1)
        var_4 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_12():
    try:
        var_0 = None
        str_0 = '{"results": [{"failed": "si", "changed": "si"}, {"failed": false, "changed": "si"}]}'
        task_result_0 = module_0.TaskResult(var_0, var_0, str_0)
        var_1 = task_result_0.is_failed()
    except BaseException:
        pass