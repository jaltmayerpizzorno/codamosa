# Automatically generated by Pynguin.
import pymonet.task as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = -3274.674
    task_0 = module_0.Task(float_0)

def test_case_2():
    bytes_0 = b"'!"
    str_0 = 'r$qx(}44*W<oRf'
    task_0 = module_0.Task(str_0)
    task_1 = module_0.Task(task_0)
    var_0 = task_1.map(bytes_0)

def test_case_3():
    str_0 = '<Y I~9C-;Xj+eFVjSx'
    list_0 = [str_0]
    task_0 = module_0.Task(list_0)
    int_0 = 124
    task_1 = module_0.Task(int_0)
    var_0 = task_1.bind(task_0)