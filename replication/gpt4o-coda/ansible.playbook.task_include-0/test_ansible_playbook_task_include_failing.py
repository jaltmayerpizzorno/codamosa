# Automatically generated by Pynguin.
import ansible.playbook.task_include as module_0

def test_case_0():
    try:
        int_0 = -555
        dict_0 = {int_0: int_0}
        float_0 = 1605.36
        task_include_0 = module_0.TaskInclude(float_0)
        var_0 = task_include_0.load(int_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        task_include_0 = module_0.TaskInclude()
        int_0 = 631
        var_0 = task_include_0.check_options(task_include_0, int_0)
    except BaseException:
        pass