# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0
import ansible.playbook.task as module_1

def test_case_0():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        set_0 = set()
        str_0 = 'iJ'
        list_0 = [str_0, str_0, str_0]
        task_include_0 = module_0.TaskInclude(list_0)
        var_0 = task_include_0.load(dict_0, set_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        task_0 = module_1.Task()
        bytes_0 = b'\x10\x8a\xb6\xb8<\xa4\x8c'
        task_include_0 = module_0.TaskInclude(bytes_0)
        var_0 = task_include_0.check_options(task_0, task_include_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.preprocess_data(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'block'
        str_1 = 'collections'
        str_2 = 'tasks'
        str_3 = 'include_role'
        var_0 = []
        var_1 = {str_3: str_3, str_1: str_3, str_1: str_1, str_2: var_0}
        var_2 = [var_1]
        var_3 = {str_0: var_2}
        task_include_0 = module_0.TaskInclude()
        int_0 = 0
        var_4 = var_3[str_0][int_0]
        var_5 = task_include_0.preprocess_data(var_4)
    except BaseException:
        pass