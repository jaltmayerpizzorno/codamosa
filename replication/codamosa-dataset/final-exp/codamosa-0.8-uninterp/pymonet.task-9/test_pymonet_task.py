# Automatically generated by Pynguin.
import pymonet.task as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xd2k\x9bz'
    task_0 = module_0.Task(bytes_0)

def test_case_2():
    float_0 = None
    set_0 = {float_0}
    bytes_0 = b'\xd2k\x9bz'
    task_0 = module_0.Task(bytes_0)
    var_0 = task_0.map(set_0)

def test_case_3():
    float_0 = -198.041
    tuple_0 = ()
    task_0 = module_0.Task(tuple_0)
    var_0 = task_0.bind(float_0)