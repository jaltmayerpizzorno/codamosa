# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0

def test_case_0():
    try:
        int_0 = -440
        list_0 = [int_0]
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.load(int_0, list_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.build_parent_block()
        list_0 = [task_include_0]
        var_1 = task_include_0.check_options(task_include_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "j+'$A0~8x+15{\t[S86wR"
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.preprocess_data(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        task_include_0 = module_0.TaskInclude()
        str_0 = '\n    GNU Hurd specific subclass of Hardware. Define memory and mount facts\n    based on procfs compatibility translator mimicking the interface of\n    the Linux kernel.\n    '
        str_1 = 'esY`GT?-elGPzs=vlj'
        task_include_1 = module_0.TaskInclude(str_0, str_1)
        var_0 = task_include_1.copy(dict_0, task_include_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'include_tasks'
        var_0 = dict(action=str_0, one=str_0, two=str_0)
        task_include_0 = module_0.TaskInclude(str_0, str_0, str_0)
        var_1 = task_include_0.preprocess_data(var_0)
    except BaseException:
        pass