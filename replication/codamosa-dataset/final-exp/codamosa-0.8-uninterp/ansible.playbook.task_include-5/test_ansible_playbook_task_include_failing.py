# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0

def test_case_0():
    try:
        str_0 = 'L\x0c[%!\r{zpi3`SJ'
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.load(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.check_options(task_include_0, task_include_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'include_tasks'
        str_1 = {str_0: str_0, str_0: str_0}
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.load_data(str_1)
        var_1 = task_include_0.check_options(var_0, str_1)
        var_2 = len(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'unkno,wn'
        str_1 = 'include_tasks'
        str_2 = {str_1: str_1, str_0: str_1}
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.load_data(str_2)
    except BaseException:
        pass

def test_case_4():
    try:
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.build_parent_block()
        str_0 = 'action'
        str_1 = 'aA0/zTMKbe)|=Aa]'
        str_2 = 'include'
        dict_0 = {str_2: str_1}
        dict_1 = {str_0: dict_0}
        var_1 = task_include_0.load(dict_0, dict_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'action'
        str_1 = 'taSs'
        str_2 = 'bla~'
        str_3 = 'include'
        dict_0 = {str_3: str_1}
        dict_1 = {str_0: dict_0}
        bytes_0 = b'C('
        task_include_0 = module_0.TaskInclude(dict_1, bytes_0)
        var_0 = task_include_0.build_parent_block()
        var_1 = task_include_0.build_parent_block()
        var_2 = task_include_0.load_data(dict_0, bytes_0)
        str_4 = {str_0: str_3, str_1: str_3, str_2: str_2}
        var_3 = task_include_0.preprocess_data(str_4)
        var_4 = task_include_0.get_vars()
    except BaseException:
        pass