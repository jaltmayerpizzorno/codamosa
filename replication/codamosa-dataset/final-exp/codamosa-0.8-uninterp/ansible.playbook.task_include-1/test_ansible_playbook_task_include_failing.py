# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0

def test_case_0():
    try:
        task_include_0 = module_0.TaskInclude()
        float_0 = -132.0
        var_0 = task_include_0.load(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        str_0 = "K8ihL]}n\ru'"
        task_include_0 = module_0.TaskInclude(str_0)
        var_0 = task_include_0.check_options(task_include_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 65001
        task_include_0 = module_0.TaskInclude()
        bool_0 = True
        var_0 = task_include_0.copy(bool_0)
        var_1 = task_include_0.preprocess_data(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'FoEJ4Y4(R(]FlI(DT\x0b'
        bool_0 = False
        task_include_0 = module_0.TaskInclude(str_0, bool_0)
        var_0 = task_include_0.copy()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'include'
        var_0 = {}
        var_1 = dict(action=str_0, apply=var_0)
        task_include_0 = module_0.TaskInclude()
        var_2 = task_include_0.load_data(var_1)
    except BaseException:
        pass