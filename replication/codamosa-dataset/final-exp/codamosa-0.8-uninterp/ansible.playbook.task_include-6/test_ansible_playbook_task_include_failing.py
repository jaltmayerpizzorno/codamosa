# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0
import ansible.playbook.task as module_1

def test_case_0():
    try:
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.copy()
        int_0 = -42
        int_1 = -3389
        var_1 = task_include_0.load(int_0, int_1)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -4816.5851
        task_0 = module_1.Task(float_0)
        task_include_0 = module_0.TaskInclude(float_0)
        var_0 = task_include_0.check_options(task_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        task_include_0 = module_0.TaskInclude()
        str_0 = 'action'
        str_1 = 'args'
        str_2 = '/home/src'
        str_3 = {str_0: str_2, str_1: str_0}
        str_4 = {str_0: str_2, str_1: str_3}
        var_0 = task_include_0.load(str_4, task_include_0, task_include_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'apply'
        str_1 = 'include_tasks'
        dict_0 = {str_1: str_0, str_1: str_1, str_0: str_0, str_0: str_0}
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.preprocess_data(dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        task_include_0 = module_0.TaskInclude()
        str_0 = 'action'
        str_1 = 'F;oiPTJ6f<9'
        str_2 = 'copy'
        str_3 = 'dest'
        var_0 = task_include_0.get_vars()
        str_4 = {str_0: str_2, str_1: str_3}
        var_1 = None
        var_2 = task_include_0.load(str_4, var_1, var_1)
    except BaseException:
        pass