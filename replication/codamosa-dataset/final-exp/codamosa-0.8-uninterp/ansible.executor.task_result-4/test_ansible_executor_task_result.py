# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'b_^=RL\x0c|"c-l|jZ32{c'
    bool_0 = False
    dict_0 = {str_0: str_0, str_0: str_0, str_0: bool_0, str_0: bool_0}
    task_result_0 = module_0.TaskResult(bool_0, dict_0, dict_0)

def test_case_2():
    str_0 = 'b_^=RL\x0c|"c-l|jZ32{c'
    bool_0 = False
    dict_0 = {str_0: str_0, str_0: str_0, str_0: bool_0, str_0: bool_0}
    task_result_0 = module_0.TaskResult(bool_0, dict_0, dict_0)
    var_0 = task_result_0.is_skipped()

def test_case_3():
    str_0 = 'b_^=RL\x0c|"c-l|jZ32{c'
    bool_0 = False
    dict_0 = {str_0: str_0, str_0: str_0, str_0: bool_0, str_0: bool_0}
    task_result_0 = module_0.TaskResult(bool_0, dict_0, dict_0)
    var_0 = task_result_0.needs_debugger()

def test_case_4():
    str_0 = 'failed'
    str_1 = '_ansible_no_Cog'
    bool_0 = True
    var_0 = {str_0: bool_0, str_0: str_1, str_1: bool_0}
    task_result_0 = module_0.TaskResult(str_0, str_0, var_0)
    var_1 = task_result_0.is_changed()
    var_2 = task_result_0.needs_debugger(str_1)

def test_case_5():
    str_0 = 'sshpass error:'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    float_0 = -2177.19861
    task_result_0 = module_0.TaskResult(dict_0, float_0, dict_0)
    var_0 = task_result_0.is_unreachable()

def test_case_6():
    str_0 = '{"notfailed": true}'
    str_1 = '{"failed": false}'
    task_result_0 = module_0.TaskResult(str_0, str_0, str_1)
    var_0 = task_result_0.is_failed()

def test_case_7():
    str_0 = 'debugger'
    str_1 = 'host'
    str_2 = 'task'
    str_3 = 'always'
    str_4 = {str_0: str_3}
    str_5 = 'changed'
    bool_0 = False
    bool_1 = {str_5: bool_0}
    task_result_0 = module_0.TaskResult(str_1, str_2, bool_1, str_4)
    var_0 = task_result_0.needs_debugger()

def test_case_8():
    str_0 = 'debugger'
    str_1 = 'f.,\\8R\x0c~hgi'
    str_2 = {str_0: str_1}
    str_3 = 'host'
    str_4 = 'task'
    bool_0 = True
    bool_1 = {str_3: bool_0}
    task_result_0 = module_0.TaskResult(str_3, str_4, bool_1, str_2)
    var_0 = task_result_0.needs_debugger()
    str_5 = 'on_unreachable'
    str_6 = {str_0: str_5}
    str_7 = 'unreachable'
    bool_2 = {str_7: bool_0}
    task_result_1 = module_0.TaskResult(str_3, str_4, bool_2, str_6)
    var_1 = task_result_1.needs_debugger()
    var_2 = task_result_0.needs_debugger()
    str_8 = 'always'
    str_9 = {str_0: str_8}
    str_10 = 'changed'
    bool_3 = False
    bool_4 = {str_10: bool_3}
    task_result_2 = module_0.TaskResult(str_3, str_4, bool_4, str_9)
    var_3 = task_result_2.needs_debugger()

def test_case_9():
    str_0 = 'debugger'
    str_1 = {str_0: str_0}
    str_2 = 'host'
    str_3 = 'task'
    bool_0 = True
    bool_1 = {}
    task_result_0 = module_0.TaskResult(str_2, str_3, bool_1, str_1)
    var_0 = task_result_0.needs_debugger()
    str_4 = 'on_unreachable'
    str_5 = {str_0: str_4}
    str_6 = 'unreachable'
    bool_2 = {str_6: bool_0}
    task_result_1 = module_0.TaskResult(str_2, str_3, bool_2, str_5)
    var_1 = task_result_1.needs_debugger()
    str_7 = 'on_skipped'
    str_8 = {str_0: str_7}
    str_9 = 'skipped'
    bool_3 = {str_9: bool_0}
    task_result_2 = module_0.TaskResult(str_2, str_3, bool_3, str_8)
    var_2 = task_result_2.needs_debugger()
    str_10 = 'always'
    str_11 = {str_0: str_10}
    str_12 = 'changed'
    bool_4 = True
    bool_5 = {str_12: bool_4}
    task_result_3 = module_0.TaskResult(str_2, str_3, bool_5, str_11)
    var_3 = task_result_3.needs_debugger()

def test_case_10():
    str_0 = 'changed'
    str_1 = 'results'
    bool_0 = False
    str_2 = 'invocation'
    var_0 = {str_0: bool_0, str_1: str_2}
    str_3 = 'dummy_host'
    var_1 = {}
    task_result_0 = module_0.TaskResult(str_3, var_1, var_0)
    var_2 = task_result_0.is_skipped()

def test_case_11():
    var_0 = None
    str_0 = 'results'
    bool_0 = True
    bool_1 = {str_0: bool_0}
    bool_2 = {str_0: bool_0}
    bool_3 = {str_0: bool_0}
    bool_4 = [bool_1, bool_2, bool_3]
    bool_5 = {str_0: bool_4}
    task_result_0 = module_0.TaskResult(var_0, var_0, bool_5)
    var_1 = task_result_0.is_skipped()

def test_case_12():
    var_0 = None
    str_0 = 'results'
    str_1 = 'skipped'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    bool_2 = {str_1: bool_0}
    bool_3 = {str_1: bool_0}
    bool_4 = [bool_1, bool_2, bool_3]
    bool_5 = {str_0: bool_4}
    task_result_0 = module_0.TaskResult(var_0, var_0, bool_5)
    var_1 = task_result_0.is_skipped()